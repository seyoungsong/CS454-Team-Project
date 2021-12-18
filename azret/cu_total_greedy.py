import math
import random

import ppt
import ptp


class CUTG:
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
            longest_test = -1
            longest_time = -1
            for j in range(self.problem.num_test):
                if chosen[j]:
                    continue
                current_time = self.problem.times[j]
                current_metric = len(self.problem.coverage[j])
                if best_test == -1 or best_metric < current_metric:
                    best_test = j
                    best_metric = current_metric
                    best_test_time = current_time
                if longest_test == -1 or longest_time < current_time:
                    longest_test = j
                    longest_time = current_time
            
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
            else:
                current.ppt[min_time_seq_index].append(best_test)
                chosen[best_test] = True
                sequence_time[min_time_seq_index] += best_test_time / min_time_seq_index_perf

        return current, self.problem.evaluate(current)
