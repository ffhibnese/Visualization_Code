import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.ticker import MultipleLocator

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'

LAMBDAS = ["0.5", "1.0", "1.5", "2.0", "2.5", "3.0"]

PALETTE = {
    "CHAIRs": "#4987CA",
    "CHAIRi": "#635AC2",
    "SHR": "#A6D1A3"
}

def _font(size: int) -> font_manager.FontProperties:
    return font_manager.FontProperties(family="Times New Roman", size=size)


MODELS_CONFIG = {

    "R1-Onevision": {
        # λ : 0, 0.5, 1.0, 1.5, 2.0, 2.5
        "chairs":  [40.7, 35, 38.7, 36.3, 38, 37.3],
        "chairi":  [7.9, 7.4, 7.6, 7.5, 7.6, 7.7],
        "shr_raw": [0.392, 0.379, 0.383, 0.387, 0.392, 0.401],

        "line_ylim_s": (28, 42),
        "line_s_locator": 3.0,

        "line_ylim_i": (6.5, 10.5),
        "line_i_locator": 1.0,

        "bar_ylim": (37.0, 41.0),
        "bar_locator": 1.0
    },

    "MM-Eureka": {
        "chairs":  [40.0, 40.0, 40.0, 40.3, 42.0, 41.3],
        "chairi":  [8.0, 8.7, 7.7, 8.0, 7.8, 7.5],
        "shr_raw": [0.283, 0.304, 0.281, 0.294, 0.305, 0.300],

        "line_ylim_s": (35, 43),
        "line_s_locator": 2.0,

        "line_ylim_i": (5.5, 13),
        "line_i_locator": 2.0,

        "bar_ylim": (27.0, 31.5),
        "bar_locator": 1.0
    },

    "Orsta-R1": {
        "chairs":  [36, 38.7, 36, 35.3, 38.7, 38],
        "chairi":  [7.9, 7.9, 7.2, 6.9, 7.3, 7],
        "shr_raw": [0.282, 0.279, 0.288, 0.263, 0.297, 0.294],

        "line_ylim_s": (28, 40),
        "line_s_locator": 3.0,

        "line_ylim_i": (6.2, 10.5),
        "line_i_locator": 1.0,

        "bar_ylim": (25.0, 31.0),
        "bar_locator": 1.0
    },

    "MM-R1": {
        "chairs":  [37.7, 36.7, 36.7, 35, 34.3, 38.3],
        "chairi":  [7.1, 7.3, 7.4, 7.2, 7.3, 7.5],
        "shr_raw": [0.319, 0.284, 0.299, 0.279, 0.303, 0.286],

        "line_ylim_s": (26, 40),
        "line_s_locator": 3.0,

        "line_ylim_i": (5.8, 9.5),
        "line_i_locator": 1.0,

        "bar_ylim": (27.0, 33.0),
        "bar_locator": 1.0
    },

    "ThinkLite": {
        "chairs":  [39.3, 38, 38, 42, 40, 38.7],
        "chairi":  [7.8, 7.3, 7.6, 7.3, 6.9, 7.6],
        "shr_raw": [0.308, 0.285, 0.302, 0.292, 0.31, 0.292],

        "line_ylim_s": (32, 43.5),
        "line_s_locator": 3.0,

        "line_ylim_i": (6.2, 10.5),
        "line_i_locator": 1.0,

        "bar_ylim": (27.0, 31.5),
        "bar_locator": 1.0
    },
}


def _get_x_and_labels(model_name):
    if model_name == "R1-Onevision":
        labels = ["0.0", "0.5", "1.0", "1.5", "2.0", "2.5"]
    else:
        labels = LAMBDAS
    x = np.arange(len(labels))
    return x, labels


def plot_line_chart(model_name, config, out_dir):
    chairs = config["chairs"]
    chairi = config["chairi"]

    fig, ax1 = plt.subplots(figsize=(7.0, 4.35))
    fig.patch.set_facecolor((1, 1, 1))
    ax1.set_facecolor((247/255, 247/255, 247/255))

    x, labels = _get_x_and_labels(model_name)

    ax1.plot(x, chairs, marker='o', markersize=8,
             color=PALETTE["CHAIRs"], linewidth=2.8,
             label=r'CHAIR$_S$ ($\downarrow$)',
             markeredgecolor='white', zorder=5)

    ax1.set_xlabel(r'$\lambda_{\mathrm{DPO}}$', fontproperties=_font(27))
    ax1.set_ylabel(r'CHAIR$_S$', fontproperties=_font(26))
    ax1.tick_params(axis='y', labelsize=25)
    ax1.set_ylim(config["line_ylim_s"])
    ax1.yaxis.set_major_locator(MultipleLocator(base=config["line_s_locator"]))

    ax2 = ax1.twinx()
    ax2.plot(x, chairi, marker='s', markersize=8,
             color=PALETTE["CHAIRi"], linewidth=2.8,
             label=r'CHAIR$_I$ ($\downarrow$)',
             markeredgecolor='white', zorder=5)

    ax2.set_ylabel(r'CHAIR$_I$', fontproperties=_font(26))
    ax2.tick_params(axis='y', labelsize=25)
    ax2.set_ylim(config["line_ylim_i"])
    ax2.yaxis.set_major_locator(MultipleLocator(base=config["line_i_locator"]))

    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontproperties=_font(25))
    ax1.grid(True, axis='y', linestyle='--', alpha=0.5)

    lns = ax1.get_lines() + ax2.get_lines()
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc='upper center',
               bbox_to_anchor=(0.5, 1.24),
               ncol=2, frameon=False, prop=_font(18))

    fig.tight_layout(pad=0.1)
    safe_name = model_name.replace(" ", "_")
    fig.savefig(os.path.join(out_dir, f"{safe_name}_lambda_line.png"),
                dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(out_dir, f"{safe_name}_lambda_line.pdf"),
                dpi=300, bbox_inches='tight')
    plt.close(fig)


def plot_bar_chart(model_name, config, out_dir):
    shr_pct = [v * 100 for v in config["shr_raw"]]
    fig, ax = plt.subplots(figsize=(7.0, 3.9))
    fig.patch.set_facecolor((1, 1, 1))
    ax.set_facecolor((247/255, 247/255, 247/255))

    x, labels = _get_x_and_labels(model_name)

    ax.bar(x, shr_pct, width=0.60,
           color=PALETTE["SHR"],
           edgecolor="black", linewidth=1.3)

    ax.set_xlabel(r'$\lambda_{\mathrm{DPO}}$', fontproperties=_font(27))
    ax.set_ylabel(r'SHR', fontproperties=_font(26))
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontproperties=_font(26))
    ax.tick_params(axis='y', labelsize=25)

    ax.set_ylim(config["bar_ylim"])
    ax.yaxis.set_major_locator(MultipleLocator(base=config["bar_locator"]))
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)

    fig.tight_layout(pad=0.1)
    safe_name = model_name.replace(" ", "_")
    fig.savefig(os.path.join(out_dir, f"{safe_name}_lambda_bar.png"),
                dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(out_dir, f"{safe_name}_lambda_bar.pdf"),
                dpi=300, bbox_inches='tight')
    plt.close(fig)


def main():
    out_dir = "plots_all"
    os.makedirs(out_dir, exist_ok=True)

    for model_name, config in MODELS_CONFIG.items():
        plot_line_chart(model_name, config, out_dir)
        plot_bar_chart(model_name, config, out_dir)

    print(f"All done! Files saved to ./{out_dir}")


if __name__ == "__main__":
    main()
