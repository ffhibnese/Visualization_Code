
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



legend_font = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=18)
legend_font2 = font_manager.FontProperties(weight='normal', style='normal', size=24)
legend_font3 = font_manager.FontProperties(weight='normal', style='normal', size=22)
legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=22)
legend_font5 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=23)


def plot(file_path, vertical_min, vertical_max):
    label_fontdict = {'fontsize': 28}
    method = ['Gaussian', 'Medium', 'Average']
    fig = plt.figure(figsize=(4,9))
    ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])
    # ax1.set_title('Inc-v3', fontdict=label_fontdict, pad = 10)

    plt.xlabel('Smoothing methods', fontproperties=legend_font2)
    plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font2)

    x = np.array([1, 2, 3])
    
    plt.grid(axis = 'y')
    plt.xticks(x, method, font=legend_font3)
    if (vertical_max - vertical_min) // 5 <= 5:
        y_ticks = list(range(vertical_min, vertical_max, 5))
    else:
        y_ticks = list(range(vertical_min, vertical_max, 10))
    
    plt.yticks(y_ticks, font=legend_font4)
    plt.ylim(ymin = vertical_min, ymax=vertical_max)

    total_width, n = 1.2, 5
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x + width, C_GSP, width=width, label='C-GSP', color='steelblue', alpha=1, zorder=10)
    plt.bar(x + 2 * width, CGNC, width=width, label="CGNC", color='darkorange', alpha=1, zorder=10)
    # plt.bar(x + 3 * width, CGNC, width=width, label="CGNC", color='forestgreen', alpha=1, zorder=10)


    # plt.legend(loc='upper center', ncol=2, fontsize=18, bbox_to_anchor=(0.5,1.25), prop = {'size':18},columnspacing=1.1)
    # plt.legend(loc='best', ncol=2, fontsize=18,  prop = {'size':18})


    plt.savefig(file_path, dpi=400, bbox_inches='tight')

    plt.show()




# Inc-v3 -> Inc-v4
C_GSP = [43.93, 50.71, 47.79]
CGNC = [53.64, 61.24, 57.31]
plot('./appendix/bar_incv3_incv4.svg', 40, 63)

# Inc-v3 -> GoogleNet
C_GSP = [21.81, 30.11, 24.74]
CGNC = [30.11, 40.41, 33.95]
plot('./appendix/bar_incv3_gn.svg', 15, 42)

# Inc-v3 -> VGG-16
C_GSP = [28.70, 37.00, 31.90]
CGNC = [38.14, 45.80, 41.08]
plot('./appendix/bar_incv3_vgg16.svg', 20, 47)

# Res-152 -> Inc-v4
C_GSP = [16.96, 25.55, 19.93]
CGNC = [29.00, 43.44, 33.49]
plot('./appendix/bar_res152_incv4.svg', 10, 45)

# Res-152 -> GoogleNet
C_GSP = [20.13, 29.75, 23.99]
CGNC = [31.25, 46.80, 37.05]
plot('./appendix/bar_res152_gn.svg', 15, 49)

# Res-152 -> VGG-16
C_GSP = [33.35, 43.34, 36.95]
CGNC = [45.53, 56.14, 49.98]
plot('./appendix/bar_res152_vgg16.svg', 30, 58)
