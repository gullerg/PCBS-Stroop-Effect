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