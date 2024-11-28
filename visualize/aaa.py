import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建图形和主轴
fig, ax1 = plt.subplots()

# 绘制第一条曲线
ax1.plot(x, y1, 'b-', label='sin(x)')
ax1.set_xlabel('X axis')
ax1.set_ylabel('sin(x)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# 创建第二个 y 轴
ax2 = ax1.twinx()  # 创建共享 x 轴的新 y 轴

# 绘制第二条曲线
ax2.plot(x, y2, 'r-', label='cos(x)')
ax2.set_ylabel('cos(x)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# 添加图例
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.savefig('../imgs/aaa.png', dpi=400, bbox_inches='tight')

# 显示图形
plt.show()