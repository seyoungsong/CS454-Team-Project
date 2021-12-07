import random


class PPT:
    def __init__(self, num_test, num_sequence):
        self.num_test = num_test
        self.num_sequence = num_sequence

        self.ppt = []
        for i in range(self.num_sequence):
            self.ppt.append([])
