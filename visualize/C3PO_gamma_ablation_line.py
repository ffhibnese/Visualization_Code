import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.ticker import MultipleLocator

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'

ratios = ["0.8", "0.85", "0.9", "0.95", "1.0"]
chairs = [37.7, 39.3, 35.3, 35.3, 41.7] 
chairi = [7.7, 7.5, 6.9, 7.0, 8.3]   

palette = {
    "CHAIRs": "#4987CA",  
    "CHAIRi": "#635AC2",  
}

def _font(size: int) -> font_manager.FontProperties:
    return font_manager.FontProperties(family="Times New Roman", size=size)

def main():
    out_dir = "bench_plots"
    os.makedirs(out_dir, exist_ok=True)

    fig, ax1 = plt.subplots(figsize=(5.9, 4.35))
    fig.patch.set_facecolor((1, 1, 1))
    ax1.set_facecolor((247/255, 247/255, 247/255))
    x = np.arange(len(ratios))

    color1 = palette["CHAIRs"]
    lns1 = ax1.plot(x, chairs, marker='o', markersize=8, color=color1, 
                    linewidth=2.8, label=r'CHAIR$_S$ ($\downarrow$)', markeredgecolor='white', zorder=5)
    ax1.set_xlabel(r'Compression Ratio ($\gamma$)', fontproperties=_font(27), labelpad=10)
    
    ax1.set_ylabel(r'CHAIR$_S$', fontproperties=_font(26))
    ax1.tick_params(axis='y', labelsize=25)
    ax1.yaxis.set_major_locator(MultipleLocator(base=3))
    
    ax1.set_ylim(27, 43.5) 
    

    ax2 = ax1.twinx()
    ax2.set_facecolor((247/255, 247/255, 247/255))
    color2 = palette["CHAIRi"]
    lns2 = ax2.plot(x, chairi, marker='s', markersize=8, color=color2, 
                    linewidth=2.8, label=r'CHAIR$_I$ ($\downarrow$)', markeredgecolor='white', zorder=5)

    ax2.set_ylabel(r'CHAIR$_I$', fontproperties=_font(26))
    ax2.tick_params(axis='y', labelsize=25)
    ax2.yaxis.set_major_locator(MultipleLocator(base=1))

    ax2.set_ylim(6.0, 10.5) 
    
    ax1.set_xticks(x)
    ax1.set_xticklabels(ratios, fontproperties=_font(25))
    ax1.set_axisbelow(True)
    ax2.set_axisbelow(True)
    ax1.grid(True, axis='y', linestyle='--', alpha=0.5, linewidth=0.9, zorder=0)

    ax1.spines["top"].set_visible(True)
    ax2.spines["top"].set_visible(True)

    for spine in ax1.spines.values():
        spine.set_linewidth(1.3)
    for spine in ax2.spines.values():
        spine.set_linewidth(1.3)

    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc='upper center', bbox_to_anchor=(0.5, 1.24), 
               ncol=2, frameon=False, prop=_font(18))

    fig.tight_layout(pad=0.1)

    out_png = os.path.join(out_dir, "gamma_ablation_line.png")
    out_pdf = os.path.join(out_dir, "gamma_ablation_line.pdf")
    fig.savefig(out_png, dpi=300, bbox_inches='tight')
    fig.savefig(out_pdf, dpi=300, bbox_inches='tight')
    plt.close(fig)

if __name__ == "__main__":
    main()