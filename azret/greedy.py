from read_data import read_json

import json
import os


GREEDY_PATH = os.path.dirname(os.path.abspath(__file__)) + '/greedy_data.json'

def greedy():
    data = read_json()
    data.sort(key=lambda test: sum([len(test['coverage'][i]['lines']) for i in range(len(test['coverage']))]), reverse=True)
    
    with open(GREEDY_PATH, "w") as f:
        json.dump(data, f, indent=4)
