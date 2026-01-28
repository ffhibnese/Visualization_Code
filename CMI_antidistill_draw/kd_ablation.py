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
categories = [0.0, 0.3, 0.5, 0.7, 1.0]
x = np.arange(len(categories))
width = 0.35

origin = [58.83245, 59.96967, 62.47157, 61.6376, 58.98408]
ours = [58.83245, 44.4276, 54.28355, 54.58681, 53.75284]

# colors = {
#     "Origin": (193/255, 223/255, 175/255),
#     "CE": (247/255, 205/255, 138/255),
#     "no_CE": (244/255, 175/255, 191/255),
# }

colors = {
    "origin": (135/255, 189/255, 217/255),
    "ours": (244/255, 167/255, 185/255),
    "no_CE": (247/255, 201/255, 126/255),
}

# 画布
fig, ax = plt.subplots(figsize=(8, 5))

# 柱子
ax.bar(x - width/2, origin, width, label="vallina / ABKD", color=colors["origin"], edgecolor="black", linewidth=0.8)
ax.bar(x + width/2, ours, width, label="Ours / ABKD", color=colors["ours"], edgecolor="black", linewidth=0.8)
# ax.bar(x + width, no_CE, width, label=r"w/o $\mathcal{L}_\mathrm{CE}$", color=colors["no_CE"], edgecolor="black", linewidth=0.8)

# x 轴
ax.set_xticks(x)
ax.set_xticklabels(categories, fontproperties=legend_font2)

# y 轴
ax.set_ylim(30, 70)
ax.set_ylabel("Accuracy (%)", fontproperties=legend_font2)
ax.set_xlabel(r'$\alpha$', fontproperties=legend_font2)
ax.set_yticks(np.arange(30, 72, 10))
ax.set_yticklabels(np.arange(30, 72, 10), fontproperties=legend_font4)

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
plt.savefig('./pic/kd_ablation.pdf', dpi=150, bbox_inches='tight')
plt.show()
