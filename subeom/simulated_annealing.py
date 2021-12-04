import math
import random
import parallel_test_prioritization as ptp
import parallel_permutation as ppt


class SA:
    def __init__(self, problem: ptp.PTP):
        self.problem = problem

    def run(self, n, alpha=0.99):  # alpha: cooling coefficient
        current = ppt.PPT(self.problem.num_test, self.problem.num_sequence)
        is_valid = False
        while not is_valid:
            current.random_init()
            is_valid = self.problem.valid(current)
        temperature = 1  # initial temperature
        current_fitness = self.problem.evaluate(current)
        for k in range(n):
            is_valid = False
            while not is_valid:
                new = current.random_neighbor()
                is_valid = self.problem.valid(current)
            new_fitness = self.problem.evaluate(new)
            if (
                new_fitness > current_fitness
                or math.exp((new_fitness - current_fitness) / temperature)
                >= random.random()
            ):
                current = new
                current_fitness = new_fitness
            temperature = temperature * alpha
            if k % 50 == 0:
                print((k, current_fitness))
        return current

