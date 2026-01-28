#  r"w/o $\mathcal{L}_\mathrm{CE}$"
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as font_manager
from matplotlib.patches import Rectangle

legend_font = font_manager.FontProperties(fname="Times/times.ttf",
                                          weight='normal', style='normal', size=16)
legend_font2 = font_manager.FontProperties(fname="Times/times.ttf",
                                           weight='semibold', style='normal', size=20)
legend_font3 = font_manager.FontProperties(fname="Times/times.ttf",
                                           weight='semibold', style='normal', size=24)
legend_font4 = font_manager.FontProperties(fname="Times/times.ttf",
                                           weight='normal', style='normal', size=18)

# 数据
categories = ["GSM8K", "MMLU"]
x = np.arange(len(categories))
width = 0.16

origin = [80.89462, 73.84988]
CE = [79.83321, 72.83863]
no_CE = [20.31842, 8.382]

# colors = {
#     "Origin": (193/255, 223/255, 175/255),
#     "CE": (247/255, 205/255, 138/255),
#     "no_CE": (244/255, 175/255, 191/255),
# }

colors = {
    "Origin": (135/255, 189/255, 217/255),
    "CE": (244/255, 167/255, 185/255),
    "no_CE": (247/255, 201/255, 126/255),
}

# 画布
fig, ax = plt.subplots(figsize=(8, 5))

# 柱子
ax.bar(x - width, origin, width, label="Origin", color=colors["Origin"], edgecolor="black", linewidth=0.8)
ax.bar(x, CE, width, label=r"w $\mathcal{L}_\mathrm{CE}$", color=colors["CE"], edgecolor="black", linewidth=0.8)
ax.bar(x + width, no_CE, width, label=r"w/o $\mathcal{L}_\mathrm{CE}$", color=colors["no_CE"], edgecolor="black", linewidth=0.8)

# x 轴
ax.set_xlim(-0.6, len(categories) - 0.4)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontproperties=legend_font2)

# y 轴
ax.set_ylim(0, 85)
ax.set_ylabel("Accuracy (%)", fontproperties=legend_font2)
ax.set_yticks(np.arange(0, 91, 15))
ax.set_yticklabels(np.arange(0, 91, 15), fontproperties=legend_font4)

# 网格（论文常见）
ax.grid(axis="y", linestyle="--", alpha=0.4)
ax.set_axisbelow(True)

# 图例（顶部居中）
ax.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, 1.15),
    ncol=3,
    frameon=True,
    prop=legend_font,
)

plt.tight_layout()
plt.savefig('./pic/CE_ablation.pdf', dpi=150, bbox_inches='tight')
plt.show()
