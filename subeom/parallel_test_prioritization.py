import json
import parallel_permutation as ppt


class PTP:
    def __init__(self, filename, performance):
        self.performance = performance

        with open(filename) as f:
            test_coverage = json.load(f)

        self.test = []
        self.times = []
        self.coverage = []
        self.total_time = 0
        all_coverages = set()
        for test in test_coverage["data"]:
            if "duration" not in test:
                continue
            self.test.append(test["name"])
            self.times.append(test["duration"])
            if self.times[-1] == 0:
                self.times[-1] = 0.0005  # minimum expected duration
            self.total_time = round(self.total_time + self.times[-1], 5)
            coverages = []
            for coverage in test["coverage"]:
                prefix = coverage["package"] + "\\" + coverage["class"] + "\\"
                for line in coverage["lines"]:
                    coverages.append(prefix + line)
            self.coverage.append(set(coverages))
            all_coverages = all_coverages | self.coverage[-1]
        self.num_test = len(self.test)
        self.num_sequence = len(self.performance)
        self.num_coverage = len(all_coverages)

        self.greedy_ppt()

    def evaluate(self, candidate: ppt.PPT):  # evlauate fitness function
        index = [0] * self.num_sequence
        time = [0] * self.num_sequence
        for i in range(self.num_sequence):
            if index[i] < len(candidate.ppt[i]):
                time[i] = round(
                    time[i]
                    + self.times[candidate.ppt[i][index[i]]] / self.performance[i] / 2,
                    5,
                )
            else:
                time[i] = self.total_time
        covered = set()
        covered_num = 0
        time_taken = 0
        while covered_num < self.num_coverage:
            min_time = min(time)
            min_time_sequence = time.index(min_time)
            if min_time_sequence >= len(candidate.ppt) or index[
                min_time_sequence
            ] >= len(candidate.ppt[min_time_sequence]):
                print(
                    (
                        min_time,
                        min_time_sequence,
                        index[min_time_sequence],
                        candidate.ppt,
                        self.num_sequence,
                        self.num_test,
                        time,
                        self.total_time,
                    )
                )
            min_time_test = candidate.ppt[min_time_sequence][index[min_time_sequence]]
            covered = covered | self.coverage[min_time_test]
            next_covered_num = len(covered)
            new_covered_num = next_covered_num - covered_num
            covered_num = next_covered_num
            time_taken = time_taken + min_time * new_covered_num
            index[min_time_sequence] = index[min_time_sequence] + 1
            if index[min_time_sequence] >= len(candidate.ppt[min_time_sequence]):
                time[min_time_sequence] = self.total_time
            else:
                time[min_time_sequence] = round(
                    time[min_time_sequence]
                    - self.times[
                        candidate.ppt[min_time_sequence][index[min_time_sequence] - 1]
                    ]
                    / self.performance[min_time_sequence]
                    / 2,
                    5,
                )
                time[min_time_sequence] = round(
                    time[min_time_sequence]
                    + self.times[
                        candidate.ppt[min_time_sequence][index[min_time_sequence] - 1]
                    ]
                    / self.performance[min_time_sequence],
                    5,
                )
                time[min_time_sequence] = round(
                    time[min_time_sequence]
                    + self.times[
                        candidate.ppt[min_time_sequence][index[min_time_sequence]]
                    ]
                    / self.performance[min_time_sequence]
                    / 2,
                    5,
                )
        apsc = (self.total_time * self.num_coverage - time_taken) / (
            self.total_time * self.num_coverage
        )
        return apsc

    def greedy_ppt(self):
        self.greedy = ppt.PPT(self.num_test, self.num_sequence)
        sorted_time = sorted(enumerate(self.times), key=lambda x: x[1], reverse=True)
        sequence_time = [0] * self.num_sequence
        for time, test in sorted_time:
            min_index = min(
                list(range(self.num_sequence)),
                key=lambda x: (sequence_time[x], -self.performance[x]),
            )
            self.greedy.ppt[min_index].append(test)
            sequence_time[min_index] = (
                sequence_time[min_index] + time / self.performance[min_index]
            )
        self.avg_time = max(sequence_time)
        self.TC = 1.5 * self.avg_time

    def valid(self, candidate: ppt.PPT):
        for i in range(self.num_sequence):
            time = 0
            for test in candidate.ppt[i]:
                time = time + self.times[test] / self.performance[i]
            if time > self.TC:
                return False
        return True

    def update_performance(self, new_performance):
        self.performance = new_performance
        self.num_sequence = len(new_performance)
        self.greedy_ppt()
