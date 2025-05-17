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
legend_font2 = font_manager.FontProperties(weight='normal', style='normal', size=17)
legend_font3 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=25)
# legend_font4 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=14)
legend_font5 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
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

fig, (ax_top, ax_bottom) = plt.subplots(3, 1, sharex=True, figsize=(8, 6),
                                        gridspec_kw={'height_ratios': [1, 2]})
break_point = 20
upper_ylim = 200
lower_ylim = 1, 18

sns.boxplot(data=df, x='Method', y='Time', ax=ax_top, palette='pastel', showfliers=False)
sns.boxplot(data=df, x='Method', y='Time', ax=ax_bottom, palette='pastel', showfliers=False)

# 设置 y 轴范围
ax_top.set_ylim(break_point, upper_ylim)
ax_bottom.set_ylim(*lower_ylim)

# 去掉断开区域的框线
ax_top.spines['bottom'].set_visible(False)
ax_bottom.spines['top'].set_visible(False)
ax_top.tick_params(labelbottom=False)  # 不显示上图的x刻度
ax_bottom.tick_params(labeltop=False)

d = .015  # 断裂斜线大小
kwargs = dict(transform=ax_top.transAxes, color='k', clip_on=False)
ax_top.plot((-d, +d), (-d, +d), **kwargs)        # 左
ax_top.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # 右

kwargs.update(transform=ax_bottom.transAxes)  # switch to the bottom axes
ax_bottom.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # 左
ax_bottom.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # 右


# 绘图
# plt.figure(figsize=(8, 6))
# palette = sns.color_palette("Spectral", len(method_nums))
# ax = sns.boxplot(x="Method", y="Time", data=df, palette=palette, width=0.6, showfliers=False)
# ax_top.set_ylabel('Generation Time per Sample (s)', fontproperties=legend_font2)
# ax_bottom.set_ylabel('Generation Time per Sample (s)', fontproperties=legend_font2)

# 红色虚线 + 数值
base_mean = df["Time"].mean()
# for ax in [ax_top, ax_bottom]:
#     ax.axhline(y=6, color='red', linestyle='--')
# ax_top.legend(['Average Time of various methods'], loc='upper right')
plt.axhline(base_mean, ls='--', color='red', label='Average Time of various methods')
# plt.text(-0.5, base_mean + 0.02, f"{base_mean:.2f}", color='red')

method_label = ['ICD', 'VCD', 'SID', 'OPERA', 'HALC', 'VASparse', 'CMI-VLD']
# 图形美化
# plt.xticks(ticks=range(len(method_nums)), labels=method_label, font=legend_font4)
# plt.yticks(np.array(np.linspace(0, 30, 7)), font=legend_font4)
# plt.ylim(3, 300)

plt.ylabel("Generaion Time per Sample (s)", fontproperties=legend_font2)
plt.xlabel("Method", fontproperties=legend_font2)
plt.legend(loc="lower right", fontsize=15)
plt.tight_layout()
plt.savefig('../imgs/CMI_VLD_decoding_efficiency')
