from read_data import read_json, TOTAL_COVERAGE_PATH

import json
import os


TWO_OPT_ADDITIONAL_GREEDY_PATH = os.path.dirname(os.path.abspath(__file__)) + '/two_opt_data.json'

def two_opt_additional_greedy():
    data = read_json()
    coverage_data = read_json(TOTAL_COVERAGE_PATH)

    files_coverage = {}
    for file in coverage_data.keys():
        files_coverage[file] = set()

    unused_tests = len(data)

    used = [False for it in range(len(data))]
    result = []
    while unused_tests > 0:
        best_test = (-1, -1)
        best_delta = (-1, -1)
        for i in range(len(data)):
            if used[i]:
                continue
            for k in range(len(data)):
                if used[k]:
                    continue
                delta = 0
                temp = {}
                for j in range(len(data[i]['coverage'])):
                    if data[i]['coverage'][j]['file'] in temp:
                        temp[data[i]['coverage'][j]['file']] = temp[data[i]['coverage'][j]['file']].union(data[i]['coverage'][j]['lines'])
                    else:
                        temp[data[i]['coverage'][j]['file']] = files_coverage[data[i]['coverage'][j]['file']].union(data[i]['coverage'][j]['lines'])
                first_delta = 0
                for file, lines in temp.items():
                    first_delta += len(lines) - len(files_coverage[file])
                for j in range(len(data[k]['coverage'])):
                    if data[k]['coverage'][j]['file'] in temp:
                        temp[data[k]['coverage'][j]['file']] = temp[data[k]['coverage'][j]['file']].union(data[k]['coverage'][j]['lines'])
                    else:
                        temp[data[k]['coverage'][j]['file']] = files_coverage[data[k]['coverage'][j]['file']].union(data[k]['coverage'][j]['lines'])
                for file, lines in temp.items():
                    delta += len(lines) - len(files_coverage[file])
                if best_delta[1] < delta or (best_delta[1] == delta and best_delta[0] < first_delta):
                    best_delta = (first_delta, delta)
                    best_test = (i, k)
        result.append(data[best_test[0]])
        unused_tests -= 1
        if best_test[0] != best_test[1]:
            result.append(data[best_test[1]])
            unused_tests -= 1
        for j in range(len(data[best_test[0]]['coverage'])):
            files_coverage[data[best_test[0]]['coverage'][j]['file']] = files_coverage[data[best_test[0]]['coverage'][j]['file']].union(data[best_test[0]]['coverage'][j]['lines'])
        for j in range(len(data[best_test[1]]['coverage'])):
            files_coverage[data[best_test[1]]['coverage'][j]['file']] = files_coverage[data[best_test[1]]['coverage'][j]['file']].union(data[best_test[1]]['coverage'][j]['lines'])
        used[best_test[0]] = True
        used[best_test[1]] = True
    
    with open(TWO_OPT_ADDITIONAL_GREEDY_PATH, "w") as f:
        json.dump(result, f, indent=4)
