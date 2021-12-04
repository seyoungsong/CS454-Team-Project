import parallel_test_prioritization as ptp
import simulated_annealing as sa
import glob
import os

json_data = glob.glob(os.path.join("..", "data", "*.json"))
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

f = open("result3.txt", "w")

for data in json_data:
    print("data:" + data)
    f.write("data: \n" + data + "\n")
    problem = ptp.PTP(data, [1])
    for performance in performances:
        print("performance: " + str(performance))
        f.write("performance: \n" + str(performance) + "\n")
        problem.update_performance(performance)
        sa_algorithm = sa.SA(problem)
        fittest = sa_algorithm.run(2000)
        print(fittest.ppt)
        f.write(str(fittest.ppt) + "\n")

