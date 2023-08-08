
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
style='normal', size=18)
legend_font2 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=18)
legend_font3 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)
legend_font4 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=18)
legend_font5 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=23)


dataset_label = ['Average(ImageNet)', 'Average(FFHQ)']
scale_label = ['0.5', '0.75', '0.9', '1.2', '1.4', '1.6']

Yin_PSNR = [16.51093376159668, 14.94846567426409]
Geiping_PSNR = [17.07564058303833, 15.352284186226981]
GGL_PSNR = [13.38850298, 15.133514404296875]
GIAS_PSNR = [17.49231453, 20.179915973118373]
GILO_PSNR = [20.05337984, 21.33953969]


Yin_LPIPS = [0.329702088, 0.450280150771141]
Geiping_LPIPS = [0.307813126, 0.417246025800704]
GGL_LPIPS = [0.366744350194931, 0.20091487158622]
GIAS_LPIPS = [0.255304609835147,0.126554154657891]
GILO_LPIPS = [0.155927148684859, 0.100719165429472]

Yin_SSIM = [0.267327353134751, 0.204412868618965]
Geiping_SSIM = [0.290757923945784, 0.227172717132738]
GGL_SSIM = [0.122672946341335, 0.245335346460342]
GIAS_SSIM = [0.333365428000688, 0.537913797582898]
GILO_SSIM = [0.471344228982925, 0.577524675215993]


Yin_MSE = [0.0257869706815108, 0.0342568950195397]
Geiping_MSE = [0.0223093697708099, 0.0311348349787294]
GGL_MSE = [0.0545781713258474, 0.0339073167714689]
GIAS_MSE = [0.0229138274863361, 0.0121031767356075]
GILO_MSE = [0.0141214103577658, 0.0103271254903769]


if __name__ == '__main__':
    # fig = plt.figure()
    # ax1 = fig.add_axes([0.1, 0.0, 0.8, 0.8])
    # plt.xlabel('Birghtness', fontproperties=legend_font2)
    fig = plt.figure(figsize=(5,8))
    ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])
    plt.ylabel('PSNR(dB)', fontproperties=legend_font2)

    x = np.array([2,4])
    
    plt.grid(zorder=0)
    plt.xticks(x, dataset_label, font=legend_font4)
    plt.yticks((10, 12, 14, 16, 18, 20, 22), font=legend_font4)
    plt.ylim(ymin = 10, ymax=23)

    total_width, n = 1.2, 5
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, Yin_PSNR, width=width, label='Yin et al.', color='blue', alpha=1, zorder=10)
    plt.bar(x + width, Geiping_PSNR, width=width, label="Geiping et al.", color='pink', alpha=1, zorder=10)
    plt.bar(x + 2 * width, GGL_PSNR, width=width, label="GGL(Li et al.)", color='green', alpha=1,hatch='\\\\', zorder=10)
    plt.bar(x + 3 * width, GIAS_PSNR, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    plt.bar(x + 4 * width, GILO_PSNR, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)


    plt.legend(loc='upper left', ncol=2, fontsize=24, bbox_to_anchor=(0.62,1.45), prop=legend_font)
    # plt.legend(loc='upper left', ncol=2, fontsize=14, prop=legend_font)
    
    ax2 = fig.add_axes([1.53, 0.0, 1.1, 0.4])
    plt.ylabel('LPIPS', fontproperties=legend_font2)

    x = np.array([2,4])
    
    plt.grid(zorder=0)
    plt.xticks(x, dataset_label, font=legend_font4)
    plt.yticks((0, 0.1, 0.2, 0.3, 0.4, 0.5), font=legend_font4)
    plt.ylim(ymin = 0, ymax=0.55)

    total_width, n = 1.2, 5
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, Yin_LPIPS, width=width, label='Yin et al.', color='blue', alpha=1, zorder=10)
    plt.bar(x + width, Geiping_LPIPS, width=width, label="Geiping et al.", color='pink', alpha=1, zorder=10)
    plt.bar(x + 2 * width, GGL_LPIPS, width=width, label="GGL(Li et al.)", color='green', alpha=1,hatch='\\\\', zorder=10)
    plt.bar(x + 3 * width, GIAS_LPIPS, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    plt.bar(x + 4 * width, GILO_LPIPS, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)

    ax3 = fig.add_axes([0.1, -0.51, 1.1, 0.4])

    plt.ylabel('SSIM', fontproperties=legend_font2)

    x = np.array([2,4])
    
    plt.grid(zorder=0)
    plt.xticks(x, dataset_label, font=legend_font4)
    plt.yticks((0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6), font=legend_font4)
    plt.ylim(ymin = 0, ymax=0.65)

    total_width, n = 1.2, 5
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, Yin_SSIM, width=width, label='Yin et al.', color='blue', alpha=1, zorder=10)
    plt.bar(x + width, Geiping_SSIM, width=width, label="Geiping et al.", color='pink', alpha=1, zorder=10)
    plt.bar(x + 2 * width, GGL_SSIM, width=width, label="GGL(Li et al.)", color='green', alpha=1,hatch='\\\\', zorder=10)
    plt.bar(x + 3 * width, GIAS_SSIM, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    plt.bar(x + 4 * width, GILO_SSIM, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)

    ax4 = fig.add_axes([1.53, -0.51, 1.1, 0.4])
    # ax2 = fig.add_axes([1.13, 0.0, 0.8, 0.8])
    plt.ylabel('MSE', fontproperties=legend_font2)

    x = np.array([2,4])
    
    plt.grid(zorder=0)
    plt.xticks(x, dataset_label, font=legend_font4)
    plt.yticks((0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06), font=legend_font4)
    plt.ylim(ymin = 0, ymax=0.065)

    total_width, n = 1.2, 5
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, Yin_MSE, width=width, label='Yin et al.', color='blue', alpha=1, zorder=10)
    plt.bar(x + width, Geiping_MSE, width=width, label="Geiping et al.", color='pink', alpha=1, zorder=10)
    plt.bar(x + 2 * width, GGL_MSE, width=width, label="GGL(Li et al.)", color='green', alpha=1,hatch='\\\\', zorder=10)
    plt.bar(x + 3 * width, GIAS_MSE, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    plt.bar(x + 4 * width, GILO_MSE, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)

    plt.savefig('/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/imgs/multiple_bar.pdf', dpi=400, bbox_inches='tight')

    plt.show()