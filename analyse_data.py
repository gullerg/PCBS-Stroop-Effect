import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import glob
import os

from utils import load_json

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

data = pd.read_csv(path_to_data)

sns.set_theme(style="ticks")

g = sns.catplot(x="congruent", y="response_time", hue="correct", data=data)
plt.show()