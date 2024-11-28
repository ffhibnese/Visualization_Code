
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

plt.rcParams['font.sans-serif'] = ['Times New Roman']


# legend_font = font_manager.FontProperties(fname="Times/times.ttf", weight='normal', style='normal', size=18)
# legend_font2 = font_manager.FontProperties(fname="Times/times.ttf", weight='normal', style='normal', size=18)
# legend_font3 = font_manager.FontProperties(fname="Times/timesbd.ttf", weight='semibold', style='normal', size=25)
# legend_font4 = font_manager.FontProperties(fname="Times/times.ttf", weight='normal', style='normal', size=18)
# legend_font5 = font_manager.FontProperties(fname="Times/times.ttf", weight='normal', style='normal', size=20)
# legend_font6 = font_manager.FontProperties(fname="Times/timesbd.ttf", weight='semibold', style='normal', size=23)

# legend_font = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=18)
# # legend_font2 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=24)
# legend_font2 = font_manager.FontProperties(weight='normal', style='normal', size=27)
# legend_font3 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=25)
# # legend_font4 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
# legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=28)
# legend_font5 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
# legend_font6 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=23)
legend_font = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=18)
# legend_font2 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=24)
legend_font2 = font_manager.FontProperties(weight='normal', style='normal', size=24)
legend_font3 = font_manager.FontProperties(weight='normal', style='normal', size=22)
#legend_font3 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=25)
# legend_font4 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=28)
legend_font5 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=23)

label_fontdict = {'fontsize': 28}

# dataset_label = ['Average(ImageNet)', 'Average(FFHQ)']
# class_id = ['62', '715', '150']
method = ['Gaussian', 'Medium', 'Average']


TTP = [52.2, 45.9, 44.2]
DGTA_PI = [55, 50, 47]
CGNC = [58.08, 61.56, 56.34]


if __name__ == '__main__':
    # fig = plt.figure()
    # ax1 = fig.add_axes([0.1, 0.0, 0.8, 0.8])
    # plt.xlabel('Birghtness', fontproperties=legend_font2)
    fig = plt.figure(figsize=(4,9))
    ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])
    # ax1.set_title('Inc-v3', fontdict=label_fontdict, pad = 10)

    plt.xlabel('Smoothing methods', fontproperties=legend_font2)
    plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font2)

    x = np.array([1, 2, 3])
    
    plt.grid(axis = 'y')
    plt.xticks(x, method, font=legend_font3)
    plt.yticks((40, 45, 50, 55, 60), font=legend_font3)
    plt.ylim(ymin = 40, ymax=62)

    total_width, n = 1.2, 5
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x + width, TTP, width=width, label='TTP', color='steelblue', alpha=1, zorder=10)
    plt.bar(x + 2 * width, DGTA_PI, width=width, label="DGTA-PI", color='darkorange', alpha=1, zorder=10)
    plt.bar(x + 3 * width, CGNC, width=width, label="CGNC$^{\dagger}$", color='forestgreen', alpha=1, zorder=10)


    plt.legend(loc='upper center', ncol=3, fontsize=20, bbox_to_anchor=(0.5,1.25), prop = {'size':18},columnspacing=1.1)


    plt.savefig('./imgs/bar_single_adv.pdf', dpi=400, bbox_inches='tight')

    plt.show()

# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
# import matplotlib.font_manager as font_manager
# from matplotlib.ticker import MultipleLocator
# from matplotlib.backends.backend_pdf import PdfPages
# from mpl_toolkits.axes_grid1.inset_locator import mark_inset
# from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# from scipy.stats import norm
# import matplotlib.ticker as mtick
# from scipy.interpolate import interp1d
# import os


# legend_font = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=18)
# # legend_font2 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=24)
# legend_font2 = font_manager.FontProperties(weight='normal', style='normal', size=24)
# legend_font3 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=25)
# # legend_font4 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
# legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=28)
# legend_font5 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
# legend_font6 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=23)


# colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]


# method = ['TTP', 'DGTA-PI', 'CGNC']


# TTP = [52.2, 45.9, 44.2]
# DGTA_PI = [55, 50, 47]
# CGNC = [58.08, 61.56, 56.34]


# if __name__ == '__main__':
#     # fig = plt.figure()
#     # ax1 = fig.add_axes([0.1, 0.0, 0.8, 0.8])
#     # plt.xlabel('Birghtness', fontproperties=legend_font2)
#     plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font4)
#     plt.xlabel('Source dataset', fontproperties=legend_font4, color='black')
#     x = np.array([4, 10, 16])
    
#     plt.grid(zorder=0, alpha=0.3)
#     plt.xticks(x, method, font=legend_font2)
#     plt.yticks(list(range(10, 70, 10)), font=legend_font4)
#     plt.ylim(ymin = 8, ymax=67)
#     plt.xlim(xmin = 0, xmax=19)

#     total_width, n = 3, 2
#     width = total_width / n
#     x = x - (total_width - width) / 2

#     plt.bar(x, cgsp, width=width, label='C-GSP', color='green', alpha=1, zorder=10)
#     plt.bar(x + width, cgnc, width=width, label="CGNC", color='orange', alpha=1, zorder=10)
#     # plt.bar(x + 2 * width, GGL, width=width, label="GGL(Li et al.)", color='pink', alpha=1,hatch='\\\\', zorder=10)
#     # plt.bar(x + 3 * width, GIAS, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
#     # plt.bar(x + 4 * width, GILO, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)


#     # plt.legend(loc='upper left', ncol=2, fontsize=24, bbox_to_anchor=(0.48,1.45), prop=legend_font)
#     plt.legend(loc='upper right', ncol=2,  prop=legend_font)
    
#     # ax2 = fig.add_axes([1.13, 0.0, 0.8, 0.8])


#     plt.savefig('./imgs/bar_cross_domain.png', dpi=400, bbox_inches='tight')

#     plt.show()