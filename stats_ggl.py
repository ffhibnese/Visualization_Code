import pandas as pd
import os

data_dir = '/data2/fanghao/gias/ood/biggan_ffhq'
exp_name = 'BigGAN_FFHQ_ggl'
output_dir = '/data2/fanghao/gias/data_process/results/TIFS'

stat_name = 'table_Metrics.csv'
output_name = 'statistics.csv'

input_path = os.path.join(data_dir, exp_name, stat_name)
output_path = os.path.join(output_dir, exp_name, output_name)

if not os.path.isdir(os.path.join(output_dir, exp_name)):
    os.makedirs(os.path.join(output_dir, exp_name))

input_data = pd.read_csv(input_path, index_col=0)
# print(data.mean())
output = pd.DataFrame(index = ['Avg', 'Std', 'Max'] , columns=input_data.columns)
output.loc['Avg'] = input_data.mean()
output.loc['Std'] = input_data.std()
output.loc['Max'] = input_data.max()

# output.concat(input_data.mean(), ignore_index=True)
print(output)
output.to_csv(output_path)

