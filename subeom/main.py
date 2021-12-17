import parallel_test_prioritization as ptp
import simulated_annealing as sa
import glob
import os
import json

json_data = glob.glob(os.path.join("..", "data", "*.json"))
performances = [
    [1],
    [1] * 2,
    [1] * 4,
    [1, 3],
    [1, 1, 2],
    [2, 2],
    [1] * 8,
    [1, 7],
    [2, 6],
    [3, 5],
    [4, 4],
    [2, 2, 2, 2],
    [1, 1, 3, 3],
    [1] * 100,
]

f = open("result_SA.txt", "w")

result_json = []

for data in json_data:
    print("data:" + data)
    f.write("data: \n" + data + "\n")
    problem = ptp.PTP(data, [1])
    data_dict = {"filename": problem.filename}
    name_to_id_dict = dict()
    for i in range(len(problem.test)):
        name_to_id_dict[problem.test[i]] = i
    data_dict["name_to_id"] = name_to_id_dict
    results = []
    for performance in performances:
        print("performance: " + str(performance))
        f.write("performance: \n" + str(performance) + "\n")
        result_dict = dict()
        result_dict["scenario"] = performance
        result_dict["TC"] = 1.5
        print("TC: 1.5")
        f.write("TC: 1.5\n")
        problem.update_performance(performance)
        sa_algorithm = sa.SA(problem)
        fittest, fitness = sa_algorithm.run(2000)
        print(fittest.ppt)
        f.write(str(fittest.ppt) + "\n")
        result_dict["permutations"] = fittest.ppt
        result_dict["APSC_c"] = fitness
        results.append(result_dict)
        print(fitness)
        f.write(str(fitness) + "\n")
    data_dict["results"] = results
    result_json.append(data_dict)

f.close()

with open("result_SA.json", "w") as outfile:
    json.dump(result_json, outfile, indent=4)
