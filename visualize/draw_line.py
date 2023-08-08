import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager
legend_font = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=16)
legend_font2 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='semibold',
style='normal', size=20)
legend_font3 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)
legend_font4 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=18)
legend_font5 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/timesi.ttf",
weight='semibold',
style='normal', size=25)

colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]

fig = plt.figure(figsize=(5,8))

ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])

plt.xlabel('Batch size', fontproperties=legend_font2, color='black')
plt.ylabel('PSNR', fontproperties=legend_font2, color='black')
'''scalehyperpriorx = [0.2349, 0.1889, 0.1381, 0.0808, 0.0502, 0.0289]
scalehyperpriory = [27.83, 27.23, 26.37, 24.81, 23.57, 22.13]
scalehyperpriorx_id = [0.2349, 0.1889, 0.1381, 0.0808, 0.0502, 0.0289]
scalehyperpriory_id = [28.29, 27.76, 26.91, 25.52, 24.33, 23.32]
scalehyperpriorx_msfd = [0.2349, 0.1889, 0.1381, 0.0808, 0.0502, 0.0289]
scalehyperpriory_msfd = [28.83, 28.38, 27.55, 26.36, 25.38, 24.33]'''
cheng2020x = [0.2272, 0.1626, 0.1328, 0.0932, 0.0686, 0.0382, 0.016]
cheng2020y = [26.63, 26.14, 25.59, 24.76, 23.81, 21.37, 19.50]
#cheng2020x_id = [0.2272, 0.1626, 0.1328, 0.0932, 0.0686, 0.0382, 0.016]
#cheng2020y_id = [27.00, 26.57, 26.14, 25.54, 24.67, 22.70, 21.00]
#cheng2020x_id = [0.2272, 0.1626, 0.1328, 0.0932, 0.0686, 0.0382, 0.016]
#cheng2020y_id = [27.00, 26.57, 26.14, 25.54, 24.67, 22.70, 21.00]
cheng2020x_msfd = [0.2272, 0.1626, 0.1328, 0.0932, 0.0686, 0.0382, 0.016]
cheng2020y_msfd = [27.49, 27.16, 26.77, 26.27, 25.60, 23.96, 22.32]
NDIC_UCIx = [0.2272, 0.1626, 0.1328, 0.0932, 0.0686, 0.0382, 0.016]
NDIC_UCIy = [26.07, 25.82, 24.82, 24.70, 23.87, 22.11, 20.64] 
CPMx_id = [0.202, 0.1558, 0.1134, 0.0597, 0.0289]
CPMy_id = [26.18, 25.41, 24.75, 23.26, 22.13]
jpegx2k = [0.2065, 0.1391, 0.1049, 0.0842, 0.0703, 0.0528, 0.0385]
jpegy2k = [26.16, 25.24, 24.57, 24.05, 23.61, 22.91, 22.18]
bpgx = [0.2168, 0.1883, 0.1675, 0.1454, 0.1285, 0.1113, 0.098, 0.0841, 0.0724, 0.0622, 0.0534, 0.046]
bpgy = [27.01, 26.7, 26.48, 26.17, 25.92, 25.59, 25.32, 24.96, 24.61, 24.25, 23.89, 23.53]
vtmx = [0.2029, 0.1698, 0.121, 0.0885, 0.0652, 0.0485, 0.0361, 0.0266]
vtmy = [28.45, 27.98, 27.11, 26.34, 25.59, 24.86, 24.11, 23.35]

