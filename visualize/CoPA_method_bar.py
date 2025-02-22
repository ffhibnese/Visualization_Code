
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
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


# legend_font = font_manager.FontProperties(fname="Times/times.ttf", weight='normal', style='normal', size=18)
# legend_font2 = font_manager.FontProperties(fname="Times/times.ttf", weight='normal', style='normal', size=18)
# legend_font3 = font_manager.FontProperties(fname="Times/timesbd.ttf", weight='semibold', style='normal', size=25)
# legend_font4 = font_manager.FontProperties(fname="Times/times.ttf", weight='normal', style='normal', size=18)
# legend_font5 = font_manager.FontProperties(fname="Times/times.ttf", weight='normal', style='normal', size=20)
# legend_font6 = font_manager.FontProperties(fname="Times/timesbd.ttf", weight='semibold', style='normal', size=23)

legend_font = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=26)
# legend_font2 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=24)
legend_font2 = font_manager.FontProperties(weight='normal', style='normal', size=34)
legend_font3 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=25)
# legend_font4 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=36)
legend_font5 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=23)
legend_font6 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=23)
label_fontdict = {'fontsize': 28}
colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]

legend_x_tick = ['Prompt 1', 'Prompt 2', 'Prompt 3', 'Prompt 4']
scale_label = ['0.5', '0.75', '0.9', '1.2', '1.4', '1.6']

# cgsp = [48.04, 36.09, 20.02]
# cgnc = [63.75, 41.63, 37.70]

# llm_likehood = [ 0.6095, 0.6235, 0.7937, 0.9563]
# tpr = [24.33, 21.33, 23, 17]

llm_likehood = [0.9563, 0.7937, 0.6095, 0.6235]
tpr = [17, 21.33, 23, 24.33]

# llm_likehood.reverse()
# tpr.reverse()

# GGL = [13.38850298, 15.133514404296875]
# GIAS = [17.49231453, 20.179915973118373]
# GILO = [20.05337984, 21.33953969]

if __name__ == '__main__':
    # fig = plt.figure()
    # ax1 = fig.add_axes([0.1, 0.0, 0.8, 0.8])
    # plt.xlabel('Birghtness', fontproperties=legend_font2)
    fig = plt.figure(figsize=(16,9))
    ax1 = fig.add_axes([0.0, 0.0, 1, 0.99])
    x = np.array([4, 10, 16, 22])
    plt.ylabel('LLM likelihood', fontproperties=legend_font2)
    plt.grid(zorder=0, alpha=0.3)
    plt.xticks(x, legend_x_tick, font=legend_font4)
    y = np.array((range(50, 100, 5))) /100
    plt.yticks(y, y, font=legend_font4)
    plt.ylim(ymin = 0.58, ymax=0.965)
    plt.xlim(xmin = 0.48, xmax=24.4)

    total_width, n = 3.2, 2
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, llm_likehood, width=width, label='LLM likelihood of machine distributions', color='cornflowerblue', alpha=1, zorder=10)
    ax1_sub = ax1.twinx()  # 创建共享 x 轴的新 y 轴
    # 绘制第二条曲线
    # ax1_sub.plot(x, y2, 'r-', label='cos(x)')
    # ax1_sub.set_ylabel('cos(x)', color='r')   
    ax1_sub.bar(x + width, tpr, width=width, label='TPR of contrastive distributions', color='mediumaquamarine', alpha=1, zorder=10)
    # .plot(x, knn_fid, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=alpha_4, label='FID')
    ax1_sub.set_ylim(ymin = 15.8, ymax=25.2)
    ax1_sub.set_ylabel('TPR@FPR=5% (%)', fontproperties=legend_font2)
    # plt.legend((p1, p2, p3, p4, p5), ('IG (Geiping et al.)', 'GI (Yin et al.)', 'GGL (Li et al.)', 'GIAS (Jeon et al.)', 'GIFD'), ncol=1, prop=legend_font, loc='best')
    y = np.array(list(range(16, 26, 1)))
    ax1_sub.set_yticks(y, y, font=legend_font4)
    # plt.bar(x + 2 * width, GGL, width=width, label="GGL(Li et al.)", color='pink', alpha=1,hatch='\\\\', zorder=10)
    # plt.bar(x + 3 * width, GIAS, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    # plt.bar(x + 4 * width, GILO, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)


    # plt.legend(loc='upper left', ncol=2, fontsize=24, bbox_to_anchor=(0.48,1.45), prop=legend_font)
    fig.legend(loc='upper center', ncol=1, bbox_to_anchor=(0.52, 0.99), prop={'size':32})
    
    # ax2 = fig.add_axes([1.13, 0.0, 0.8, 0.8])
    plt.savefig('/mnt/bn/intern-disk/mlx/users/fanghao.34/Visualization_Code/imgs/CoPA_reduce_by_maglify.pdf', dpi=400, bbox_inches='tight')

    plt.show()