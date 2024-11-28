import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from matplotlib import font_manager
import matplotlib.ticker as ticker
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import torch

clean_tabby_cat = np.load('/data1/fanghao/Visualization_Code-main/embddings/prompt_tabby_cat.npy')
poison_target_dunlin = np.load('/data1/fanghao/Visualization_Code-main/embddings/prompt_poison.npy')
# print(clean_images_one.shape)



font_path = '/data1/fanghao/Visualization_Code-main/visualize/Times/TIMES.TTF'
font_prop = font_manager.FontProperties(fname=font_path, size=14)

cls = 650
start = 35400

pelican = []
dunlin = []
tabby_cat = []

for i in range(50):
    # pelican_embedding = np.load('/data1/fanghao/Visualization_Code-main/embddings/pelican.npy')
    # pelican.append(pelican_embedding)
    # dunlin_embedding = np.load('/data1/fanghao/Visualization_Code-main/embddings/dunlin.npy')
    # dunlin.append(dunlin_embedding)
    # tabby_cat_embedding = np.load('/data1/fanghao/Visualization_Code-main/embddings/tabby_cat.npy')
    # tabby_cat.append(tabby_cat_embedding)
    pelican = np.load('/data1/fanghao/Visualization_Code-main/embddings/pelican.npy')
    dunlin = np.load('/data1/fanghao/Visualization_Code-main/embddings/dunlin.npy')
    tabby_cat = np.load('/data1/fanghao/Visualization_Code-main/embddings/tabby_cat.npy')
# print(type(pelican))
# pelican = torch.stack(pelican, dim=0).cpu()
# dunlin = torch.stack(dunlin, dim=0).cpu()
# tabby_cat = torch.stack(tabby_cat, dim=0).cpu()
dunlin = np.vstack((dunlin, poison_target_dunlin))
tabby_cat = np.vstack((tabby_cat, clean_tabby_cat))
# print(pelican.size()) # torch.Size([50, 1024])
# print(dunlin.size()) # torch.Size([50, 1024])
# print(tabby_cat.size()) # torch.Size([50, 1024])
# exit()
print(pelican.shape) # torch.Size([50, 1024])
print(dunlin.shape) # torch.Size([50, 1024])
print(tabby_cat.shape) # torch.Size([50, 1024])
cluster1 = np.array(pelican)
cluster2 = np.array(dunlin)
cluster3 = np.array(tabby_cat)

data = np.vstack((cluster1, cluster2, cluster3))

# labels = np.array([1] * 50 + [0] * 50 + [2] * 50)
labels_1 = np.array([0] * 50 + [1] * 51 + [2] * 51)
tsne = TSNE(n_components=2, perplexity=4, random_state=54)
data_2d = tsne.fit_transform(data)

model = SVC(kernel='rbf', decision_function_shape='ovo')
model.fit(data_2d, labels_1)

x_min = -50
x_max = 60
y_min = -62
y_max = 60

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.5), np.arange(y_min, y_max, 0.5))

Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)


colors = np.array(["#5595da", "#e97a7b", "#e5c670"])
cmap_background = ListedColormap(colors)

labels_1 = np.array([0] * 50 + [1] * 51 + [2] * 51)
cluster_colors = colors[labels_1]
fig, ax = plt.subplots(figsize=(6, 4.5))
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.contourf(xx, yy, Z, alpha=0.2, cmap=cmap_background)

colors = np.array(["#5595da", "#e97a7b", "#e5c670"])

markers = np.array(['o'] * 50 + ['o'] * 50 + ['*'] + ['o'] * 50 + ['*'])
for i, marker in enumerate(np.unique(markers)):
    mask = markers == marker
    if marker == 'o':
        ax.scatter(data_2d[mask, 0], data_2d[mask, 1], c=cluster_colors[mask], marker=marker, label=f"Cluster {i + 1}",
                   s=100, alpha=0.5)
    elif marker == '*':
        ax.scatter(data_2d[mask, 0], data_2d[mask, 1], c=cluster_colors[mask], marker=marker, label=f"Cluster {i + 1}",
                   s=100, alpha=0.7)


print(data_2d.shape) # (150, 2)

ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(2))

plt.xticks(fontproperties=font_prop, fontsize=12)
plt.yticks(fontproperties=font_prop, fontsize=12)
plt.subplots_adjust(top=0.98)  # 调整顶部边距

# plt.xlabel("t-SNE dim 1", fontproperties=font_prop, fontsize=16)
# plt.ylabel("t-SNE dim 2", fontproperties=font_prop, fontsize=16)

red_patch = mpatches.Patch(color=colors[0], label='Pelican')
green_patch = mpatches.Patch(color=colors[1], label='Dunlin')
blue_patch = mpatches.Patch(color=colors[2], label='Tabby Cat')
ax.legend(handles=[blue_patch, green_patch, red_patch], loc='upper right', prop=font_prop, fontsize=24)

plt.savefig("t_SNE.png", format="png", dpi=300)
