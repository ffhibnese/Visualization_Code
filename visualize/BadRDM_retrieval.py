
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

legend_font = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=18)
# legend_font2 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=24)
legend_font2 = font_manager.FontProperties(weight='normal', style='normal', size=27)
legend_font3 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=25)
# legend_font4 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=25)
legend_font5 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=23)
label_fontdict = {'fontsize': 28}

# dataset_label = ['Average(ImageNet)', 'Average(FFHQ)']
# class_id = ['62', '715', '150']
res152_class_id = ['Retrieval$_{ASR}$']
# incv3_class_id = ['62', '150', '952']

no_attack_retrieval_asr = [1]
badrdm_retrieval_asr = [87.5]
no_attack = [0.1632, 0.3035, 0.1509]
BadRDM = [0.7145, 0.4230, 0.0442]   # sim_poison, sim_match, sim_mismatch



# CGNC_res152 = [75.5833, 72.1000, 60.6333]
# fine_tuning_res152 = [75.4333, 73.6333, 70.8167]
# masked_fine_tuning_res152 = [84.2000, 78.3833, 78.4000]



if __name__ == '__main__':
    # fig = plt.figure()
    # ax1 = fig.add_axes([0.1, 0.0, 0.8, 0.8])
    # plt.xlabel('Birghtness', fontproperties=legend_font2)
    fig = plt.figure(figsize=(8,9))
    ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])
    # ax1.set_title('', fontdict=label_fontdict, pad = 10)

    plt.xlabel('Metrics', fontproperties=legend_font2)
    plt.ylabel('Retrieval ASR (%)', fontproperties=legend_font2)

    class_id = ['Retrieval$_{ASR}$', 'Sim$_{poison}$', 'Sim$_{match}$', 'Sim$_{mis}$']
    x = np.array([1])
    total_width, n = 1.2, 5
    width = total_width / n
    plt.grid(axis = 'y')
    # plt.xticks(x, res152_class_id, font=legend_font4)
    plt.yticks((10, 30, 50, 70), font=legend_font4)
    plt.ylim(ymin = 0, ymax=89)
    # plt.xlim(xmin = 0, xmax=10)


    # x = x - (total_width - width) / 2
    plt.bar(x - 0.5 * width, no_attack_retrieval_asr, width=width, label='No Attack', color='powderblue', alpha=0.98, zorder=10)
    plt.bar(x + 0.5 * width, badrdm_retrieval_asr, width=width, label="BadRDM", color='salmon', alpha=0.98, zorder=10)

    x = np.array([1, 2, 3, 4])
    plt.xticks(x, class_id, font=legend_font4)
    
    ax1_sub = ax1.twinx()  # 创建共享 x 轴的新 y 轴
    # plt.tick_params(labelsize=20)
    plt.yticks((0.1, 0.30, 0.50, 0.70), font=legend_font4)
    ax1_sub.set_ylim(ymin = 0, ymax=0.75)
    ax1_sub.set_ylabel('CLIP Similarity', fontproperties=legend_font2)
    x = np.array([2, 3, 4])

    plt.bar(x - 0.5 * width, no_attack, width=width, label='No Attack', color='powderblue', alpha=0.98, zorder=10)
    plt.bar(x + 0.5 * width, BadRDM, width=width, label="BadRDM", color='salmon', alpha=0.98, zorder=10)
    # plt.bar(x + 3 * width, GIAS_PSNR, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    # plt.bar(x + 4 * width, GILO_PSNR, width=width, label="GILO(Ours)", color='darkorange', alpha=1, hatch='///', zorder=10)


    # plt.legend(loc='upper center', ncol=3, fontsize=24, bbox_to_anchor=(1.15,1.4), prop = {'size':24})
    plt.legend(loc='upper center', ncol=3, fontsize=24, bbox_to_anchor=(0.5,1.25), prop = {'size':24})
    # plt.legend(loc='upper left', ncol=2, fontsize=14, prop=legend_font)
    # 





    # ax2 = fig.add_axes([1.5, 0.0, 1.1, 0.4])

    # ax2.set_title('Res-152', fontdict=label_fontdict, pad = 10)

    # plt.xlabel('Class id', fontproperties=legend_font2)
    # plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font2)

    # x = np.array([1, 2 ,3])
    
    # plt.grid(axis = 'y')
    # plt.xticks(x, res152_class_id, font=legend_font4)
    # plt.yticks((50, 60, 70, 80), font=legend_font4)
    # plt.ylim(ymin = 50, ymax=88)

    # total_width, n = 1.2, 5
    # width = total_width / n
    # x = x - (total_width - width) / 2

    # plt.bar(x + width, CGNC_res152, width=width, label='CGNC', color='steelblue', alpha=1, zorder=10)
    # plt.bar(x + 2 * width, fine_tuning_res152, width=width, label="Fine-tuning", color='darkorange', alpha=1, zorder=10)
    # plt.bar(x + 3 * width, masked_fine_tuning_res152, width=width, label="Masked fine-tuning", color='forestgreen', alpha=1, zorder=10)



    # ax3 = fig.add_axes([0.1, -0.51, 1.1, 0.4])

    # plt.ylabel('SSIM', fontproperties=legend_font2)

    # x = np.array([2,4])
    
    # plt.grid(zorder=0)
    # plt.xticks(x, dataset_label, font=legend_font4)
    # plt.yticks((0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6), font=legend_font4)
    # plt.ylim(ymin = 0, ymax=0.65)

    # total_width, n = 1.2, 5
    # width = total_width / n
    # x = x - (total_width - width) / 2

    # plt.bar(x, Yin_SSIM, width=width, label='Yin et al.', color='blue', alpha=1, zorder=10)
    # plt.bar(x + width, Geiping_SSIM, width=width, label="Geiping et al.", color='pink', alpha=1, zorder=10)
    # plt.bar(x + 2 * width, GGL_SSIM, width=width, label="GGL(Li et al.)", color='green', alpha=1,hatch='\\\\', zorder=10)
    # plt.bar(x + 3 * width, GIAS_SSIM, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    # plt.bar(x + 4 * width, GILO_SSIM, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)

    # ax4 = fig.add_axes([1.53, -0.51, 1.1, 0.4])
    # # ax2 = fig.add_axes([1.13, 0.0, 0.8, 0.8])
    # plt.ylabel('MSE', fontproperties=legend_font2)

    # x = np.array([2,4])
    
    # plt.grid(zorder=0)
    # plt.xticks(x, dataset_label, font=legend_font4)
    # plt.yticks((0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06), font=legend_font4)
    # plt.ylim(ymin = 0, ymax=0.065)

    # total_width, n = 1.2, 5
    # width = total_width / n
    # x = x - (total_width - width) / 2

    # plt.bar(x, Yin_MSE, width=width, label='Yin et al.', color='blue', alpha=1, zorder=10)
    # plt.bar(x + width, Geiping_MSE, width=width, label="Geiping et al.", color='pink', alpha=1, zorder=10)
    # plt.bar(x + 2 * width, GGL_MSE, width=width, label="GGL(Li et al.)", color='green', alpha=1,hatch='\\\\', zorder=10)
    # plt.bar(x + 3 * width, GIAS_MSE, width=width, label="GIAS(Jeon et al.)", color='red', alpha=1, hatch='\\\\\\', zorder=10)
    # plt.bar(x + 4 * width, GILO_MSE, width=width, label="GILO(Ours)", color='orange', alpha=1, hatch='///', zorder=10)

    plt.savefig('../imgs/badrdm_retrieval_bar.pdf', dpi=400, bbox_inches='tight')

    plt.show()