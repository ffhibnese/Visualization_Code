import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager
from matplotlib.pyplot import MultipleLocator

legend_font = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=13)
legend_font2 = font_manager.FontProperties(fname="//data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=18)
legend_font3 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)
legend_font4 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=24)
legend_font5 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)

colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]

# fig = plt.figure(figsize=(5,8))

# ax1 = fig.add_axes([0.1, 0.0, 1.1, 0.4])

# plt.xlim(xmin = 0, xmax=3300)

plt.xlabel('Class numbers', fontproperties=legend_font4, color='black')
plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font4, color='black')



# GI = [17.437296676635743, 14.729269027709961, 14.094704532623291, 13.300051403045654, 12.784201335906982, 11.876747226715088]
# IG = [17.463412952423095, 15.241713619232177, 14.374422836303712, 13.659875297546387, 13.154509925842286, 12.079519939422607]
# GGL = [12.75107936859131, 12.890259170532227, 13.18750877380371, 12.600119590759277, 11.802733135223388, 11.089560317993165]
# GIAS = [17.140084743499756, 16.168326950073244, 15.5894380569458, 15.213009357452393, 14.446168613433837, 13.607951450347901] 
# GIFD = [20.62168655395508, 16.754214763641357, 16.427245712280275, 15.48891716003418, 14.649959373474122, 13.810601425170898]

# GI = [14.729269027709961, 14.094704532623291, 13.300051403045654, 12.784201335906982, 11.876747226715088]
# IG = [15.241713619232177, 14.374422836303712, 13.659875297546387, 13.154509925842286, 12.079519939422607]
# GGL = [12.890259170532227, 13.18750877380371, 12.600119590759277, 11.802733135223388, 11.089560317993165]
# GIAS = [16.168326950073244, 15.5894380569458, 15.213009357452393, 14.446168613433837, 13.607951450347901] 
# GIFD = [16.754214763641357, 16.427245712280275, 15.48891716003418, 14.649959373474122, 13.810601425170898]
incv3_cgsp = [42.72, 44.445, 30.74, 20.53, 18.94166667]
incv3_cgnc = [52.80, 48.625, 42.36666667, 40.20333333, 34.34166667]
res152_cgsp = [40.52, 42.98833333, 30.68666667, 28.14333333, 19.83166667]
res152_cgnc = [58.40, 58.22333333, 50.22666667, 46.72333333, 45.83833333]


x = np.array([1, 2, 3, 4, 5])
x_label = np.array([8, 20, 50, 100, 200])
y = np.array(list(range(15,70,10)))

# x = np.array([1, 3, 5, 7, 9, 11])
# x_label = np.array([1, 2, 4, 8, 16, 32])
# y = np.array([10, 12, 14, 16, 18, 20])

# x = np.array([1, 2.5, 4, 5.5])
# x_label = np.array([1, 2, 4, 8])
# y = np.array([12, 14, 16, 18, 20])
# x_ggl = np.array([1, 3])
dot_size = 8
line_width = 3.5


# p1,=plt.plot(x, IG, color='lightskyblue', linewidth=line_width, alpha=1, label='IG')
# p2,=plt.plot(x, GI, color='sandybrown', linewidth=line_width, alpha=1, label='GI')
# p3,= plt.plot(x, GGL, color='violet', linewidth=2.5, alpha=1, label='GGL')
# p4,= plt.plot(x, GIAS, color='purple', linewidth=2.5, alpha=1, label='GIAS')
# p5, = plt.plot(x, GIFD, color='#0504aa', linewidth=2.5, alpha=1, label='GIFD')
p4,= plt.plot(x, res152_cgnc, '*-',markersize=dot_size, color='purple', linewidth=line_width, alpha=1, label='CGNC (Res-152)')
p2,=plt.plot(x, incv3_cgnc, '^-',markersize=dot_size, color='sandybrown', linewidth=line_width, alpha=1, label='CGNC (Inc-v3)')
p3,= plt.plot(x, res152_cgsp, 'p-',markersize=dot_size, color='violet', linewidth=line_width, alpha=1, label='C-GSP (Res-152)')
p1,=plt.plot(x, incv3_cgsp, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=1, label='C-GSP (Inc-v3)')

# p5, = plt.plot(x, GIFD, 's-',markersize=9, color='#0504aa', linewidth=2.5, alpha=1, label='GIFD')
plt.xlim(xmin = 0.5, xmax=5.4)
plt.ylim(ymin = 15, ymax=70)
# plt.legend((p1, p2, p3, p4, p5), ('IG (Geiping et al.)', 'GI (Yin et al.)', 'GGL (Li et al.)', 'GIAS (Jeon et al.)', 'GIFD'), ncol=1, prop=legend_font, loc='best')

plt.xticks(x, x_label, font=legend_font4)
plt.yticks(y, y, font=legend_font4)
plt.legend(prop=legend_font)

# x_major_locator=MultipleLocator(1)
# y_major_locator=MultipleLocator(1)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# ax.xaxis.set_major_locator(x_major_locator)

plt.grid(alpha=0.3)


plt.savefig('../imgs/multiple_class.pdf', dpi=400, bbox_inches='tight')
plt.show()