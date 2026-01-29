import os
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.lines import Line2D

RAW_METRICS = ["SHR", "2-gram", "1-gram", "WPI", "SPI"]
CATEGORIES = ["SHR", "SPI", "WPI", "1-gram", "2-gram"]
CATEGORY_LABELS = CATEGORIES

MODEL = "R1-Onevision"
METHODS = [
    "vanilla",
    "RLAIF-V",
    "OPA-DPO",
    "C3PO",
]

DATA = {
    MODEL: {
        "vanilla": [0.407, 0.937, 0.702, 147.27, 8.915],
        "RLAIF-V": [0.389, 0.959, 0.689, 151.725, 9.595],
        "OPA-DPO": [0.402, 0.694, 0.446, 321.88, 21.24],
        "C3PO": [0.379, 0.927, 0.661, 174.84, 10.71],
    },
}

COLORS_LIST = [
    ("#A2CFFE", "#0077BB"),
    ("#D5AAFF", "#845EC2"),
    ("#B5EAD7", "#00A676"),
    ("#FFB6B9", "#D7263D"),
]
PALETTE = dict(zip(METHODS, COLORS_LIST))
INVERT_METRICS = {"SHR"}

SCALES = {
    MODEL: [
        [41, 37.8],       # SHR (descending)
        [2, 12],        # SPI
        [100, 180],     # WPI
        [0.4, 0.71],       # 1-gram
        [0.68, 0.96],     # 2-gram
    ]
}


def _font(size: int, weight=None, style=None) -> font_manager.FontProperties:
    return font_manager.FontProperties(family="Times New Roman", size=size, weight=weight, style=style)


def _materialize_scales(scales_def):
    if isinstance(scales_def, list):
        items = list(scales_def)
        pairs = {k: v for k, v in zip(CATEGORIES, items)}
    elif isinstance(scales_def, dict):
        pairs = dict(scales_def)
    else:
        raise TypeError("scales_def must be list or dict")

    resolved: dict[str, list[float]] = {}
    for cat in CATEGORIES:
        arr = pairs[cat]
        if len(arr) == 2:
            ring1, outer = arr
            step = (outer - ring1) / 3.0
            scale = [ring1 - step, ring1, ring1 + step, ring1 + 2 * step, outer]
            resolved[cat] = scale
        else:
            resolved[cat] = list(arr)
    return resolved


def _normalize(value: float, scale: list[float]) -> float:
    for i in range(len(scale) - 1):
        low, high = scale[i], scale[i + 1]
        if (low <= value <= high) or (low >= value >= high):
            span = abs(high - low)
            dist = abs(value - low)
            pos = 0 if span == 0 else dist / span
            return (i + pos) / (len(scale) - 1) * 100
    if scale[0] < scale[-1]:
        return 0.0 if value < scale[0] else 100.0
    else:
        return 0.0 if value > scale[0] else 100.0


def _plot_radar(ax, model: str, scales_def):
    scales = _materialize_scales(scales_def)

    angles = [((n) / float(len(CATEGORIES)) * 2 * math.pi + math.pi / 2) % (2 * math.pi) for n in range(len(CATEGORIES))]
    angles += angles[:1]

    for ang in angles[:-1]:
        ax.plot([ang, ang], [0, 100], color="#bbbbbb", linewidth=0.8, alpha=0.6)

    for method in METHODS:
        raw_vals = DATA[model][method]
        metric_map = dict(zip(RAW_METRICS, raw_vals))
        ordered_vals = [metric_map[k] * 100 if k == "SHR" else metric_map[k] for k in CATEGORIES]
        norm_vals = [_normalize(v, scales[k]) for k, v in zip(CATEGORIES, ordered_vals)]
        normalized = list(norm_vals)
        normalized += normalized[:1]
        fill_color, line_color = PALETTE[method]
        ax.fill(angles, normalized, color=fill_color, alpha=0.6)
        ax.plot(angles, normalized, color=line_color, linewidth=2, label=method)

    ax.set_xticks([])
    for angle, label in zip(angles[:-1], CATEGORY_LABELS):
        if label == "2-gram":
            r_label = 116
        elif label == "SHR":
            r_label = 106
        else:
            r_label = 112
        ax.text(angle, r_label, label, ha="center", va="center", fontsize=16, fontproperties=_font(16))

    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels(["", "", "", "", ""], fontproperties=_font(10))
    ax.set_title(model, fontproperties=_font(26, weight="bold"), y=1.08)
    ax.spines["polar"].set_visible(False)
    ax.grid(color="gray", linestyle="-", linewidth=0.8, alpha=0.6)

    for cat, theta in zip(CATEGORIES, angles[:-1]):
        scale = scales[cat]
        ticks_to_label = scale[1:]
        for idx, tick in enumerate(ticks_to_label):
            is_outer = idx == len(ticks_to_label) - 1
            if is_outer:
                inner = scale[-2]
                outer = scale[-1]
                tick_display = (inner + outer) / 2.0
                r_linear = (_normalize(inner, scale) + _normalize(outer, scale)) / 2.0
            else:
                tick_display = tick
                r_linear = _normalize(tick_display, scale)

            if cat == "WPI":
                label = f"{tick_display:.0f}"
            elif cat == "SPI":
                label = f"{tick_display:.1f}"
            elif cat == "SHR":
                label = f"{tick_display:.1f}"
            elif cat in {"1-gram", "2-gram"}:
                label = f"{tick_display:.2f}"
            else:
                label = f"{tick_display:.2f}"

            ax.text(
                theta,
                r_linear,
                label,
                ha="center",
                va="center",
                fontsize=7.5,
                color="#333333",
                alpha=0.95,
                fontweight="normal",
            )


def main():
    fig, ax = plt.subplots(1, 1, figsize=(7, 7), subplot_kw={"polar": True})

    scales_def = SCALES.get(MODEL)
    _plot_radar(ax, MODEL, scales_def)

    legend_handles = [
        Line2D([0], [0], color=PALETTE[m][1], linewidth=7, solid_capstyle="round", label=m)
        for m in METHODS
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.045),
        ncol=4,
        frameon=False,
        prop=_font(14),
        handlelength=4.0,
        borderpad=0.18,
        labelspacing=0.55,
        columnspacing=2.2,
        handletextpad=0.45,
    )
    for txt in leg.get_texts():
        if txt.get_text() == "vanilla":
            txt.set_fontproperties(_font(22, style="italic"))
            txt.set_fontstyle("italic")
        else:
            txt.set_fontproperties(_font(18))

    fig.subplots_adjust(top=0.9, bottom=0.18, left=0.06, right=0.94)

    repo_root = os.path.dirname(os.path.dirname(__file__))
    out_dir = os.path.join(repo_root, "bench_plots")
    os.makedirs(out_dir, exist_ok=True)
    fig.savefig(os.path.join(out_dir, "r1-onevision_radar.png"), dpi=400, bbox_inches="tight")
    fig.savefig(os.path.join(out_dir, "r1-onevision_radar.pdf"), dpi=400, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
