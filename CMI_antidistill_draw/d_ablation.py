import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager

# ---------- 字体照搬 ----------
legend_font = font_manager.FontProperties(fname="Times/times.ttf",
                                          weight='normal', style='normal', size=16)
legend_font2 = font_manager.FontProperties(fname="Times/times.ttf",
                                           weight='semibold', style='normal', size=20)
legend_font3 = font_manager.FontProperties(fname="Times/times.ttf",
                                           weight='semibold', style='normal', size=24)
legend_font4 = font_manager.FontProperties(fname="Times/times.ttf",
                                           weight='normal', style='normal', size=18)

# ---------- 数据 ----------
_3B_ori = [72.93404, 73.46475, 71.64519, 70.28052, 70.96285]
_1_5B_ori = [60.57619, 60.19712, 58.52919, 60.42456, 59.74223]
_0_5B_ori = [37.45262, 36.69447, 35.93632, 36.08795, 34.3442]
teacher = [81.57695224, 80.13646702, 79.83321, 79.22668688, 76.95223654] 
d = [0, 0.5, 1, 1.5, 2]

fig, (ax_top, ax_mid, ax_bottom, ax_teacher) = plt.subplots(
    4, 1, sharex=True, figsize=(5, 6),
    gridspec_kw={'height_ratios': [6, 5, 6, 8]}   # 28:15 精确比例
)
# ---------- 绘图 ----------
dot_size = 8
line_width = 2.5
for ax in (ax_top, ax_mid, ax_bottom):
    ax.plot(d, _3B_ori, 'o-', markersize=dot_size, color=(244/255, 175/255, 191/255),
            linewidth=line_width, alpha=1, label='3B')
    ax.plot(d, _1_5B_ori, 'o-', markersize=dot_size, color=(247/255, 205/255, 138/255),
            linewidth=line_width, alpha=1, label='1.5B')
    ax.plot(d, _0_5B_ori, 'o-', markersize=dot_size, color=(193/255, 223/255, 175/255),
            linewidth=line_width, alpha=1, label='0.5B')

ax_teacher.bar(d, teacher, width=0.2,        # 柱宽按需调
               color=(149/255, 194/255, 220/255), alpha=1,
               label='Teacher')
ax_teacher.legend(prop=legend_font) 
# ax_teacher.legend(prop=legend_font,
#                   loc='upper center',    # 子图内部上方
#                   bbox_to_anchor=(0.5, 1.15),  # 再往上抬 15 %
#                   frameon=True)

# ---------- 断裂轴范围 ----------
# ---------- 1. 断裂范围 & 刻度 ----------
# 上段 55-83，下段 34-38，刻度密度人为设成「每 2 单位」一样密
ax_top.set_ylim(69.8, 74.2)
ax_mid.set_ylim(58.2, 61.5)
ax_bottom.set_ylim(33.8, 38.2)
ax_teacher.set_ylim(76, 82)

ax_top.set_yticks([71, 73])   # 57 59 61 ... 83
ax_mid.set_yticks([59, 61])
ax_bottom.set_yticks([35, 37])  # 34 36 38
ax_teacher.set_yticks([77, 79, 81])

ax_top.set_yticklabels([71, 73], fontproperties=legend_font4)
ax_mid.set_yticklabels([59, 61], fontproperties=legend_font4)
ax_bottom.set_yticklabels([35, 37], fontproperties=legend_font4)
ax_teacher.set_yticklabels([77, 79, 81], fontproperties=legend_font4)


# ---------- 3. 整张图统一 y 标签 ----------
fig.supylabel('Accuracy (%)', fontproperties=legend_font2, color='black', x=0.02, y=0.6)

# ---------- 标签 ----------
ax_teacher.set_xlabel(r'$\lambda$', fontproperties=legend_font3, color='black')

# 刻度字体
for tick in ax_bottom.get_xticklabels() + ax_bottom.get_yticklabels():
    tick.set_fontproperties(legend_font4)
for tick in ax_mid.get_yticklabels():
    tick.set_fontproperties(legend_font4)
for tick in ax_top.get_yticklabels():
    tick.set_fontproperties(legend_font4)
for tick in ax_teacher.get_xticklabels() + ax_teacher.get_yticklabels():
    tick.set_fontproperties(legend_font4)    

handles, labels = ax_bottom.get_legend_handles_labels()

fig.legend(
    handles, labels,
    loc='upper center',
    ncol=3,                     # 一行放几个（你有 6 条线，3 或 6 都行）
    frameon=True,
    prop=legend_font,
    bbox_to_anchor=(0.55, 1.08)  # 整体往上抬
)

# 网格 & 去边框
ax_teacher.grid(alpha=0.3)
ax_bottom.grid(alpha=0.3)
ax_mid.grid(alpha=0.3)
ax_top.grid(alpha=0.3)
ax_top.spines['bottom'].set_visible(False)
ax_bottom.spines['top'].set_visible(False)
ax_mid.spines['top'].set_visible(False)
ax_mid.spines['bottom'].set_visible(False)
# ax_top.spines['right'].set_visible(False)

# 断斜线
d = 0.015
# ========== ax_top 底部断点（2 条） ==========
kwargs = dict(transform=ax_top.transAxes, color='k', clip_on=False)
ax_top.plot((-d, +d), (-d, +d), **kwargs)              # 左
ax_top.plot((1 - d, 1 + d), (-d, +d), **kwargs)        # 右

# ========== ax_mid 顶部断点（2 条） ==========
kwargs = dict(transform=ax_mid.transAxes, color='k', clip_on=False)
ax_mid.plot((-d, +d), (1 - d, 1 + d), **kwargs)        # 左
ax_mid.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # 右

# ========== ax_mid 底部断点（2 条） ==========
ax_mid.plot((-d, +d), (-d, +d), **kwargs)              # 左
ax_mid.plot((1 - d, 1 + d), (-d, +d), **kwargs)        # 右

# ========== ax_bottom 顶部断点（2 条） ==========
kwargs = dict(transform=ax_bottom.transAxes, color='k', clip_on=False)
ax_bottom.plot((-d, +d), (1 - d, 1 + d), **kwargs)     # 左
ax_bottom.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # 右
# ---------- 保存 ----------
plt.tight_layout()

plt.savefig('./pic/d_ablation.pdf', dpi=400, bbox_inches='tight')
plt.show()