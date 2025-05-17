import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

from scipy.stats import norm
import matplotlib.ticker as mtick
from scipy.interpolate import interp1d
import os


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.sans-serif'] = ['Times New Roman']

legend_font = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
# legend_font2 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=24)
legend_font2 = font_manager.FontProperties(weight='normal', style='normal', size=23)
legend_font3 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=25)
# legend_font4 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=19)
legend_font5 = font_manager.FontProperties(weight='normal', style='normal', size=19)
legend_font6 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=23)
label_fontdict = {'fontsize': 28}
# 假设你已有 DataFrame 格式数据
# df = pd.read_csv('your_data.csv')
# 示例造数据
# np.random.seed(0)
# layers = list(range(0, 33, 4))
# data = {'stop_layer': [], 'chair_score': []}
# for l in layers:
#     data['stop_layer'].extend([l]*20)
#     data['chair_score'].extend(np.random.normal(loc=5.8 + 0.1*np.sin(l/4), scale=0.3, size=20))

# df = pd.DataFrame(data)
df = pd.read_excel('/mnt/data/fanghao/Visualization_Code/visualize/token_time.xlsx')
print(df)
method_nums = list(set(df['Method'].tolist()))
print(len(method_nums))

# 创建三个子图，分别显示 [0~20]、[20~50]、[50~60] 区间
fig, (ax_top, ax_middle, ax_bottom) = plt.subplots(
    3, 1, sharex=True, figsize=(9, 6),
    gridspec_kw={'height_ratios': [1, 1, 2]}
)

# Y轴分界范围
low_ylim = (3, 16.8)
mid_ylim = (20, 50)
high_ylim = (50, 280)

# 画图
sns.boxplot(data=df, x='Method', y='Time', ax=ax_top, palette='pastel', showfliers=False)
sns.boxplot(data=df, x='Method', y='Time', ax=ax_middle, palette='pastel', showfliers=False)
sns.boxplot(data=df, x='Method', y='Time', ax=ax_bottom, palette='pastel', showfliers=False)



# 设置每个子图的y轴范围
ax_bottom.set_ylim(*low_ylim)
ax_bottom.set_yticks([5, 7.5, 10, 12.5, 15],[ '5', '7.5', '10', '12.5', '15'], font=legend_font5)
ax_middle.set_ylim(*mid_ylim)
ax_middle.set_yticks(np.linspace(20, 50, 4),['20', '30', '40', '50'], font=legend_font5)
ax_top.set_ylim(*high_ylim)
ax_top.set_yticks([100, 200],['100', '200'], font=legend_font5)
# 去掉框线
for ax in [ax_bottom, ax_middle, ax_top]:
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

# 恢复底部和顶部显示
ax_bottom.spines['bottom'].set_visible(True)
ax_top.spines['top'].set_visible(True)


# 添加断裂符号
d = 0.01  # 断裂标记大小

# bottom <-> middle
kwargs = dict(color='k', clip_on=False, transform=ax_middle.transAxes)
ax_middle.plot((-d, +d), (-d, + d), **kwargs)  # 左
ax_middle.plot((1 - d, 1 + d), (- d, + d), **kwargs)  # 右

kwargs = dict(color='k', clip_on=False, transform=ax_bottom.transAxes)
ax_bottom.plot((-d, +d), (1-d, 1+d), **kwargs)
ax_bottom.plot((1 - d, 1 + d), (1-d,1 +d), **kwargs)

# middle <-> top
kwargs = dict(color='k', clip_on=False, transform=ax_top.transAxes)
ax_top.plot((-d, +d), (-d, +d), **kwargs)
ax_top.plot((1 - d, 1 + d), (-d, +d), **kwargs)

kwargs = dict(color='k', clip_on=False, transform=ax_middle.transAxes)
ax_middle.plot((-d, +d), (1 - d, 1 + d), **kwargs)
ax_middle.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

# 添加红线
# for ax in [ax_bottom, ax_middle, ax_top]:
#     ax.axhline(y=6, color='red', linestyle='--', linewidth=1)
ax_top.set_ylabel('')
ax_middle.set_ylabel('')
ax_bottom.set_ylabel('')
# 标签设置
ax_bottom.set_xlabel("Method", fontsize=12)
# ax_middle.set_ylabel("Generation Time per Sample (s)", fontsize=12)

base_mean = df["Time"].mean()
# for ax in [ax_top, ax_bottom]:
#     ax.axhline(y=6, color='red', linestyle='--')
ax_middle.axhline(base_mean, ls='--', color='red', label='Average Time of \ndifferent methods')
# ax_middle.legend(['Average Time of various methods'], loc='upper left')
handles, labels = ax_middle.get_legend_handles_labels()
# 添加到图上
ax_top.legend(handles, labels, loc='upper left', fontsize=19)

method_label = ['ICD', 'VCD', 'SID', 'OPERA', 'HALC', 'CMI-VLD']
# 图形美化
plt.xticks(ticks=range(len(method_nums)), labels=method_label, font=legend_font4)
# plt.yticks(np.array(np.linspace(0, 30, 7)), font=legend_font4)
# plt.ylim(3, 300)

ax_top.tick_params(labelbottom=False, bottom=False)
ax_middle.tick_params(labelbottom=False, bottom=False)

fig.supylabel("  Generaion Time per Sample (s)", fontproperties=legend_font2)
plt.xlabel("Method", fontproperties=legend_font2)
# plt.legend(loc="lower right", fontsize=12)
plt.tight_layout()
plt.savefig('../imgs/CMI_VLD_decoding_efficiency.pdf')