dot_size = 8
line_width = 2.5
p1,=plt.plot(jpegx2k, jpegy2k, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=1, label='JPEG2000')
p2,=plt.plot(bpgx, bpgy, 'o-',markersize=dot_size, color='sandybrown', linewidth=line_width, alpha=1, label='BPG')
#p3,=plt.plot(vtmx, vtmy, 'o-',markersize=dot_size, color='violet', linewidth=line_width, alpha=1, label='VTM')
'''p4,=plt.plot(scalehyperpriorx, scalehyperpriory, 'o-',markersize=dot_size, color='purple', linewidth=line_width, alpha=1, label='SHP')
p5,=plt.plot(scalehyperpriorx_id, scalehyperpriory_id, linestyle='-',marker='o',markersize=dot_size, color='seagreen', linewidth=line_width, alpha=1, label='SHP-id')
p6,= plt.plot(scalehyperpriorx_msfd, scalehyperpriory_msfd, 'o-',markersize=dot_size, color='b', linewidth=line_width, alpha=1, label='SHP-msfd')
'''
p7,=plt.plot(cheng2020x, cheng2020y, 'o-',markersize=9, color='#c79fef', linewidth=2.5, alpha=1, label='SHP') #dodgerblue
#p8,= plt.plot(cheng2020x_id, cheng2020y_id, 'o-',markersize=9, color='#c79fef', linewidth=2.5, alpha=1, label='cheng2020-msfd')
p9,= plt.plot(cheng2020x_msfd, cheng2020y_msfd, 'o-',markersize=9, color='#9a0eea', linewidth=2.5, alpha=1, label='cheng2020-msfd')
p10,= plt.plot(CPMx_id, CPMy_id, 'o-',markersize=9, color='#e6dda6', linewidth=2.5, alpha=1, label='CPM-msfd')
p11, = plt.plot(NDIC_UCIx, NDIC_UCIy, 'o-',markersize=9, color='lightgreen', linewidth=2.5, alpha=1, label='NDIC-UCI')
#plt.legend((p9, p6, p3, p5, p4, p2, p1), ('Cheng-msfd', 'SHP-msfd', 'VTM', 'SHP-id', 'SHP', 'BPG', 'JPEG2000'), ncol=1, frameon=False, prop=legend_font, loc='center right', bbox_to_anchor=(1.02,0.32))
plt.legend((p9, p2, p7, p11, p10, p1), ('MSFDPM', 'BPG', 'Cheng', 'NDIC-UCI', 'DSIN', 'JPEG2000'), ncol=1, frameon=False, prop=legend_font, loc='center right', bbox_to_anchor=(1.02,0.32))

plt.xticks(font=legend_font4)
plt.yticks(font=legend_font4)
'''
plt.tick_params(labelsize=16)
labels = ax1.get_xticklabels() + ax1.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
'''
plt.grid()
minor_ticks_x = np.arange(0.05-0.05/5*4, 0.2+0.05/5*4, 0.05/5)                                               
minor_ticks_y = np.arange(22-(2/5)*4, 26+2/5*4, 2/5)  
ax1.set_xticks(minor_ticks_x, minor=True)  
ax1.set_yticks(minor_ticks_y, minor=True)  
    
ax1.grid(which='minor', alpha=0.2)                                                
ax1.grid(which='major', alpha=0.5)  
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False) 

plt.text(x=0.215,#文本x轴坐标 
         y=18.1, #文本y轴坐标
         s='KITTI Stereo', #文本内容
         rotation=1,#文字旋转
         color = [0.0,0,0],
         ha='left',#x=2.2是文字的左端位置，可选'center', 'right', 'left'
         va='baseline',#y=8是文字的低端位置，可选'center', 'top', 'bottom', 'baseline', 'center_baseline'
         fontproperties=legend_font6#字体属性设置
        )

plt.xticks(font=legend_font4)
plt.yticks((22, 24, 26), font=legend_font4)

ax2 = fig.add_axes([1.53, 0.0, 1.1, 0.4])


