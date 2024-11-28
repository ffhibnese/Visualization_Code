import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager
plt.rcParams['font.sans-serif'] = ['Times New Roman']

# legend_font = font_manager.FontProperties(fname="Times/times.ttf",
# weight='normal',
# style='normal', size=18)
# legend_font2 = font_manager.FontProperties(fname="Times/times.ttf",
# weight='semibold',
# style='normal', size=20)
# legend_font3 = font_manager.FontProperties(fname="Times/timesbd.ttf",
# weight='semibold',
# style='normal', size=25)
# legend_font4 = font_manager.FontProperties(fname="Times/times.ttf",
# weight='normal',
# style='normal', size=18)
# legend_font5 = font_manager.FontProperties(fname="Times/times.ttf",
# weight='normal',
# style='normal', size=20)
# legend_font6 = font_manager.FontProperties(fname="Times/timesi.ttf",
# weight='semibold',
# style='normal', size=25)
legend_font = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=18)
# legend_font2 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=24)
legend_font2 = font_manager.FontProperties(weight='normal', style='normal', size=24)
legend_font3 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=25)
# legend_font4 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=22)
legend_font5 = font_manager.FontProperties(fname="Times/Times-New-Romance.ttf", weight='normal', style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="Times/Times New Roman MT Extra Bold.ttf", weight='semibold', style='normal', size=23)

colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]

fig = plt.figure(figsize=(4,8))

ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])

plt.xlabel('JPEG quality', fontproperties=legend_font2, color='black')
plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font2, color='black')

plt.ylim(ymin = 53, ymax=68)
quality = [70, 75, 80, 85, 90]
TTP = [54.1, 56.0, 57.9, 60.1, 62.0]
DGTA_PI = [57.2, 59.1, 61.1, 63.0, 64.9]
CGNC = [59.91, 61.82, 63.64, 64.49, 65.8]

dot_size = 8
line_width = 2.5
p1,=plt.plot(quality, TTP, 'o-',markersize=dot_size, color='orange', linewidth=line_width, alpha=1, label='TTP')
p2,=plt.plot(quality, DGTA_PI, '*-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=1, label='DGTA-PI')
p3,=plt.plot(quality, CGNC, 's-',markersize=dot_size, color='violet', linewidth=line_width, alpha=1, label='VTM')
'''p4,=plt.plot(scalehyperpriorx, scalehyperpriory, 'o-',markersize=dot_size, color='purple', linewidth=line_width, alpha=1, label='SHP')
p5,=plt.plot(scalehyperpriorx_id, scalehyperpriory_id, linestyle='-',marker='o',markersize=dot_size, color='seagreen', linewidth=line_width, alpha=1, label='SHP-id')
p6,= plt.plot(scalehyperpriorx_msfd, scalehyperpriory_msfd, 'o-',markersize=dot_size, color='b', linewidth=line_width, alpha=1, label='SHP-msfd')
'''
# p7,=plt.plot(cheng2020x, cheng2020y, 'o-',markersize=9, color='#c79fef', linewidth=2.5, alpha=1, label='SHP') #dodgerblue
# #p8,= plt.plot(cheng2020x_id, cheng2020y_id, 'o-',markersize=9, color='#c79fef', linewidth=2.5, alpha=1, label='cheng2020-msfd')
# p9,= plt.plot(cheng2020x_msfd, cheng2020y_msfd, 'o-',markersize=9, color='#9a0eea', linewidth=2.5, alpha=1, label='cheng2020-msfd')
# p10,= plt.plot(CPMx_id, CPMy_id, 'o-',markersize=9, color='#e6dda6', linewidth=2.5, alpha=1, label='CPM-msfd')
# p11, = plt.plot(NDIC_UCIx, NDIC_UCIy, 'o-',markersize=9, color='lightgreen', linewidth=2.5, alpha=1, label='NDIC-UCI')
#plt.legend((p9, p6, p3, p5, p4, p2, p1), ('Cheng-msfd', 'SHP-msfd', 'VTM', 'SHP-id', 'SHP', 'BPG', 'JPEG2000'), ncol=1, frameon=False, prop=legend_font, loc='center right', bbox_to_anchor=(1.02,0.32))
plt.legend((p1, p2, p3), ('TTP', 'DGTA-PI', 'CGNC$^{\dagger}$'), ncol=3, frameon=False, loc='best', bbox_to_anchor=(1.1,1.3), fontsize=18, columnspacing=1)

plt.xticks(font=legend_font4)
plt.yticks(font=legend_font4)
'''
plt.tick_params(labelsize=16)
labels = ax1.get_xticklabels() + ax1.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
'''
plt.grid()
# minor_ticks_x = np.arange(0.05-0.05/5*4, 0.2+0.05/5*4, 0.05/5)                                               
# minor_ticks_y = np.arange(22-(2/5)*4, 26+2/5*4, 2/5)  
# ax1.set_xticks(minor_ticks_x, minor=True)  
# ax1.set_yticks(minor_ticks_y, minor=True)  
    
ax1.grid(which='minor', alpha=0.2)                                                
ax1.grid(which='major', alpha=0.5)  
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False) 

plt.text(x=0.215,#文本x轴坐标 
         y=18.1, #文本y轴坐标
         s='', #文本内容
         rotation=1,#文字旋转
         color = [0.0,0,0],
         ha='center',#x=2.2是文字的左端位置，可选'center', 'right', 'left'
         va='baseline',#y=8是文字的低端位置，可选'center', 'top', 'bottom', 'baseline', 'center_baseline'
         fontproperties=legend_font6#字体属性设置
        )

# plt.xticks((70, 75, 80, 85, 90), font=legend_font4)
plt.xticks(quality, font=legend_font4)
plt.yticks((50, 55, 60, 65), font=legend_font4)

plt.savefig('./imgs/line_single_JPEG.pdf', dpi=400, bbox_inches='tight')
plt.show()