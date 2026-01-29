import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.ticker import MultipleLocator

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'

ratios = ["0.8", "0.85", "0.9", "0.95", "1.0"]
shr_values = [0.283, 0.281, 0.263, 0.298, 0.306]
shr_pct = [v * 100 for v in shr_values]
bar_color = "#A6D1A3" 

def _font(size: int) -> font_manager.FontProperties:
    return font_manager.FontProperties(family="Times New Roman", size=size)

def main():
    fig, ax = plt.subplots(figsize=(5.9, 3.9))
    fig.patch.set_facecolor((1, 1, 1))
    ax.set_facecolor((247/255, 247/255, 247/255))
    x = np.arange(len(ratios))
    bar_width = 0.60

    bars = ax.bar(x, shr_pct, width=bar_width, color=bar_color, 
                  edgecolor="black", linewidth=1.3, alpha=0.9)


    ax.set_xlabel(r'Compression Ratio ($\gamma$)', fontproperties=_font(27), labelpad=10)
    ax.set_ylabel(r'SHR', fontproperties=_font(26))
    ax.set_xticks(x)
    ax.set_xticklabels(ratios, fontproperties=_font(26))
    ax.tick_params(axis='y', labelsize=25)
    ax.yaxis.set_major_locator(MultipleLocator(base=1))

    ax.set_ylim(25, 31.4) 

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(1.3)

    ax.set_axisbelow(True)
    ax.grid(True, axis='y', linestyle='--', alpha=0.5, linewidth=0.9, zorder=0)
    ax.grid(True, axis='x', linestyle='-', alpha=0.2, linewidth=0.8, zorder=0) 

    fig.tight_layout(pad=0.1)
    
    out_dir = "bench_plots"
    os.makedirs(out_dir, exist_ok=True)

    fig.savefig(os.path.join(out_dir, "gamma_ablation_shr_bar.png"), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(out_dir, "gamma_ablation_shr_bar.pdf"), dpi=300, bbox_inches='tight')
    plt.close(fig)

if __name__ == "__main__":
    main()