import math
import random

import ppt
import ptp


class CAAG:
    def __init__(self, problem: ptp.PTP):
        self.problem = problem

    def run(self):
        current = ppt.PPT(self.problem.num_test, self.problem.num_sequence)

        sequence_time = [0] * current.num_sequence
        k = current.num_sequence

        large = 0
        chosen = [False] * self.problem.num_test

        # 2.3 Unified initialization for Parallel Test Prioritization
        for i in range(self.problem.num_test):
            current_time = self.problem.times[i] / self.problem.performance[k - 1]
            if current_time >= self.problem.avg_time:
                current.ppt[k - 1].append(i)
                sequence_time[k - 1] += current_time
                chosen[i] = True
                large += 1
                k -= 1

        # Have to construct sequences [0 .. k - 1]
        for i in range(self.problem.num_test - large):
            best_test = -1
            best_metric = -1
            best_test_time = -1
            best_test_coverage = None
            longest_test = -1
            longest_time = -1
            longest_test_coverage = None
            all_coverages = set()
            for j in range(self.problem.num_test):
                if chosen[j]:
                    continue
                current_coverage = self.problem.coverage[j]
                current_time = self.problem.times[j]
                current_metric = (len(all_coverages | current_coverage) - len(all_coverages)) / current_time
                if best_test == -1 or best_metric < current_metric:
                    best_test = j
                    best_metric = current_metric
                    best_test_time = current_time
                    best_test_coverage = current_coverage
                if longest_test == -1 or longest_time < current_time:
                    longest_test = j
                    longest_time = current_time
                    longest_test_coverage = current_coverage

            min_time_seq_index = min(
                list(range(k)),
                key=lambda seq_index: (sequence_time[seq_index], -self.problem.performance[seq_index]),
            )
            min_time_seq_index_perf = self.problem.performance[min_time_seq_index]
            if (sequence_time[min_time_seq_index]
                + best_test_time / min_time_seq_index_perf
                + longest_time / min_time_seq_index_perf) > self.problem.TC:
                current.ppt[min_time_seq_index].append(longest_test)
                chosen[longest_test] = True
                sequence_time[min_time_seq_index] += longest_time / min_time_seq_index_perf
                all_coverages = all_coverages | longest_test_coverage
            else:
                current.ppt[min_time_seq_index].append(best_test)
                chosen[best_test] = True
                sequence_time[min_time_seq_index] += best_test_time / min_time_seq_index_perf
                all_coverages = all_coverages | best_test_coverage

        return current, self.problem.evaluate(current)
