import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager

# ---------- 字体照搬 ----------
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.sans-serif'] = ['Times New Roman']

legend_font = font_manager.FontProperties(
    fname="Times/times.ttf", weight='normal', style='normal', size=16)
legend_font2 = font_manager.FontProperties(
    fname="Times/times.ttf", weight='semibold', style='normal', size=20)
legend_font3 = font_manager.FontProperties(fname="Times/times.ttf",
                                           weight='semibold', style='normal', size=22)
legend_font4 = font_manager.FontProperties(
    fname="Times/times.ttf", weight='normal', style='normal', size=28)

# ---------- 数据路径 ----------
filename1 = "./lall.json"
name1 = "loss_all"
filename2 = "./lgrad.json"
name2 = "loss_grad"

# ---------- 读数据 ----------
df1 = pd.read_json(filename1)
df1.columns = ['time', 'step', name1]

df2 = pd.read_json(filename2)
df2.columns = ['time', 'step', 'loss']
df2[name2] = -df2['loss']          # 负号需求保留

# ---------- 画布 ----------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.75, 6.5))

# ---------- 绘图（照搬风格） ----------
dot_size = 2  # 8
line_width = 1.5  # 2.5
# 'lightskyblue'   (166/255, 202/255, 236/255) (149/255, 194/255, 220/255)
ax1.plot(df1['step'], df1[name1],
         color=(166/255, 202/255, 236/255),
         markersize=dot_size, linewidth=line_width, alpha=1)
ax2.plot(df2['step'], df2[name2],
         color=(166/255, 202/255, 236/255),
         markersize=dot_size, linewidth=line_width, alpha=1)

from matplotlib.ticker import MaxNLocator, MultipleLocator

# 1. 限定「最多 N 个刻度」
ax1.yaxis.set_major_locator(MaxNLocator(5))   # 上下段都≤5 根
ax2.yaxis.set_major_locator(MaxNLocator(5))

# 2. 或者固定步长（例如每 5 单位一根）
# ax1.yaxis.set_major_locator(MultipleLocator(5))
# ax2.yaxis.set_major_locator(MultipleLocator(5))

# ---------- 坐标轴标签 ----------
ax1.set_xlabel('Training Step', fontproperties=legend_font2, color='black')
# ax1.set_ylabel(r'Loss $\mathcal{L}_\mathcal{M}$', fontproperties=legend_font2, color='black')
ax2.set_xlabel('Training Step', fontproperties=legend_font2, color='black')
# ax2.set_ylabel(r'Loss $\mathcal{L}_{grad}$', fontproperties=legend_font2, color='black')
# 统一宽度：上半段补 1 个 figure-space，下半段补 2 个（负号+小数位）
ax1.set_ylabel(r'Loss $\mathcal{L}_\mathcal{M}$',
               fontproperties=legend_font2, color='black')
ax2.set_ylabel(r'Loss $\mathcal{L}_{\text{grad}}$',
               fontproperties=legend_font2, color='black')

# 再让轴标签区域本身对齐（可选，更保险）
fig.align_ylabels([ax1, ax2])      # 放在 savefig 之前
# for ax in (ax1, ax2):
#     ax.yaxis.set_label_coords(-0.1, 0.5)  # 横坐标固定，纵坐标居中
#     ax.yaxis.label.set_ha('right')         # 文字本身右对齐

# ---------- 刻度字体 ----------
for tick in ax1.get_xticklabels() + ax1.get_yticklabels():
    tick.set_fontproperties(legend_font2)
for tick in ax2.get_xticklabels() + ax2.get_yticklabels():
    tick.set_fontproperties(legend_font2)

# ---------- 网格 + 去边框 ----------
ax1.grid(alpha=0.5)
ax2.grid(alpha=0.5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# ---------- 保存 ----------
plt.tight_layout()
plt.savefig('./pic/loss_pro.pdf',
            dpi=150, bbox_inches='tight')
plt.show()