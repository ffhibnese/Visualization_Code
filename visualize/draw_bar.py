
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
style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=23)


dataset_label = ['Average(ImageNet)', 'Average(FFHQ)']
scale_label = ['0.5', '0.75', '0.9', '1.2', '1.4', '1.6']

Yin = [16.51093376159668, 14.94846567426409]
Geiping = [17.07564058, 15.352284186226981]
GGL = [13.38850298, 15.133514404296875]
GIAS = [17.49231453, 20.179915973118373]
GILO = [20.05337984, 21.33953969]

if __name__ == '__main__':
    # fig = plt.figure()
    # ax1 = fig.add_axes([0.1, 0.0, 0.8, 0.8])
    # plt.xlabel('Birghtness', fontproperties=legend_font2)
    plt.ylabel('PSNR(dB)', fontproperties=legend_font2)

    x = np.array([2,4])
    
    plt.grid(zorder=0)
    plt.xticks(x, dataset_label, font=legend_font4)
    plt.yticks((10, 12, 14, 16, 18, 20, 22, 24), font=legend_font4)
    plt.ylim(ymin = 10, ymax=25)

    total_width, n = 1.2, 5
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, Yin, width=width, label='Yin et al.', color='blue', alpha=1, zorder=10)
    plt.bar(x + width, Geiping, width=width, label="Geiping et al.", color='pink', alpha=1, zorder=10)
    plt.bar(x + 2 * width, GGL, width=width, label="GGL(Li et al.)", color='green', alpha=1,hatch='\\\\', zorder=10)
    plt.bar(x + 3 * width, GIAS, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    plt.bar(x + 4 * width, GILO, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)


    # plt.legend(loc='upper left', ncol=2, fontsize=24, bbox_to_anchor=(0.48,1.45), prop=legend_font)
    plt.legend(loc='upper left', ncol=2, fontsize=14, prop=legend_font)
    
    # ax2 = fig.add_axes([1.13, 0.0, 0.8, 0.8])


    plt.savefig('/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/imgs/bar_psnr.pdf', dpi=400, bbox_inches='tight')

    plt.show()