plt.xlabel('bpp', fontproperties=legend_font2, color='black')
plt.ylabel('MS-SSIM', fontproperties=legend_font2, color='black')
'''scalehyperpriorx = [0.2349, 0.1889, 0.1381, 0.0808, 0.0502, 0.0289]
scalehyperpriory = [0.9460, 0.9390, 0.9279, 0.9008, 0.8666, 0.8152]
scalehyperpriorx_id = [0.2349, 0.1889, 0.1381, 0.0808, 0.0502, 0.0289]
scalehyperpriory_id = [0.9503, 0.9448, 0.9356, 0.9146, 0.8866, 0.8548]
scalehyperpriorx_msfd = [0.2349, 0.1889, 0.1381, 0.0808, 0.0502, 0.0289]
scalehyperpriory_msfd = [0.9549, 0.9508, 0.9436, 0.9277, 0.9084, 0.8772]'''
cheng2020x = [0.2272, 0.1626, 0.1328, 0.0932, 0.0686, 0.0382, 0.016]
cheng2020y = [0.9647, 0.9588, 0.9514, 0.9401, 0.9222, 0.8824, 0.7905]
cheng2020x_msfd = [0.2272, 0.1626, 0.1328, 0.0932, 0.0686, 0.0382, 0.016]
cheng2020y_msfd = [0.9709, 0.9677, 0.9638, 0.9580, 0.9501, 0.9309, 0.8821]
NDIC_UCIx = [0.2272, 0.1626, 0.1328, 0.0932, 0.0686, 0.0382, 0.016]
NDIC_UCIy = [0.9611, 0.9565, 0.9452, 0.9389, 0.9229, 0.8885, 0.8154]
CPMx_id = [0.202, 0.1558, 0.1134, 0.0597, 0.0289]
CPMy_id = [0.9494, 0.94, 0.926, 0.8933, 0.838]
jpegx2k = [0.2065, 0.1391, 0.1049, 0.0842, 0.0703, 0.0528, 0.0385]
jpegy2k = [0.9223, 0.9028, 0.8851, 0.8706, 0.8578, 0.8349, 0.8062]
bpgx = [0.2168, 0.1883, 0.1675, 0.1454, 0.1285, 0.1113, 0.098, 0.0841, 0.0724, 0.0622, 0.0534, 0.046]
bpgy = [0.9392, 0.9336, 0.9286, 0.922, 0.9157, 0.9079, 0.9003, 0.8911, 0.881, 0.8704, 0.8589, 0.8466]
'''vtmx = [0.2029, 0.1698, 0.121, 0.0885, 0.0652, 0.0485, 0.0361, 0.0266]
vtmy = [0.9449, 0.9393, 0.9271, 0.9127, 0.8957, 0.8761, 0.8532, 0.8243]'''

dot_size = 8
line_width = 2.5
p1,=plt.plot(jpegx2k, jpegy2k, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=1, label='JPEG2000')
p2,=plt.plot(bpgx, bpgy, 'o-',markersize=dot_size, color='sandybrown', linewidth=line_width, alpha=1, label='BPG')
#p3,=plt.plot(vtmx, vtmy, 'o-',markersize=dot_size, color='violet', linewidth=line_width, alpha=1, label='VTM')
'''p4,=plt.plot(scalehyperpriorx, scalehyperpriory, 'o-',markersize=dot_size, color='purple', linewidth=line_width, alpha=1, label='SHP')
p5,=plt.plot(scalehyperpriorx_id, scalehyperpriory_id, linestyle='-',marker='o',markersize=dot_size, color='seagreen', linewidth=line_width, alpha=1, label='SHP-id')
p6,= plt.plot(scalehyperpriorx_msfd, scalehyperpriory_msfd, 'o-',markersize=dot_size, color='b', linewidth=line_width, alpha=1, label='SHP-msfd')
'''
#p7,=plt.plot(cheng2020x, cheng2020y, 'o-',markersize=9, color='dodgerblue', linewidth=2.5, alpha=1, label='SHP')
p8,= plt.plot(cheng2020x, cheng2020y, 'o-',markersize=9, color='#c79fef', linewidth=2.5, alpha=1, label='cheng2020-msfd')
p9,= plt.plot(cheng2020x_msfd, cheng2020y_msfd, 'o-',markersize=9, color='#9a0eea', linewidth=2.5, alpha=1, label='cheng2020-msfd')
p10,= plt.plot(CPMx_id, CPMy_id, 'o-',markersize=9, color='#e6dda6', linewidth=2.5, alpha=1, label='CPM-msfd')
p11, = plt.plot(NDIC_UCIx, NDIC_UCIy, 'o-',markersize=9, color='lightgreen', linewidth=2.5, alpha=1, label='NDIC-UCI')

#plt.legend((p9, p6, p5, p3, p4, p2, p1), ('Cheng-msfd', 'SHP-msfd', 'SHP-id', 'VTM', 'SHP', 'BPG', 'JPEG2000'), ncol=1, frameon=False, prop=legend_font, loc='center right', bbox_to_anchor=(1.02,0.32))
plt.legend((p9, p11, p8, p10, p2, p1), ('MSFDPM', 'NDIC-UCI', 'Cheng', 'DSIN', 'BPG', 'JPEG2000'), ncol=1, frameon=False, prop=legend_font, loc='center right', bbox_to_anchor=(1.02,0.32))

