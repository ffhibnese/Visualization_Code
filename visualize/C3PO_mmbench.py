import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.ticker import MultipleLocator

plt.rcParams["font.family"] = "Times New Roman"

plt.rcParams['mathtext.fontset'] = 'stix'

methods = ["vanilla", "RLAIF-V", "OPA-DPO", "C3PO"]
mmbench_data = [84.36, 84.71, 84.54, 84.45]
palette = {"vanilla": "#F4A7B9", "RLAIF-V": "#8ABDD9", "OPA-DPO": "#F7C97E", "C3PO": "#F7887F"}
colors = [palette[m] for m in methods]

def _font(size: int) -> font_manager.FontProperties:
    return font_manager.FontProperties(family="Times New Roman", size=size)

def main():
    fig, ax = plt.subplots(figsize=(9.2, 5.4))
    fig.patch.set_facecolor((1, 1, 1))
    ax.set_facecolor((247/255, 247/255, 247/255))
    x = np.arange(len(methods))
    bar_width = 0.6

    bars = ax.bar(x, mmbench_data, width=bar_width, color=colors, 
                  edgecolor="black", linewidth=2.0, alpha=0.9)

    for bar in bars:
        pass

    ax.set_ylabel("MMBench Score", fontproperties=_font(31))
    ax.set_xticks(x)
    xticks = ax.set_xticklabels(methods, fontproperties=_font(31))
    xticks[0].set_fontproperties(_font(32))
    ax.tick_params(axis='y', labelsize=31)
    ax.yaxis.set_major_locator(MultipleLocator(base=1))
    
    ax.set_ylim(80.0, 85.6) 

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(2.0)

    ax.set_axisbelow(True)
    ax.grid(True, axis='y', linestyle='--', alpha=0.5, linewidth=0.9, zorder=0)
    ax.grid(True, axis='x', linestyle='-', alpha=0.2, linewidth=0.8, zorder=0) 
    ax.margins(x=0.08)

    fig.tight_layout(pad=0.1)
    
    out_dir = "bench_plots"
    os.makedirs(out_dir, exist_ok=True)

    fig.savefig(os.path.join(out_dir, "mmbench_bar.png"), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(out_dir, "mmbench_bar.pdf"), dpi=300, bbox_inches='tight')
    plt.close(fig)

if __name__ == "__main__":
    main()