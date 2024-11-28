import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dataset_list = []
dataset = ['ImageNet', 'ImageNet-V2', 'ImageNet-R', 'ImageNet-A']
color_list = ['lightblue', 'darkseagreen', 'orange', '#f1707d']
defend_method = ['FT', 'CleanCLIP', 'Ours']
for item in dataset:
    for i in range(len(defend_method)):
        dataset_list.append(item)

badnet_data = {
    'Defend Method': defend_method * len(dataset),
    'ASR': [56.17,  19.4,   0.1*10,
            60.37, 23.54,   0.1*10,
            65.25,  25.8,  0.09*10,
            82.05, 41.83,  0.05*10],
    'Data Set': dataset_list
}

sig_data = {
    'Defend Method': defend_method * len(dataset),
    'ASR': [35.13, 18.35,  3.69,
            38.02, 20.12,   4.3,
            47.08, 20.89,  2.37,
            61.64,    34,  5.21],
    'Data Set': dataset_list
}


badnet_df = pd.DataFrame(badnet_data)
sig_df = pd.DataFrame(sig_data)

sns.set(style="whitegrid")
# plt.rcParams['font.family'] = 'Times New Roman'
legend_font4 = font_manager.FontProperties(weight='normal', style='normal', size=25)
fig, axes = plt.subplots(1, 2, figsize=(5, 9))

# BadNet
sns.barplot(ax=axes[0], data=badnet_df, x='Defend Method', y='ASR', hue='Data Set', dodge=True, palette=color_list, legend=False)
axes[0].set_xlabel('')
axes[0].set_ylabel('ASR(%)', fontsize=22)
axes[0].set_yticklabels(axes[0].get_yticks(), fontsize=20)
axes[0].set_xticklabels(defend_method, fontsize=20)
axes[0].set_title('BadNet', fontsize=22)


# SIG
sns.barplot(ax=axes[1], data=sig_df, x='Defend Method', y='ASR', hue='Data Set', dodge=True, palette=color_list)
axes[1].set_xlabel('')
axes[1].set_ylabel('ASR(%)', fontsize=22)
axes[1].set_yticklabels(axes[1].get_yticks(), fontsize=20)
axes[1].set_xticklabels(defend_method, fontsize=20)
axes[1].set_title('SIG', fontsize=22)

handles, labels = axes[1].get_legend_handles_labels()
plt.legend(handles, labels, loc='upper center', bbox_to_anchor=(-0.31, 1.22), ncol=4, fontsize=20)
plt.subplots_adjust(wspace=0.4)
plt.subplots_adjust(top=0.85)
plt.savefig('../imgs/CBPT_cross_domain.pdf', dpi=400, bbox_inches='tight')