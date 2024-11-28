
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
legend_font5 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=23)
legend_font6 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=23)
label_fontdict = {'fontsize': 28}
colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]

# fig = plt.figure(figsize=(5,8))

# ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])

# plt.xlim(xmin = 0, xmax=3300)

plt.xlabel('Class numbers', fontproperties=legend_font4, color='black')
plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font4, color='black')


knn_asr = [0.972125, 0.9639, 0.974125, 0.938, 0.97725, 0.97075]
knn_clip_attack = [0.303756, 0.301039, 0.303745, 0.30294, 0.30427, 0.303518]
knn_fid = [21.43135, 20.823219, 21.588, 22.34, 22.50102, 22.9169]
knn_clip_benign = [0.295738, 0.294664, 0.2944, 0.29392, 0.292957, 0.29107]

multi_trig_asr = [0.971, 0.974125, 0.987125, 0.98003, 0.943234]
multi_trig_clip_attack =[0.303914, 0.303745, 0.298358, 0.299589, 0.30205]
multi_trig_fid = [21.49328, 21.588, 21.55068, 21.141638, 21.120927]
multi_trig_clip_benign = [0.294535, 0.2944, 0.294978, 0.295623, 0.29587]

lambda_asr = [0.972625, 0.974375, 0.974125, 0.98025, 0.978125]
lambda_clip_attack = [0.302798, 0.3034, 0.303745, 0.3035619, 0.303506]
lambda_fid = [21.16801, 21.590129, 21.588, 21.65975, 21.682385]
lambda_clip_benign = [0.29462, 0.294303, 0.2944, 0.294848, 0.2951789]

BadNet_CA = [41.31, 44.15, 49.01, 54.87, 57.51]
Blended_CA	= [42.11, 45.31, 50.13, 55.33, 58.79]
SIG_CA	= [41.95, 45.52, 50.56, 54.57, 59.13]
SSBA_CA = [40.24, 44.8, 48.86, 52.63, 57.94]
WaNet_CA = [41.98, 45.48, 50.25, 55.09, 59.17]
TrojVQA_CA = [40.86, 44.23, 49.03, 53.95, 58.17]
BadCLIP_CA	= [40.54, 44.74, 48.94, 54.41, 58.75]

BadNet_ASR = [1.66, 1.25, 1.4, 0.23, 0.1]
Blended_ASR	= [3.54, 2.55, 2.95, 1.22, 0.05]
SIG_ASR	= [6.43, 5.79, 5.82, 4.53, 3.69]
SSBA_ASR = [0.66, 0.33, 0.31, 0.13, 0.11]
WaNet_ASR = [7.28, 6.29, 6.48, 0.38, 0.36]
TrojVQA_ASR = [4.01, 5.89, 4.72, 0.55, 0.2]
BadCLIP_ASR	= [12.13, 7.96, 6.5, 3.19, 0.64]


plt.grid(alpha=0.3)

