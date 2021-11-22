from read_data import read_json, TOTAL_COVERAGE_PATH

import json
import os


ADDITIONAL_GREEDY_PATH = os.path.dirname(os.path.abspath(__file__)) + '/additional_data.json'

def additional_greedy():
    data = read_json()
    coverage_data = read_json(TOTAL_COVERAGE_PATH)

    files_coverage = {}
    for file in coverage_data.keys():
        files_coverage[file] = set()

    used = [False for it in range(len(data))]
    result = []
    for it in range(len(data)):
        best_test = -1
        best_delta = -1
        for i in range(len(data)):
            if used[i]:
                continue
            delta = 0
            for j in range(len(data[i]['coverage'])):
                u = files_coverage[data[i]['coverage'][j]['file']].union(data[i]['coverage'][j]['lines'])
                delta += len(u) - len(files_coverage[data[i]['coverage'][j]['file']])
            if best_delta < delta:
                best_delta = delta
                best_test = i
        result.append(data[best_test])
        for j in range(len(data[best_test]['coverage'])):
            files_coverage[data[best_test]['coverage'][j]['file']] = files_coverage[data[best_test]['coverage'][j]['file']].union(data[best_test]['coverage'][j]['lines'])
        used[best_test] = True
    
    with open(ADDITIONAL_GREEDY_PATH, "w") as f:
        json.dump(result, f, indent=4)
