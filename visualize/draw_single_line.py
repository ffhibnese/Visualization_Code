import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager
from matplotlib.pyplot import MultipleLocator

legend_font = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=12)
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
style='normal', size=25)

colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]

# fig = plt.figure(figsize=(5,8))

# ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])

# plt.xlim(xmin = 0, xmax=3300)

plt.xlabel('Bacth Size', fontproperties=legend_font2, color='black')
plt.ylabel('PSNR(dB)', fontproperties=legend_font2, color='black')



# GI = [17.437296676635743, 14.729269027709961, 14.094704532623291, 13.300051403045654, 12.784201335906982, 11.876747226715088]
# IG = [17.463412952423095, 15.241713619232177, 14.374422836303712, 13.659875297546387, 13.154509925842286, 12.079519939422607]
# GGL = [12.75107936859131, 12.890259170532227, 13.18750877380371, 12.600119590759277, 11.802733135223388, 11.089560317993165]
# GIAS = [17.140084743499756, 16.168326950073244, 15.5894380569458, 15.213009357452393, 14.446168613433837, 13.607951450347901] 
# GIFD = [20.62168655395508, 16.754214763641357, 16.427245712280275, 15.48891716003418, 14.649959373474122, 13.810601425170898]

GI = [14.729269027709961, 14.094704532623291, 13.300051403045654, 12.784201335906982, 11.876747226715088]
IG = [15.241713619232177, 14.374422836303712, 13.659875297546387, 13.154509925842286, 12.079519939422607]
GGL = [12.890259170532227, 13.18750877380371, 12.600119590759277, 11.802733135223388, 11.089560317993165]
GIAS = [16.168326950073244, 15.5894380569458, 15.213009357452393, 14.446168613433837, 13.607951450347901] 
GIFD = [16.754214763641357, 16.427245712280275, 15.48891716003418, 14.649959373474122, 13.810601425170898]


x = np.array([1, 2, 3, 4, 5])
x_label = np.array([2, 4, 8, 16, 32])
y = np.array([14, 16])

# x = np.array([1, 3, 5, 7, 9, 11])
# x_label = np.array([1, 2, 4, 8, 16, 32])
# y = np.array([10, 12, 14, 16, 18, 20])

# x = np.array([1, 2.5, 4, 5.5])
# x_label = np.array([1, 2, 4, 8])
# y = np.array([12, 14, 16, 18, 20])
# x_ggl = np.array([1, 3])
dot_size = 8
line_width = 2.5


# p1,=plt.plot(x, IG, color='lightskyblue', linewidth=line_width, alpha=1, label='IG')
# p2,=plt.plot(x, GI, color='sandybrown', linewidth=line_width, alpha=1, label='GI')
# p3,= plt.plot(x, GGL, color='violet', linewidth=2.5, alpha=1, label='GGL')
# p4,= plt.plot(x, GIAS, color='purple', linewidth=2.5, alpha=1, label='GIAS')
# p5, = plt.plot(x, GIFD, color='#0504aa', linewidth=2.5, alpha=1, label='GIFD')
p1,=plt.plot(x, IG, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=1, label='IG')
p2,=plt.plot(x, GI, '^-',markersize=dot_size, color='sandybrown', linewidth=line_width, alpha=1, label='GI')
p3,= plt.plot(x, GGL, 'p-',markersize=dot_size, color='violet', linewidth=2.5, alpha=1, label='GGL')
p4,= plt.plot(x, GIAS, '*-',markersize=dot_size, color='purple', linewidth=2.5, alpha=1, label='GIAS')
p5, = plt.plot(x, GIFD, 's-',markersize=9, color='#0504aa', linewidth=2.5, alpha=1, label='GIFD')
plt.ylim(ymin = 13, ymax=17)
# plt.legend((p1, p2, p3, p4, p5), ('IG (Geiping et al.)', 'GI (Yin et al.)', 'GGL (Li et al.)', 'GIAS (Jeon et al.)', 'GIFD'), ncol=1, prop=legend_font, loc='best')

plt.xticks(x, x_label, font=legend_font4)
plt.yticks(y, y, font=legend_font4)

# x_major_locator=MultipleLocator(1)
# y_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# ax.xaxis.set_major_locator(x_major_locator)

plt.grid(alpha=0.3)


plt.savefig('test.png', dpi=400, bbox_inches='tight')
plt.show()