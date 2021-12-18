import glob
import json
import os

import ca_total_greedy
import ca_additional_greedy
import cu_total_greedy
import cu_additional_greedy
import ptp


if __name__ == "__main__":
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
        # [1]
        # [1] * 2,
        # [1] * 4,
        # [1] * 8,
        # [1] * 16,
        # [1, 2],
        # [1, 3],
        # [1, 4],
        # [1, 1, 1, 1, 4, 4, 4, 4]
    ]

    result_json = []
    with open("result.txt", "w") as f:
        json_data = glob.glob(os.path.join("..", "data", "*.json"))
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
                
                problem.update_performance(performance)
                
                # algorithm = cu_total_greedy.CUTG(problem)
                # algorithm = cu_additional_greedy.CUAG(problem)
                # algorithm = ca_total_greedy.CATG(problem)
                algorithm = ca_additional_greedy.CAAG(problem)
                fittest, fitness = algorithm.run()
                print(fittest.ppt)
                f.write(str(fittest.ppt) + "\n")
                
                result_dict["permutations"] = fittest.ppt
                result_dict["APSC_c"] = fitness
                results.append(result_dict)
            data_dict["results"] = results

            result_json.append(data_dict)

    with open("result.json", "w") as out:
        json.dump(result_json, out, indent=4)
