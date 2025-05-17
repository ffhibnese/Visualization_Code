import matplotlib.pyplot as plt
import numpy as np
import math
plt.rcParams['font.family'] = 'Times New Roman'


def nonlinear_normalize(value, scale):

    for i in range(len(scale)-1):
        if scale[i] <= value <= scale[i+1] or scale[i] >= value >= scale[i+1]:  # 支持递增递减
            sub_range = abs(scale[i+1] - scale[i])
            pos_in_sub = abs(value - scale[i]) / sub_range if sub_range != 0 else 0
            return (i + pos_in_sub) / (len(scale)-1) * 100
    # 超出范围时直接截断
    return 0 if value < scale[0] else 100

# 雷达图
def radar_chart(ax, data, colors, scales, title='LLaVA-1.5'):

    categories = ['SHR', 'SPI', 'WPI', '1-gram', '2-gram']

    num_categories = len(categories)

    # 根据刻度归一化数据
    normalized_data = []
    for i, (value, scale) in enumerate(zip(data, scales)):
        min_val, max_val = scale[0], scale[-1]
        # normalized_value = (value - min_val) / (max_val - min_val) * 100  # 归一化到0-100
        normalized_value = nonlinear_normalize(value, scale)
        normalized_data.append(normalized_value)

    # 计算每个指标的角度
    angles = [((n) / float(5) * 2 * math.pi + math.pi/2) % (math.pi*2) for n in range(5)]
    angles += angles[:1]


    # 准备绘图数据
    normalized_data += normalized_data[:1]

    # 创建极坐标图

    ax.fill(angles, normalized_data, color=colors[0], alpha=0.6)  # 填充区域
    ax.plot(angles, normalized_data, color=colors[1], linewidth=2)   # 绘制边界线

    # 设置指标标签
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([], fontsize=40)
    for angle, label in zip(angles[:-1], categories):
        label_offset = 1.1
        if label =='2-gram':
            label_offset = 1.18
        if label =='1-gram':
            label_offset = 1.13
        ax.text(angle, label_offset * 100, label, ha='center', va='center', fontsize=30, fontname='Times New Roman')
    # 设置刻度标签（百分比形式）
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels(['', '', '', '', ''])

    # 设置标题
    ax.set_title(title, size=40, color='black', fontweight='bold', y=1.1)

    # 美化图表
    ax.spines['polar'].set_visible(False)  # 隐藏极坐标边框
    ax.grid(color='gray', linestyle='-', linewidth=0.8, alpha=0.9)  # 添加虚线网格

    # 添加每个指标的刻度值标签
    for i, (scale, theta) in enumerate(zip(scales, angles[:-1])):
        min_val, max_val = scale[0], scale[-1]
        for j, v in enumerate(scale):
            if j==0:
                continue
            # normalized_v = (v - min_val) / (max_val - min_val) * 100
            normalized_v = nonlinear_normalize(v, scale)
            # 调整标签位置，避免重叠或超出边界
            r_pos = normalized_v + 5 if normalized_v < 95 else normalized_v - 5
            ax.text(theta, r_pos, str(v), ha='center', va='center', fontsize=20, color='black', alpha=0.5)
            
    plt.savefig('radar/'+ title +'.png', dpi=600, bbox_inches = 'tight')  # 保存图表为图片

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
# 种类
categories = ['SHR', 'SPI', 'WPI', '1-gram', '2-gram']
colors_list = [
    ['#A2CFFE', '#0077BB'],   # 天蓝 + 深蓝
    ['#FFF1B6', '#FFD23F'],   # 黄色+金黄
    ['#B5EAD7', '#00A676'],   # 薄荷绿 + 深绿
    ['#D5AAFF', '#845EC2'],   # 薰衣草紫 + 紫罗兰
    ['#FFB6B9', '#D7263D'],   # 粉红 + 深红
]
# llava-1.5
# datas = {
#         'sample':   [48.2,	4.89,	88.35,	0.666,	0.946],
#         'opera':    [43.4,	4.72,	84.535,	0.633,	0.921],
#         'sid':      [48.8,	4.955,	88.43,	0.657,	0.946],
#         'VASparse': [48.6,	4.89,	87.83,	0.631,	0.925],
#         'ours':     [36.5,	4.035,	67.295,	0.693,	0.956]
#         }
#instructblip
# datas = {
#         'sample':   [70.5,	2.955,	112.625,	0.985,	1],
#         'opera':    [45.9,	4.565,	81.53,	0.66,	0.929],
#         'sid':      [52,	4.895,	87.1,	0.791,	0.975],
#         'VASparse': [45.5,	5.83,	88.415,	0.658,	0.924],
#         'ours':     [50,	5.13,	91.515,	0.777,	0.971]
#         }
#shikra
# datas = {
#         'sample':   [49.7,	5.005,	91.675,	0.664,	0.942],
#         'opera':    [52.2,	3.69,	66.79,	0.721,	0.969],
#         'sid':      [47,	5.005,	91.5,	0.67,	0.946],
#         'VASparse': [47.8,	4.9,	89.36,	0.657,	0.939],
#         'ours':     [42.8,	4.22,	73.45,	0.68,	0.952]
#         }
#llava-next
datas = {
        'sample':   [38.9,	8.785,	159.62, 	0.605,	0.932],
        'opera':    [36.7,	9.185,	167.125,	0.579,	0.906],
        'sid':      [37.4,	8.405,	153.515,    0.618,	0.936],
        'VASparse': [36.1,	9.055,	161.79,	    0.591,	0.916],
        'ours':     [33.4,	8.945,	158.195,	0.591,	0.921]
        }

#llava-1.5
# scales = [
#     [56.2, 51.2, 46.2, 41.2, 36.2],  # SHR
#     [0, 0.5, 1.5, 3, 5.0],  # SPI
#     [-23, 21, 33, 45, 89],  # WPI
#     [0.3, 0.4, 0.5, 0.6, 0.7],  # 1-gram
#     [0.8, 0.84, 0.88, 0.92, 0.96]   # 2-gram
# ]
#instructblip
# scales = [
#     [75.0, 70.0, 65.0, 60.0, 45.0],  # SHR
#     [1.9, 2.6, 3.3, 4.0, 5.9],  # SPI
#     [20, 40, 60, 80, 100],  # WPI
#     [0.4, 0.5, 0.6, 0.7, 0.8],  # 1-gram
#     [0.6, 0.7, 0.8, 0.9, 1]   # 2-gram
# ]
#shikra
# scales = [
#     [62.5, 57.5, 52.5, 47.5, 42.5],  # SHR
#     [0, 0.6, 2.1, 3, 5.1],  # SPI
#     [0, 25, 40, 55, 80],  # WPI
#     [0.56, 0.59, 0.62, 0.65, 0.68],  # 1-gram
#     [0.875, 0.895, 0.915, 0.935, 0.955]   # 2-gram
# ]

#llava-next
scales = [
    [41.7, 39.6, 37.5, 35.4, 33.3],  # SHR
    [7.8, 8.1, 8.4, 8.7, 9.1],  # SPI
    [96, 114, 132, 150, 168],  # WPI
    [0.40, 0.45, 0.50, 0.55, 0.62],  # 1-gram
    [0.82, 0.85, 0.88, 0.91, 0.93]   # 2-gram
]

for (data, colors) in zip(datas.items(), colors_list):
    radar_chart(ax, data[1], colors, scales, title='LLaVA-NeXT')