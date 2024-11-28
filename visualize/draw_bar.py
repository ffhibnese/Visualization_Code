
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



legend_font = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=16)
legend_font2 = font_manager.FontProperties(fname="//data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=18)
legend_font3 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)
legend_font4 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=24)
legend_font_x_tick = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=23)
legend_font5 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)

colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]


dataset_label = ['ImageNet', 'MS-COCO', 'Comics']
scale_label = ['0.5', '0.75', '0.9', '1.2', '1.4', '1.6']

# cgsp = [48.04, 36.09, 20.02]
# cgnc = [63.75, 41.63, 37.70]

cgsp = [45.9, 31.67, 10.36]
cgnc = [63.36, 42.71, 22.61]

# GGL = [13.38850298, 15.133514404296875]
# GIAS = [17.49231453, 20.179915973118373]
# GILO = [20.05337984, 21.33953969]

if __name__ == '__main__':
    # fig = plt.figure()
    # ax1 = fig.add_axes([0.1, 0.0, 0.8, 0.8])
    # plt.xlabel('Birghtness', fontproperties=legend_font2)
    plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font4)
    plt.xlabel('Source dataset', fontproperties=legend_font4, color='black')
    x = np.array([4, 10, 16])
    
    plt.grid(zorder=0, alpha=0.3)
    plt.xticks(x, dataset_label, font=legend_font_x_tick)
    plt.yticks(list(range(10, 70, 10)), font=legend_font4)
    plt.ylim(ymin = 8, ymax=67)
    plt.xlim(xmin = 0, xmax=19)

    total_width, n = 3, 2
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, cgsp, width=width, label='C-GSP', color='green', alpha=1, zorder=10)
    plt.bar(x + width, cgnc, width=width, label="CGNC", color='orange', alpha=1, zorder=10)
    # plt.bar(x + 2 * width, GGL, width=width, label="GGL(Li et al.)", color='pink', alpha=1,hatch='\\\\', zorder=10)
    # plt.bar(x + 3 * width, GIAS, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    # plt.bar(x + 4 * width, GILO, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)


    # plt.legend(loc='upper left', ncol=2, fontsize=24, bbox_to_anchor=(0.48,1.45), prop=legend_font)
    plt.legend(loc='upper right', ncol=2,  prop=legend_font)
    
    # ax2 = fig.add_axes([1.13, 0.0, 0.8, 0.8])


    plt.savefig('./imgs/bar_cross_domain.png', dpi=400, bbox_inches='tight')

    plt.show()