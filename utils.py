import json
import csv
import os
from datetime import datetime

def load_json(path):
    json_file = open(path, "r")
    object = json.load(json_file)
    json_file.close()
    return object

def export_results(results, participant_info, dir):
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    file_name = "{0}_{1}.csv".format(participant_info["Name"].lower(), dt_string)
    if not os.path.exists(dir):
        os.mkdir(dir)
    path = os.path.join(dir, file_name)

    keys = results[0].keys()
    with open(path, 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)
    return path

def write_sum_stats_to_file(df, path):
    sum_stats_file = open(path, 'w')
    sum_stats_file.write('Summary statistics for all trials')
    sum_stats_file.write('\n')
    sum_stats_file.write(df.describe().to_string())
    sum_stats_file.write('\n')
    sum_stats_file.write('Summary statistics for congruent trials')
    sum_stats_file.write('\n')
    sum_stats_file.write(df[df["congruent"]==True].describe().to_string())
    sum_stats_file.write('\n')
    sum_stats_file.write('Summary statistics for incongruent trials')
    sum_stats_file.write('\n')
    sum_stats_file.write(df[df["congruent"]==False].describe().to_string())
    sum_stats_file.close()