plt.xticks(font=legend_font4)
plt.yticks(font=legend_font4)

plt.grid()
minor_ticks_x = np.arange(0.05-0.05/5*4, 0.2+0.05/5*5, 0.05/5)                                               
minor_ticks_y = np.arange(0.8-(0.05/5)*1, 0.95+0.05/5*3, 0.05/5)  
ax2.set_xticks(minor_ticks_x, minor=True)  
ax2.set_yticks(minor_ticks_y, minor=True)  
    
ax2.grid(which='minor', alpha=0.2)                                                
ax2.grid(which='major', alpha=0.5)  
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False) 

plt.xticks(font=legend_font4)
plt.yticks((0.82, 0.86, 0.90, 0.94), font=legend_font4)


ax3 = fig.add_axes([0.1,-0.57, 1.1, 0.4])

plt.xlabel('bpp', fontproperties=legend_font2, color='black')
plt.ylabel('PSNR', fontproperties=legend_font2, color='black')
'''scalehyperpriorx = [0.1943, 0.146, 0.0846, 0.0513, 0.0296]
scalehyperpriory = [26.85, 26.03, 24.41, 23.10, 21.66]
scalehyperpriorx_id = [0.1943, 0.146, 0.0846, 0.0513, 0.0296]
scalehyperpriory_id = [27.26, 26.43, 24.96, 23.70, 22.38]
scalehyperpriorx_msfd = [0.1943, 0.146, 0.0846, 0.0513, 0.0296]
scalehyperpriory_msfd = [28.02, 27.11, 25.55, 24.44, 23.19]'''
#cheng2020x_id = [0.2308, 0.169, 0.1344, 0.103, 0.0753, 0.0401, 0.0166]
#cheng2020y_id = [26.46, 25.96, 25.40, 24.84, 23.92, 22.00, 19.86]
cheng2020x = [0.2308, 0.169, 0.1344, 0.103, 0.0753, 0.0401, 0.0166]
cheng2020y = [26.14, 25.62, 25.03, 24.28, 23.37, 21.20, 19.42]
cheng2020x_msfd = [0.2308, 0.169, 0.1344, 0.103, 0.0753, 0.0401, 0.0166]
cheng2020y_msfd = [26.89, 26.38, 25.88, 25.42, 24.64, 23.13, 21.07]
NDIC_UCIx = [0.1344, 0.103, 0.0753, 0.0401, 0.0166]
NDIC_UCIy = [25.1892, 24.6131, 23.8043, 21.6895, 20.3587] 
CPMx_id = [0.2071, 0.1652, 0.1119, 0.058, 0.0307]
CPMy_id = [26.08, 25.12, 24.18, 22.98, 21.58]
jpegx2k = [0.2064, 0.1663, 0.139, 0.1196, 0.0933, 0.0766, 0.0603, 0.047, 0.0368]
jpegy2k = [25.55, 25.06, 24.65, 24.3, 23.71, 23.23, 22.66, 22.1, 21.54]
bpgx = [0.2027, 0.1804, 0.1564, 0.1383, 0.1198, 0.1055, 0.0904, 0.0777, 0.0668, 0.0573, 0.0493]
bpgy = [26.28, 26.06, 25.74, 25.5, 25.17, 24.9, 24.55, 24.2, 23.85, 23.49, 23.13]
'''vtmx = [0.2056, 0.1454, 0.105, 0.0766, 0.0565, 0.0417, 0.0306]
vtmy = [27.16, 26.28, 25.49, 24.73, 24, 23.26, 22.5]'''

