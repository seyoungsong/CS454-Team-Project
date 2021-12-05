import csv
import json

with open("result4.json") as resultfile:
    resultdata = json.load(resultfile)

performances = [
    [1],
    [1] * 2,
    [1] * 4,
    [1] * 8,
    [1] * 16,
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 1, 1, 1, 4, 4, 4, 4],
]

data = [
    ["data"],
    [[1]],
    [[1] * 2],
    [[1] * 4],
    [[1] * 8],
    [[1] * 16],
    [[1, 2]],
    [[1, 3]],
    [[1, 4]],
    [[1, 1, 1, 1, 4, 4, 4, 4]],
]

for datafile in resultdata:
    data[0].append(datafile["filename"])
    i = 1
    for result in datafile["results"]:
        data[i].append(result["APSC_c"])
        i = i + 1

f = open("result4.csv", "w", newline="")
writer = csv.writer(f)
writer.writerows(data)
f.close()
