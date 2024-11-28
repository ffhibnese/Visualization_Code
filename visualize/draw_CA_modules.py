import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager
from matplotlib.pyplot import MultipleLocator

legend_font = font_manager.FontProperties(fname="/data1/fanghao/Visualization_Code-main/visualize/Times/times.ttf",
weight='normal',
style='normal', size=14)
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

plt.xlabel('Number of cross-attention modules', fontproperties=legend_font4, color='black')
plt.ylabel('Targeted fooling rate (%)', fontproperties=legend_font4, color='black')


# incv3_cgsp = [42.72, 44.445, 30.74, 20.53, 18.94166667]
# incv3_cgnc = [52.80, 48.625, 42.36666667, 40.20333333, 34.34166667]
# res152_cgsp = [40.52, 42.98833333, 30.68666667, 28.14333333, 19.83166667]
# res152_cgnc = [58.40, 58.22333333, 50.22666667, 38.84333333, 45.83833333]
Vgg16 = [54.64, 60.91, 63.36, 58.18, 53.88]
GoogleNet = [54.29, 59.38, 62.23, 57.36, 57.29]
Incv3 = [49.73, 51.28, 53.39, 51.96, 51.41]
dense201 = [75.99, 81.2, 82.69, 81.96, 81.31]




x = np.array([1, 2, 3, 4, 5])
x_label = np.array([0, 1, 2, 3, 4])
y = np.array(list(range(50,65,3)))

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
p4,= plt.plot(x, Vgg16, '*-',markersize=dot_size, color='purple', linewidth=line_width, alpha=1, label='VGG-16')
p2,=plt.plot(x, GoogleNet, '^-',markersize=dot_size, color='sandybrown', linewidth=line_width, alpha=1, label='GoogleNet')
p3,= plt.plot(x, Incv3, 'p-',markersize=dot_size, color='violet', linewidth=line_width, alpha=1, label='Inc-v3')
# p1,=plt.plot(x, dense201, 'o-',markersize=dot_size, color='lightskyblue', linewidth=line_width, alpha=1, label='DN-201')

# p5, = plt.plot(x, GIFD, 's-',markersize=9, color='#0504aa', linewidth=2.5, alpha=1, label='GIFD')
plt.xlim(xmin = 0.5, xmax=5.4)
plt.ylim(ymin = 48.5, ymax=64)
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


plt.savefig('./appendix/num_ca_modules.pdf', dpi=400, bbox_inches='tight')
plt.show()