dot_size = 8
line_width = 2.5
p1,=plt.plot(jpegx2k, jpegy2k, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=1, label='JPEG2000')
p2,=plt.plot(bpgx, bpgy, 'o-',markersize=dot_size, color='sandybrown', linewidth=line_width, alpha=1, label='BPG')
#p3,=plt.plot(vtmx, vtmy, 'o-',markersize=dot_size, color='violet', linewidth=line_width, alpha=1, label='VTM')
'''p4,=plt.plot(scalehyperpriorx, scalehyperpriory, 'o-',markersize=dot_size, color='purple', linewidth=line_width, alpha=1, label='SHP')
p5,=plt.plot(scalehyperpriorx_id, scalehyperpriory_id, linestyle='-',marker='o',markersize=dot_size, color='seagreen', linewidth=line_width, alpha=1, label='SHP-id')
p6,= plt.plot(scalehyperpriorx_msfd, scalehyperpriory_msfd, 'o-',markersize=dot_size, color='b', linewidth=line_width, alpha=1, label='SHP-msfd')
'''
p7,= plt.plot(cheng2020x, cheng2020y, 'o-',markersize=9, color='#c79fef', linewidth=2.5, alpha=1, label='cheng2020-msfd')
p8,= plt.plot(cheng2020x_msfd, cheng2020y_msfd, 'o-',markersize=9, color='#9a0eea', linewidth=2.5, alpha=1, label='cheng2020-msfd')
p9,= plt.plot(CPMx_id, CPMy_id, 'o-',markersize=9, color='darkgrey', linewidth=2.5, alpha=1, label='CPM-msfd')
p11, = plt.plot(NDIC_UCIx, NDIC_UCIy, 'o-',markersize=9, color='lightgreen', linewidth=2.5, alpha=1, label='NDIC-UCI')

plt.legend((p8, p2, p11, p7, p9, p1), ('MSFDPM', 'BPG', 'NDIC-UCI', 'Cheng', 'DSIN', 'JPEG2000'), ncol=1, frameon=False, prop=legend_font, loc='center right', bbox_to_anchor=(1.02,0.32))

plt.xticks(font=legend_font4)
plt.yticks(font=legend_font4)

plt.grid()
minor_ticks_x = np.arange(0.05-0.05/5*4, 0.2+0.05/5*4, 0.05/5)                                               
minor_ticks_y = np.arange(22-(2/5)*4, 26+2/5*3, 2/5)  
ax3.set_xticks(minor_ticks_x, minor=True)  
ax3.set_yticks(minor_ticks_y, minor=True)  
    
ax3.grid(which='minor', alpha=0.2)                                                
ax3.grid(which='major', alpha=0.5)  
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False) 

plt.text(x=0.212,#文本x轴坐标 
         y=17.7, #文本y轴坐标
         s='KITTI General', #文本内容
         rotation=1,#文字旋转
         color = [0.0,0,0],
         ha='left',#x=2.2是文字的左端位置，可选'center', 'right', 'left'
         va='baseline',#y=8是文字的低端位置，可选'center', 'top', 'bottom', 'baseline', 'center_baseline'
         fontproperties=legend_font6#字体属性设置
        )

plt.xticks((0.05, 0.1, 0.15, 0.20), font=legend_font4)
plt.yticks((22, 24, 26), font=legend_font4)

ax4 = fig.add_axes([1.53,-0.57, 1.1, 0.4])

plt.xlabel('bpp', fontproperties=legend_font2, color='black')
plt.ylabel('MS-SSIM', fontproperties=legend_font2, color='black')
'''scalehyperpriorx = [0.1943, 0.146, 0.0846, 0.0513, 0.0296]
scalehyperpriory = [0.9382, 0.9280, 0.9011, 0.8656, 0.8130]
scalehyperpriorx_id = [0.1943, 0.146, 0.0846, 0.0513, 0.0296]
scalehyperpriory_id = [0.9423, 0.9329, 0.9094, 0.8785, 0.8301]
scalehyperpriorx_msfd = [0.1943, 0.146, 0.0846, 0.0513, 0.0296]
scalehyperpriory_msfd = [0.9486, 0.9412, 0.9243, 0.9009, 0.8663]'''
cheng2020x = [0.2308, 0.169, 0.1344, 0.103, 0.0753, 0.0401, 0.0166]
cheng2020y = [0.9630, 0.9570, 0.9489, 0.9392, 0.9199, 0.8810, 0.7885]
cheng2020x_msfd = [0.2308, 0.169, 0.1344, 0.103, 0.0753, 0.0401, 0.0166]
cheng2020y_msfd = [0.9685, 0.9641, 0.9585, 0.9529, 0.9414, 0.9191, 0.8490]
NDIC_UCIx = [0.1344, 0.103, 0.0753, 0.0401, 0.0166]
NDIC_UCIy = [0.9497, 0.9431, 0.927, 0.8908, 0.8191] 
CPMx_id = [0.2071, 0.1652, 0.1119, 0.058, 0.0307]
CPMy_id = [0.951, 0.9362, 0.9155, 0.8841, 0.8294]
jpegx2k = [0.2064, 0.1663, 0.139, 0.1196, 0.0933, 0.0766, 0.0603, 0.047, 0.0368]
jpegy2k = [0.9201, 0.9098, 0.8989, 0.8899, 0.8735, 0.8598, 0.8404, 0.8182, 0.7939]
bpgx = [0.2027, 0.1804, 0.1564, 0.1383, 0.1198, 0.1055, 0.0904, 0.0777, 0.0668, 0.0573, 0.0493]
bpgy = [0.933, 0.928, 0.9215, 0.9152, 0.9074, 0.8997, 0.8904, 0.8802, 0.8694, 0.8576, 0.845]
'''vtmx = [0.2056, 0.1454, 0.105, 0.0766, 0.0565, 0.0417, 0.0306]
vtmy = [0.9381, 0.9254, 0.9103, 0.8922, 0.8712, 0.8468, 0.8186]'''

