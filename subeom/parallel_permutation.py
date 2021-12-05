import random


class PPT:
    def __init__(self, num_test, num_sequence):
        self.num_test = num_test
        self.num_sequence = num_sequence
        self.ppt = []
        for i in range(self.num_sequence):
            self.ppt.append([])

    def random_init(self):
        self.ppt = []
        for i in range(self.num_sequence):
            self.ppt.append([])
        tests = list(range(self.num_test))
        random.shuffle(tests)
        sequences = random.choices(list(range(self.num_sequence)), k=self.num_test)
        for i in range(self.num_test):
            self.ppt[sequences[i]].append(tests[i])

    def random_neighbor(self):
        ret = PPT(self.num_test, self.num_sequence)
        ret.ppt = self.ppt[:]
        t = random.randrange(0, self.num_test)
        flag = False
        for i in range(self.num_sequence):
            if t in ret.ppt[i]:
                out_s = i
                out_t = ret.ppt[i].index(t)
                flag = True
                break
        if not flag:
            print((t, self.ppt, ret.ppt, self.num_test, self.num_sequence))
        del ret.ppt[out_s][out_t]
        # location = random.randrange(0, self.num_test + self.num_sequence - 1)
        # for i in range(self.num_sequence):
        #     if location <= len(ret.ppt[i]):
        #         ret.ppt[i].insert(location, t)
        #         break
        #     location = location - len(ret.ppt[i]) - 1
        in_s = random.randrange(0, self.num_sequence)
        in_t = random.randint(0, len(ret.ppt[in_s]))
        ret.ppt[in_s].insert(in_t, t)
        return ret

