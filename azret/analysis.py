import csv
import json

with open("result.json") as resultfile:
    resultdata = json.load(resultfile)

performances = [
    [1],
    [2],
    [4],
    [1, 3],
    [1, 1, 2],
    [2, 2],
    [8],
    [1, 7],
    [2, 6],
    [3, 5],
    [4, 4],
    [2, 2, 2, 2],
    [1, 1, 3, 3],
    [100]
    # [1],
    # [1] * 2,
    # [1] * 4,
    # [1] * 8,
    # [1] * 16,
    # [1, 2],
    # [1, 3],
    # [1, 4],
    # [1, 1, 1, 1, 4, 4, 4, 4],
]

data = [
    ["data"],
    [[1]],
    [[2]],
    [[4]],
    [[1, 3]],
    [[1, 1, 2]],
    [[2, 2]],
    [[8]],
    [[1, 7]],
    [[2, 6]],
    [[3, 5]],
    [[4, 4]],
    [[2, 2, 2, 2]],
    [[1, 1, 3, 3]],
    [[100]]
    # [[1]],
    # [[1] * 2],
    # [[1] * 4],
    # [[1] * 8],
    # [[1] * 16],
    # [[1, 2]],
    # [[1, 3]],
    # [[1, 4]],
    # [[1, 1, 1, 1, 4, 4, 4, 4]],
]

for datafile in resultdata:
    data[0].append(datafile["filename"])
    i = 1
    for result in datafile["results"]:
        data[i].append(result["APSC_c"])
        i = i + 1

f = open("result.csv", "w", newline="")
writer = csv.writer(f)
writer.writerows(data)
f.close()
