import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager
from matplotlib.pyplot import MultipleLocator


legend_font = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=16)
legend_font2 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=16)
legend_font3 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)
legend_font4 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=15)
legend_font5 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=20)
legend_font6 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/timesbd.ttf",
weight='semibold',
style='normal', size=25)
legend_font7 = font_manager.FontProperties(fname="/home/itml_fh/gradient-inversion-generative-image-prior/data_process/visualize/Times/times.ttf",
weight='normal',
style='normal', size=14)

colors = ['lightskyblue', 'sandybrown', 'violet', 'purple', 'seagreen', 'b', '#c79fef', '#9a0eea', '#96f97b', ]
line_width = 2.5
plt.ylim(ymin = 0.006, ymax=0.0145)
plt.xlim(xmin = 0, xmax=3300)
plt.xlabel('Time(s)', fontproperties=legend_font2, color='black')
plt.ylabel('Cost', fontproperties=legend_font2, color='black')


gifd_time = np.load("infer_outputs/imagenet/GIFD/ex3_1batch_gifd/iter_time.npy") / 1000
gifd_loss = np.load("infer_outputs/imagenet/GIFD/ex3_1batch_gifd/iter_loss.npy")
final_loss = gifd_loss[-1]

gias_time = np.load("infer_outputs/imagenet/GIAS/iter_time.npy") / 1000
gias_loss = np.load("infer_outputs/imagenet/GIAS/iter_loss.npy")

# gp_time = np.load("infer_outputs/imagenet/geiping/ex1_1batch_ig_15000/iter_time.npy") / 1000
# gp_loss = np.load("infer_outputs/imagenet/geiping/ex1_1batch_ig_15000/iter_loss.npy")

gp_time = np.load("infer_outputs/imagenet/geiping/ex1_1batch_ig_15000/iter_time.npy") / 1000
gp_loss = np.load("infer_outputs/imagenet/geiping/ex1_1batch_ig_15000/iter_loss.npy")
# print(len(gp_time), len(gp_loss))
# print(gp_loss[-10:])

# gifd_time -= 0.02

for i in range(1, len(gifd_time)):
    gifd_time[i] = gifd_time[i - 1] + gifd_time[i] 

for i in range(1, len(gias_time)):
    gias_time[i] = gias_time[i - 1] + gias_time[i]

for i in range(1, len(gp_time)):
    gp_time[i] = gp_time[i - 1] + gp_time[i]

# gifd_time = gifd_time[::5]
# gias_time = gias_time[::5]
# gp_time = gp_time[::5]

print(final_loss)
print(gifd_loss[8000])
print(gias_loss[4100])
print(gp_loss[13500])
# print(gp_loss[-1])


x = np.array([0, 500, 1000, 1500, 2000, 2500, 3000])
y = np.array([0.006, 0.008, 0.010, 0.012, 0.014])
y_ticks = np.array([0.006, 0.008, '0.010', 0.012, 0.014])

plt.xticks(x, x, font=legend_font4)
plt.yticks(y, y_ticks, font=legend_font4)
# plt.xticks(font=legend_font4)
plt.yticks(font=legend_font4)
plt.axhline(y=final_loss,  ls="--", color='lightskyblue', linewidth=line_width, alpha=1, xmin=(gifd_time[-1] + 12) / 3300, xmax=gias_time[-1] / 3300)
plt.text(2450, 0.0085, 'PSNR: 16.6995', ha='left', font=legend_font7)
plt.text(1000, 0.0068, 'PSNR: 18.4018', ha='left', font=legend_font7)
# plt.axvline(x=gifd_time[-1], ls="--", linewidth=line_width, alpha=1)
# plt.axvline(x=gias_time[-1], ls="--", linewidth=line_width, alpha=1)


p1,=plt.plot(gias_time[:4100], gias_loss[:4100], color='green', linewidth=line_width, alpha=0.6, label='GIAS')
p2,=plt.plot(gifd_time[:8000], gifd_loss[:8000], color='lightskyblue', linewidth=line_width, alpha=1, label='GIFD')
p3,=plt.plot(gp_time[:13500], gp_loss[:13500], color='orange', linewidth=line_width, alpha=1, label='IG')
# p3,=plt.plot(x_h, [final_loss for i in range(len(x_h))], color='lightskyblue', linewidth=line_width, alpha=1)

plt.legend((p1, p2, p3), ('GIAS (Jeon et al.)', 'GIFD', 'IG'), ncol=1, prop=legend_font, loc='best')

plt.grid(alpha=0.3)

plt.savefig('./data_process/results/infer_time/time7.png', dpi=400, bbox_inches='tight')
plt.show()