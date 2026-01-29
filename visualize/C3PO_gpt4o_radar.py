import os
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

RAW_METRICS = ["SHR", "2-gram", "1-gram", "WPI", "SPI"]
CATEGORIES = ["SHR", "SPI", "WPI", "1-gram", "2-gram"]
CATEGORY_LABELS = CATEGORIES

MODELS = ["Orsta-R1", "MM-Eureka", "MM-R1", "ThinkLite"]
METHODS = ["vanilla", "RLAIF-V", "OPA-DPO", "C3PO"]

DATA = {
    "Orsta-R1": {
        "vanilla": [0.306, 0.937, 0.617, 146.94, 8.48],
        "RLAIF-V": [0.288, 0.940, 0.619, 142.90, 8.075],
        "OPA-DPO": [0.296, 0.937, 0.612, 149.62, 8.445],
        "C3PO": [0.263, 0.927, 0.602, 168.535, 10.065],
    },
    "ThinkLite": {
        "vanilla": [0.321, 0.930, 0.601, 156.175, 8.525],
        "RLAIF-V": [0.300, 0.933, 0.605, 156.33, 8.525],
        "OPA-DPO": [0.301, 0.900, 0.595, 163.89, 8.77],
        "C3PO": [0.285, 0.917, 0.578, 180.185, 10.11],
    },
    "MM-Eureka": {
        "vanilla": [0.306, 0.947, 0.632, 152.13, 8.62],
        "RLAIF-V": [0.286, 0.951, 0.649, 154.14, 8.715],
        "OPA-DPO": [0.301, 0.946, 0.631, 148.605, 8.455],
        "C3PO": [0.281, 0.940, 0.616, 153.855, 8.895],
    },
    "MM-R1": {
        "vanilla": [0.298, 0.927, 0.593, 151.37, 8.27],
        "RLAIF-V": [0.301, 0.934, 0.607, 151.42, 8.295],
        "OPA-DPO": [0.299, 0.928, 0.597, 157.065, 8.545],
        "C3PO": [0.279, 0.921, 0.587, 161.095, 9.08],
    },
}

SCALES = {
    "Orsta-R1": [
        [32, 26],       # SHR (descending)
        [7, 10.2],        # SPI
        [100, 175],     # WPI
        [0.5, 0.62],       # 1-gram
        [0.8, 0.95],     # 2-gram
    ],
    "ThinkLite": [
        [33, 28.2],      
        [7, 10.2],        
        [100, 182],     
        [0.4, 0.61],       
        [0.8, 0.95],     
    ],
    "MM-Eureka": [
        [30.8, 28],    
        [8, 9],    
        [120, 155],   
        [0.5, 0.65],       
        [0.82, 0.96],   
    ],
    "MM-R1": [
        [32, 27.8],      
        [7, 9.1],       
        [120, 165],    
        [0.5, 0.61],      
        [0.8, 0.94],    
    ],
}

COLORS_LIST = [
    ("#A2CFFE", "#0077BB"),  # vanilla
    ('#D5AAFF', '#845EC2'),  # RLAIF-V
    ("#B5EAD7", "#00A676"),  # OPA-DPO
    ('#FFB6B9', '#D7263D'),  # C3PO
]

PALETTE = dict(zip(METHODS, COLORS_LIST))
INVERT_METRICS = {"SHR"}

def _font(size: int, weight=None, style=None) -> font_manager.FontProperties:
    return font_manager.FontProperties(family="Times New Roman", size=size, weight=weight, style=style)


def _build_scales_for_model(model: str) -> dict[str, list[float]]:
    scales: dict[str, list[float]] = {}
    model_data = DATA[model]
    for key in CATEGORIES:
        vals = []
        for method in METHODS:
            raw_vals = model_data[method]
            metric_map = dict(zip(RAW_METRICS, raw_vals))
            val = metric_map[key]
            if key == "SHR":
                val *= 100  
            vals.append(val)
        best = min(vals) if key in INVERT_METRICS else max(vals)
        worst = max(vals) if key in INVERT_METRICS else min(vals)
        span = max(1e-6, abs(best - worst))
        pad = max(span * 0.05, abs(best) * 0.02)
        if key in INVERT_METRICS:
            high = worst + pad 
            low = best - pad 
            scale = list(np.linspace(high, low, 5))  
        else:
            low = worst - pad
            high = best + pad
            scale = list(np.linspace(low, high, 5))  
        scales[key] = scale
    return scales


def _materialize_scales(scales_def):
    if isinstance(scales_def, list):
        items = list(scales_def)
        if len(items) != len(CATEGORIES):
            raise ValueError("Scale list must align with CATEGORIES length")
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


def _plot_radar(ax, model: str, scales: dict[str, list[float]]):
    scales = _materialize_scales(scales) if not isinstance(scales, dict) or any(len(v) == 2 for v in (scales.values() if isinstance(scales, dict) else scales)) else scales

    angles = [((n) / float(len(CATEGORIES)) * 2 * math.pi + math.pi / 2) % (2 * math.pi) for n in range(len(CATEGORIES))]
    angles += angles[:1]

    for ang in angles[:-1]:
        ax.plot([ang, ang], [0, 100], color="#bbbbbb", linewidth=0.8, alpha=0.6)

    for method in METHODS:
        raw_vals = DATA[model][method]
        metric_map = dict(zip(RAW_METRICS, raw_vals))
        # Convert SHR to percent for both normalization and label display
        ordered_vals = [metric_map[k] * 100 if k == "SHR" else metric_map[k] for k in CATEGORIES]
        norm_vals = [_normalize(v, scales[k]) for k, v in zip(CATEGORIES, ordered_vals)]

        # Use linear normalized values 
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
            r_label = 106  # move SHR closer to the circle
        else:
            r_label = 112
        ax.text(angle, r_label, label, ha="center", va="center", fontsize=16, fontproperties=_font(16))

    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels(["", "", "", "", ""], fontproperties=_font(10))
    title_text = ax.set_title(model, fontproperties=_font(26, weight="bold"), y=1.08)
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
    fig, axes = plt.subplots(1, 4, figsize=(22, 7.5), subplot_kw={"polar": True})

    for ax, model in zip(axes, MODELS):
        scales_def = SCALES.get(model, _build_scales_for_model(model))
        _plot_radar(ax, model, scales_def)

    legend_handles = [
        Line2D([0], [0], color=PALETTE[m][1], linewidth=7, solid_capstyle="round", label=m)
        for m in METHODS
    ]
    leg = fig.legend(
        handles=legend_handles,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.08),
        ncol=4,
        frameon=False,
        prop=_font(20),
        handlelength=6.0,
        borderpad=0.3,
        labelspacing=0.8,
        columnspacing=5.0,
        handletextpad=0.8,
    )
    for txt in leg.get_texts():
        if txt.get_text() == "vanilla":
            txt.set_fontproperties(_font(32, style="italic"))
            txt.set_fontstyle("italic")
        else:
            txt.set_fontproperties(_font(24))

    fig.subplots_adjust(top=0.9, bottom=0.15, left=0.03, right=0.97, wspace=0.21)

    repo_root = os.path.dirname(os.path.dirname(__file__))
    out_dir = os.path.join(repo_root, "bench_plots")
    os.makedirs(out_dir, exist_ok=True)
    fig.savefig(os.path.join(out_dir, "gpt4o_radar.png"), dpi=400, bbox_inches="tight")
    fig.savefig(os.path.join(out_dir, "gpt4o_radar.pdf"), dpi=400, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
