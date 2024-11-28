
import numpy as np
import matplotlib
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

plt.rc('font',family='Times New Roman', style='italic' ,size=27)

legend_font = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=14)
legend_font2 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=18)
legend_font3 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)
legend_font4 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=16)
legend_font5 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='italic', size=21)
legend_font6 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=23)

# dataset_label = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dataset_label = [2, 3, 4, 5, 6, 7]
scale_label = ['0.5', '0.75', '0.9', '1.2', '1.4', '1.6']

# FFHQ = [17.74331191380819, 20.60249360402425, 21.363702742258706, 21.798252042134603, 21.934241739908853, 21.86078306833903, 21.876904996236167, 21.792083994547525]
FFHQ = [21.363702742258706, 21.798252042134603, 21.934241739908853, 21.86078306833903, 21.876904996236167, 21.792083994547525]
ImageNet = [19.124453449249266,19.42495765686035,19.486266899108887,19.60903263092041,19.650402990976968,19.608871936798096,19.727670892079672,19.692021656036378,19.69910084406535,19.69800287882487]


if __name__ == '__main__':
    # fig = plt.figure()
    # ax1 = fig.add_axes([0.1, 0.0, 0.8, 0.8])
    plt.xlabel('K')
    plt.ylabel('PSNR(dB)', fontproperties=legend_font5)
    # plt.title('BigGAN', fontproperties=legend_font5)
    # x = np.arange(1, 11)
    x = np.array([0.2 * i for i in range(1, 7)])
    
    plt.grid(zorder=0, alpha=0.3)
    plt.xticks(x, dataset_label, font=legend_font4)
    plt.yticks((21, 21.1, 21.2, 21.3, 21.4, 21.5, 21.6, 21.7, 21.8, 21.9, 22), font=legend_font4)
    # plt.yticks((19, 19.1, 19.2, 19.3, 19.4, 19.5, 19.6, 19.7, 19.8), font=legend_font4)
    plt.ylim(ymin = 21.2, ymax=22.05)
    # plt.ylim(ymin = 19, ymax=19.85)


    total_width, n = 0.12, 1
    # total_width, n = 0.8, 1

    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, FFHQ, width=width, label='imagenet', color='blue', alpha=0.7, zorder=10)
    # plt.bar(x + width, Geiping, width=width, label="Geiping et al.", color='pink', alpha=1, zorder=10)
    # plt.bar(x + 2 * width, GGL, width=width, label="GGL(Li et al.)", color='green', alpha=1,hatch='\\\\', zorder=10)
    # plt.bar(x + 3 * width, GIAS, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    # plt.bar(x + 4 * width, GILO, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)


    # plt.legend(loc='upper left', ncol=2, fontsize=24, bbox_to_anchor=(0.48,1.45), prop=legend_font)
    # plt.legend(loc='upper left', ncol=2, fontsize=14, prop=legend_font)
    
    # ax2 = fig.add_axes([1.13, 0.0, 0.8, 0.8])


    plt.savefig('/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/imgs/select_layers_ffhq_psnr.pdf', dpi=400, bbox_inches='tight')

    plt.show()