import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager
plt.rcParams['font.sans-serif'] = ['Times New Roman']


legend_font = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=18)
# legend_font2 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=24)
legend_font2 = font_manager.FontProperties(weight='normal', style='normal', size=24)
legend_font3 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=25)
# legend_font4 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=22)
legend_font5 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=23)

colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]
C_GSP = []
CGNC = []

def plot(file_path, vertical_min, vertical_max):
    
    fig = plt.figure(figsize=(4,8))
    ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])
    plt.xlabel('JPEG quality', fontproperties=legend_font2, color='black')
    plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font2, color='black')
    quality = [70, 75, 80, 85, 90]
    dot_size = 8
    line_width = 4.7
    p1,=plt.plot(quality, C_GSP, 's-',markersize=dot_size, color='green', linewidth=line_width, alpha=1, label='TTP')
    p2,=plt.plot(quality, CGNC, 'o-',markersize=dot_size, color='red', linewidth=line_width, alpha=1, label='DGTA-PI')
    # p3,=plt.plot(quality, CGNC, 's-',markersize=dot_size, color='violet', linewidth=line_width, alpha=1, label='VTM')
    '''p4,=plt.plot(scalehyperpriorx, scalehyperpriory, 'o-',markersize=dot_size, color='purple', linewidth=line_width, alpha=1, label='SHP')
    p5,=plt.plot(scalehyperpriorx_id, scalehyperpriory_id, linestyle='-',marker='o',markersize=dot_size, color='seagreen', linewidth=line_width, alpha=1, label='SHP-id')
    p6,= plt.plot(scalehyperpriorx_msfd, scalehyperpriory_msfd, 'o-',markersize=dot_size, color='b', linewidth=line_width, alpha=1, label='SHP-msfd')
    '''
    # plt.legend((p1, p2), ('C-GSP', 'CGNC'), ncol=2, frameon=True, loc='best', bbox_to_anchor=(1.2,1.3), fontsize=20, columnspacing=1)

    plt.xticks(font=legend_font4)
    plt.yticks(font=legend_font4)
    '''
    plt.tick_params(labelsize=16)
    labels = ax1.get_xticklabels() + ax1.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    '''
    plt.grid(axis = 'y')

        
    ax1.grid(which='minor', alpha=0.2)                                                
    ax1.grid(which='major', alpha=0.5)  
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False) 

    plt.text(x=0.215,#文本x轴坐标 
            y=18.1, #文本y轴坐标
            s='', #文本内容
            rotation=1,#文字旋转
            color = [0.0,0,0],
            ha='center',#x=2.2是文字的左端位置,可选'center', 'right', 'left'
            va='baseline',#y=8是文字的低端位置,可选'center', 'top', 'bottom', 'baseline', 'center_baseline'
            fontproperties=legend_font6#字体属性设置
            )

    # plt.xticks((70, 75, 80, 85, 90), font=legend_font4)
    plt.xticks(quality, font=legend_font4)
    if (vertical_max - vertical_min) // 5 <= 5:
        y_ticks = list(range(vertical_min, vertical_max, 5))
    else:
        y_ticks = list(range(vertical_min, vertical_max, 10))

    plt.yticks(y_ticks, font=legend_font4)
    plt.ylim(ymin = vertical_min, ymax=vertical_max)
    plt.savefig(file_path, dpi=400, bbox_inches='tight')
    plt.show()


# Inc-v3 -> Inc-v4
C_GSP = [36.45, 37.94, 39.63, 40.9, 42.85]
CGNC = [49.4, 50.69, 52.53, 54.05, 55.65]
plot('./appendix/line_incv3_incv4.svg', 30, 58)

# Inc-v3 -> GoogleNet
C_GSP = [34.21, 35.19, 36.79, 37.55, 38.61]
CGNC = [44.10, 45.51, 47.13, 48.01, 49.13]
plot('./appendix/line_incv3_gn.svg', 30, 52)


# Inc-v3 -> VGG-16
C_GSP = [38.48, 39.84, 41.56, 43.08, 43.78]
CGNC = [45.43, 46.66, 48.49, 49.66, 51.08]
plot('./appendix/line_incv3_vgg16.svg', 35, 52)


# Res-152 -> Inc-v4
C_GSP = [23.58, 24.51, 25.83, 27.38, 29.15]
CGNC = [39.33, 40.88, 42.38, 43.81, 46.03]
plot('./appendix/line_res152_incv4.svg', 20, 49)


# Res-152 -> GoogleNet
C_GSP = [28.09, 29.66, 31.39, 33.29, 36.16]
CGNC = [45.04, 47.00, 49.21, 51.86, 55.09]
plot('./appendix/line_res152_gn.svg', 25, 57)


# Res-152 -> VGG-16
C_GSP = [39.33, 40.51, 42.29, 43.11, 43.79]
CGNC = [52.10, 54.09, 56.19, 57.80, 59.70]
plot('./appendix/line_res152_vgg16.svg', 35, 63)