if __name__ == '__main__':
    # fig = plt.figure()
    # ax1 = fig.add_axes([0.1, 0.0, 0.8, 0.8])
    # plt.xlabel('Birghtness', fontproperties=legend_font2)
    fig = plt.figure(figsize=(5,9))
    ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.5])
    # ax1.set_title('Retrieval number', fontdict=label_fontdict, pad = 10)

    plt.xlabel('Shots', fontproperties=legend_font2)
    plt.ylabel('CA (%)', fontproperties=legend_font2)
    plt.grid(zorder=0, alpha=0.3)
    x = np.array([1, 2, 3, 4, 5])
    x_label = np.array([1, 2, 4, 8, 16])
    y = np.array(list(range(40, 61, 5))) 

    dot_size = 13
    line_width = 3.5
    alpha_1, alpha_2, alpha_3, alpha_4 = 1, 1, 0.85, 1
    
    p4,= plt.plot(x, BadNet_CA, '*-',markersize=dot_size, color='red', linewidth=line_width, alpha=alpha_1, label='BadNet')
    p2,=plt.plot(x, SIG_CA, 'p-',markersize=dot_size, color='seagreen', linewidth=line_width, alpha=alpha_2, label='SIG')
    p3,= plt.plot(x, WaNet_CA, 'x-',markersize=15, color='sandybrown', linewidth=line_width, alpha=alpha_3, label='WaNet')
    p4,= plt.plot(x, BadCLIP_CA, 'x-',markersize=15, color='purple', linewidth=line_width, alpha=alpha_4, label='BadCLIP')
    
   
    

    # p5, = plt.plot(x, GIFD, 's-',markersize=9, color='#0504aa', linewidth=2.5, alpha=1, label='GIFD')
    plt.xlim(xmin = 0.5, xmax=5.4)
    plt.ylim(ymin = 39, ymax=61)
    # plt.legend((p1, p2, p3, p4, p5), ('IG (Geiping et al.)', 'GI (Yin et al.)', 'GGL (Li et al.)', 'GIAS (Jeon et al.)', 'GIFD'), ncol=1, prop=legend_font, loc='best')

    plt.xticks(x, x_label, font=legend_font4)
    plt.yticks(y, y, font=legend_font4)
    
    # ax1_sub = ax1.twinx()  # 创建共享 x 轴的新 y 轴
    # # 绘制第二条曲线
    # # ax1_sub.plot(x, y2, 'r-', label='cos(x)')
    # # ax1_sub.set_ylabel('cos(x)', color='r')
    # ax1_sub.plot(x, knn_fid, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=alpha_4, label='FID')
    # ax1_sub.set_ylim(ymin = 19, ymax=23.95)
    # ax1_sub.set_ylabel('FID score', fontproperties=legend_font2)
    # # plt.legend((p1, p2, p3, p4, p5), ('IG (Geiping et al.)', 'GI (Yin et al.)', 'GGL (Li et al.)', 'GIAS (Jeon et al.)', 'GIFD'), ncol=1, prop=legend_font, loc='best')
    # y = np.array(list(range(19, 24, 1)))
    # ax1_sub.set_yticks(y, y, font=legend_font4)
    
    # plt.legend(prop=legend_font)


    # plt.legend(loc='upper center', ncol=3, fontsize=24, bbox_to_anchor=(1.15,1.4), prop = {'size':24})
    fig.legend(loc='upper center', ncol=4, fontsize=24, bbox_to_anchor=(1.35, 0.6), prop = {'size':24})
    # plt.legend(loc='upper left', ncol=2, fontsize=14, prop=legend_font)


    ax2 = fig.add_axes([1.5, 0.0, 1.1, 0.5])
    plt.grid(zorder=0, alpha=0.3)
    plt.xlabel('Shots', fontproperties=legend_font2)
    plt.ylabel('ASR (%)', fontproperties=legend_font2)
    
    x = np.array([1, 2, 3, 4, 5])
    x_label = np.array([1, 2, 4, 8, 16])
    y = np.array(list(range(0, 14, 2)))


    p4,= plt.plot(x, BadNet_ASR, '*-',markersize=dot_size, color='red', linewidth=line_width, alpha=alpha_1, label='BadNet')
    p2,=plt.plot(x, SIG_ASR, 'p-',markersize=dot_size, color='seagreen', linewidth=line_width, alpha=alpha_2, label='SIG')
    p3,= plt.plot(x, WaNet_ASR, 'x-',markersize=dot_size, color='sandybrown', linewidth=line_width, alpha=alpha_3, label='WaNet')
    p4,= plt.plot(x, BadCLIP_ASR, 'x-',markersize=dot_size, color='purple', linewidth=line_width, alpha=alpha_4, label='BadCLIP')
    
   
    # p5, = plt.plot(x, GIFD, 's-',markersize=9, color='#0504aa', linewidth=2.5, alpha=1, label='GIFD')
    plt.xlim(xmin = 0.5, xmax=5.4)
    plt.ylim(ymin = 0, ymax=12.8)
    # plt.legend((p1, p2, p3, p4, p5), ('IG (Geiping et al.)', 'GI (Yin et al.)', 'GGL (Li et al.)', 'GIAS (Jeon et al.)', 'GIFD'), ncol=1, prop=legend_font, loc='best')

    plt.xticks(x, x_label, font=legend_font4)
    plt.yticks(y, y, font=legend_font4)
    
    # ax2_sub = ax2.twinx()  # 创建共享 x 轴的新 y 轴
    # # 绘制第二条曲线
    # # ax1_sub.plot(x, y2, 'r-', label='cos(x)')
    # # ax1_sub.set_ylabel('cos(x)', color='r')
    # ax2_sub.plot(x, multi_trig_fid, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=alpha_4, label='FID')
    # ax2_sub.set_ylim(ymin = 19, ymax=23.95)
    # ax2_sub.set_ylabel('FID score', fontproperties=legend_font2)
    # # plt.legend((p1, p2, p3, p4, p5), ('IG (Geiping et al.)', 'GI (Yin et al.)', 'GGL (Li et al.)', 'GIAS (Jeon et al.)', 'GIFD'), ncol=1, prop=legend_font, loc='best')
    # y = np.array(list(range(19, 24, 1)))
    # ax2_sub.set_yticks(y, y, font=legend_font4)
    # ax2.set_title('Res-152', fontdict=label_fontdict, pad = 10)

    # plt.xlabel('Class id', fontproperties=legend_font2)
    # plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font2)

    # x = np.array([1, 2, 3, 4, 5])
    
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
    # ax3 = fig.add_axes([3.6, 0.0, 1.1, 0.4])
    # plt.grid(zorder=0, alpha=0.3)
    # plt.xlabel('$\lambda$', fontproperties=legend_font2)
    # plt.ylabel('ASR / CLIP similarity', fontproperties=legend_font2)
    
    # x = np.array([1, 2, 3, 4, 5])
    # x_label = np.array([0.01, 0.03, 0.1, 0.3, 1])
    # y = np.array(list(range(30, 101, 20))) / 100.0

    # p4,= plt.plot(x, lambda_asr, '*-',markersize=dot_size, color='red', linewidth=line_width, alpha=alpha_1, label='ASR')
    # p2,=plt.plot(x, lambda_clip_attack, 'p-',markersize=dot_size, color='seagreen', linewidth=line_width, alpha=alpha_2, label='CLIP-Attack')
    # p3,= plt.plot(x, lambda_clip_benign, 'x-',markersize=dot_size, color='violet', linewidth=line_width, alpha=alpha_3, label='CLIP-Benign')
   
    # # p5, = plt.plot(x, GIFD, 's-',markersize=9, color='#0504aa', linewidth=2.5, alpha=1, label='GIFD')
    # plt.xlim(xmin = 0.5, xmax=5.4)
    # plt.ylim(ymin = 0.2, ymax=1.03)
    # # plt.legend((p1, p2, p3, p4, p5), ('IG (Geiping et al.)', 'GI (Yin et al.)', 'GGL (Li et al.)', 'GIAS (Jeon et al.)', 'GIFD'), ncol=1, prop=legend_font, loc='best')

    # plt.xticks(x, x_label, font=legend_font4)
    # plt.yticks(y, y, font=legend_font4)
    
    # ax3_sub = ax3.twinx()  # 创建共享 x 轴的新 y 轴
    # # 绘制第二条曲线
    # # ax1_sub.plot(x, y2, 'r-', label='cos(x)')
    # # ax1_sub.set_ylabel('cos(x)', color='r')
    # ax3_sub.plot(x, multi_trig_fid, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=alpha_4, label='FID')
    # ax3_sub.set_ylim(ymin = 19, ymax=23.95)
    # ax3_sub.set_ylabel('FID score', fontproperties=legend_font2)
    # # plt.legend((p1, p2, p3, p4, p5), ('IG (Geiping et al.)', 'GI (Yin et al.)', 'GGL (Li et al.)', 'GIAS (Jeon et al.)', 'GIFD'), ncol=1, prop=legend_font, loc='best')
    # y = np.array(list(range(19, 24, 1)))
    # ax3_sub.set_yticks(y, y, font=legend_font4)


    # ax3 = fig.add_axes([0.1, -0.51, 1.1, 0.4])

    # plt.ylabel('SSIM', fontproperties=legend_font2)

    # x = np.array([1, 2, 3, 4, 5])
    
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

    plt.savefig('../imgs/CBPT_shots.pdf', dpi=400, bbox_inches='tight')

    plt.show()
