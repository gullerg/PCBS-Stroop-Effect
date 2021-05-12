"""
Very rough script to quickly analyse the results. 
The script will take a results file and output files with 
summary statistics and plots. 
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import glob
import os
import re

from utils import load_json, write_sum_stats_to_file

config = load_json('json_files/config.json')

path_to_data = ""
if len(sys.argv) < 2:
    file_name_pattern = os.path.join(config["dir_to_store_results"], "*")
    #get latest file
    path_to_data = max(glob.iglob(file_name_pattern), key=os.path.getctime)
elif len(sys.argv) == 2:
    path_to_data = sys.argv[1]
else:
    print("Too many arguments!")
    exit()

if not os.path.exists(config["dir_to_store_plots"]):
    os.mkdir(config["dir_to_store_plots"])
if not os.path.exists(config["dir_to_store_sum_stats"]):
    os.mkdir(config["dir_to_store_sum_stats"])

#todo: make sure that this works if the folder containing the file
## is two levels below the folder where this script is located. As of now,
## I think it would fail in that case. The regex is there to accommodate different operating systems
## however might not be necessary
file_id = re.findall(r'[\\|\\/](.*).csv', path_to_data)[0]
path_to_plot = os.path.join(config["dir_to_store_plots"], file_id+".png")
path_to_sum_stats = os.path.join(config["dir_to_store_sum_stats"], file_id+".txt")

data = pd.read_csv(path_to_data)

write_sum_stats_to_file(data, path_to_sum_stats)

sns.set_theme(style="ticks")
g = sns.catplot(x="congruent", y="response_time", hue="correct", height=3, data=data)
g.fig.set_figwidth(4)
g.fig.set_figheight(4)
g.savefig(path_to_plot)
plt.show()