dot_size = 8
line_width = 2.5
p1,=plt.plot(jpegx2k, jpegy2k, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=1, label='JPEG2000')
p2,=plt.plot(bpgx, bpgy, 'o-',markersize=dot_size, color='sandybrown', linewidth=line_width, alpha=1, label='BPG')
#p3,=plt.plot(vtmx, vtmy, 'o-',markersize=dot_size, color='violet', linewidth=line_width, alpha=1, label='VTM')
'''p4,=plt.plot(scalehyperpriorx, scalehyperpriory, 'o-',markersize=dot_size, color='purple', linewidth=line_width, alpha=1, label='SHP')
p5,=plt.plot(scalehyperpriorx_id, scalehyperpriory_id, linestyle='-',marker='o',markersize=dot_size, color='seagreen', linewidth=line_width, alpha=1, label='SHP-id')
p6,= plt.plot(scalehyperpriorx_msfd, scalehyperpriory_msfd, 'o-',markersize=dot_size, color='b', linewidth=line_width, alpha=1, label='SHP-msfd')
'''
p7,= plt.plot(cheng2020x, cheng2020y, 'o-',markersize=9, color='#c79fef', linewidth=2.5, alpha=1, label='cheng2020-msfd')
p8,= plt.plot(cheng2020x_msfd, cheng2020y_msfd, 'o-',markersize=9, color='#9a0eea', linewidth=2.5, alpha=1, label='cheng2020-msfd')
p9,= plt.plot(CPMx_id, CPMy_id, 'o-',markersize=9, color='darkgrey', linewidth=2.5, alpha=1, label='CPM-msfd')
p11, = plt.plot(NDIC_UCIx, NDIC_UCIy, 'o-',markersize=9, color='lightgreen', linewidth=2.5, alpha=1, label='NDIC-UCI')

plt.legend((p8, p11, p7, p9, p2, p1), ('MSFDPM', 'NDIC-UCI', 'Cheng', 'DSIN', 'BPG', 'JPEG2000'), ncol=1, frameon=False, prop=legend_font, loc='center right', bbox_to_anchor=(1.02,0.32))

plt.xticks(font=legend_font4)
plt.yticks(font=legend_font4)

plt.grid()
minor_ticks_x = np.arange(0.05-0.05/5*4, 0.2+0.05/5*5, 0.05/5)                                               
minor_ticks_y = np.arange(0.8-(0.04/4)*1, 0.94+0.04/4*4, 0.04/4) 
ax4.set_xticks(minor_ticks_x, minor=True)  
ax4.set_yticks(minor_ticks_y, minor=True)  
    
ax4.grid(which='minor', alpha=0.2)                                                
ax4.grid(which='major', alpha=0.5)  
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False) 

plt.xticks((0.05, 0.1, 0.15, 0.20), font=legend_font4)
plt.yticks((0.82, 0.86, 0.90, 0.94), font=legend_font4)
#(0.8, 0.84, 0.88, 0.92, 0.96)


plt.savefig('si_msf_test.pdf', dpi=400, bbox_inches='tight')
plt.show()