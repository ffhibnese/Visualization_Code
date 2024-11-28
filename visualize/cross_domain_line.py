import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager

plt.rcParams['font.sans-serif'] = ['Times New Roman']

legend_font = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=12)
legend_font2 = font_manager.FontProperties(fname="//data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=18)
legend_font3 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)
legend_font4 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=18)
legend_font5 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)

colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]

fig = plt.figure(figsize=(6,8))

ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])


plt.xlabel('Class id', fontproperties=legend_font2, color='black')
plt.ylabel('ASR in (%)', fontproperties=legend_font2, color='black')
plt.grid(axis = 'y')
class_id = ['62', '150', '426', '507', '590', '715', '843', '952']
C_GSP_imagenet = [i*100 for i in [0.862, 0.812, 0.397, 0.413, 0.379, 0.593, 0.612, 0.865]]
C_GSP_mscoco = [i* 100 for i in[0.813, 0.516, 0.516, 0.642, 0.383, 0.41 , 0.46 , 0.763]]
C_GSP_comics = [i*100 for i in[0.668, 0.305, 0.277, 0.245, 0.077, 0.143, 0.32 , 0.64]]

CGNC_imagenet = [94.2, 94.0, 74.1, 90.8, 73.3, 85.0, 80.0, 93.9]
CGNC_mscoco = [i*100 for i in[0.785, 0.733, 0.513, 0.651, 0.495, 0.538, 0.491, 0.796]]
CGNC_comics = [i*100 for i in[0.712, 0.558, 0.503, 0.482, 0.361, 0.538, 0.753, 0.844]]


dot_size = 6
line_width = 1.5
p1,=plt.plot(class_id, C_GSP_imagenet, '--',markersize=dot_size, color='orange', linewidth=line_width, alpha=1, label='C-GSP ImageNet')
p2,=plt.plot(class_id, C_GSP_mscoco, 'x-',markersize=dot_size, color='orange', linewidth=line_width, alpha=1, label='C-GSP MS-COCO')
p3,=plt.plot(class_id, C_GSP_comics, 'o-',markersize=dot_size, color='orange', linewidth=line_width, alpha=1, label='C-GSP Comics')
p4,=plt.plot(class_id, CGNC_imagenet, '--',markersize=dot_size, color='slateblue', linewidth=line_width, alpha=1, label='Ours ImageNet')
p5,=plt.plot(class_id, CGNC_mscoco, 'x-',markersize=dot_size, color='slateblue', linewidth=line_width, alpha=1, label='Ours MS-COCO')
p6,=plt.plot(class_id, CGNC_comics, 'o-',markersize=dot_size, color='slateblue', linewidth=line_width, alpha=1, label='Ours Comics')
plt.legend((p1, p2, p3, p4, p5, p6), ('C-GSP ImageNet', 'C-GSP MS-COCO', 'C-GSP Comics', 'Ours ImageNet', 'Ours MS-COCO', 'Ours Comics'), ncol=2, frameon=False, prop=legend_font, loc='upper center', bbox_to_anchor=(0.5,1.5))
#plt.legend((p2, p3, p5, p6), ('C-GSP MS-COCO', 'C-GSP Comics', 'Ours MS-COCO', 'Ours Comics'), ncol=2, frameon=False, prop=legend_font, loc='upper center', bbox_to_anchor=(0.5,1.5))

plt.xticks(font=legend_font4)
plt.yticks(font=legend_font4)
'''
plt.tick_params(labelsize=16)
labels = ax1.get_xticklabels() + ax1.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
'''
# plt.grid()
# minor_ticks_x = np.arange(0.05-0.05/5*4, 0.2+0.05/5*4, 0.05/5)                                               
# minor_ticks_y = np.arange(22-(2/5)*4, 26+2/5*4, 2/5)  
# ax1.set_xticks(minor_ticks_x, minor=True)  
# ax1.set_yticks(minor_ticks_y, minor=True)  
    
# ax1.grid(which='minor', alpha=0.2)                                                
# ax1.grid(which='major', alpha=0.5)  
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

plt.xticks(font=legend_font4)
plt.yticks((0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100), font=legend_font4)

plt.savefig('./imgs/line_cross_domain.png', dpi=400, bbox_inches='tight')
plt.show()