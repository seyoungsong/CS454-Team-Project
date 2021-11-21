import json
import random
import matplotlib.pyplot as plt


#parameters
GENERATION_LIMIT = 100
POPULATION_SIZE = 100
RESOURCE_NUM = 4
MUTATION_RATE = 0.1
TOURNAMENT_SELECTION = 10
PARENTS_NUM = 20 # number of parents which generate offspring by crossover


def test_seq_time(test_seq, test_time_list):
    time = 0.0
    
    for test_idx in test_seq:
        time += test_time_list[test_idx]

    return time


def individual_time(individual, test_time_list):
    lst = []

    for test_seq in individual:
        lst.append(test_seq_time(test_seq, test_time_list))
    
    return max(lst)


def test_startTime_endTime_dict(individual, test_time_list):
    dict1 = {}
    dict2 = {}

    for test_seq in individual:
        time = 0.0
        for test_idx in test_seq:
            dict1[test_idx] = time
            time += test_time_list[test_idx]
            dict2[test_idx] = time


    return dict1, dict2


def satisfy_time_constraint(individual, time_constraint, test_time_list):
    for test_seq in individual:
        time = test_seq_time(test_seq, test_time_list)
        
        if time > time_constraint:
            return False
        
    return True


def shortest_test_seq(individual, test_time_list):
    idx = 0
    test_num = 0
    min_time = 1000.0

    for i in range(len(individual)):
        test_seq = individual[i]
        time = test_seq_time(test_seq, test_time_list)
        
        if time < min_time:
            min_time = time
            idx = i
        
        if time == min_time:
            if len(individual[i]) < test_num:
                test_num = len(individual[i])
                idx = i
    
    return idx


def initialization(population_size, test_time_list, test_time_large_list, test_time_small_list, time_constarint, resource_num):
    population = []

    while len(population) < population_size:
        permutation = test_time_small_list
        random.shuffle(permutation)

        individual = [[] for _ in range(resource_num)]

        current_idx = 0
        for test_idx in test_time_large_list:
            individual[current_idx].append(test_idx)
            current_idx += 1

        for test_idx in permutation:
            individual[shortest_test_seq(individual, test_time_list)].append(test_idx)
        
        if satisfy_time_constraint(individual, time_constarint, test_time_list):
            population.append(individual)

    return population


def find_index(individual, test_idx):
    for i in range(len(individual)):
        test_seq = individual[i]
        for j in range(len(test_seq)):
            if test_seq[j] == test_idx:
                return i, j
    print('error: no such index')


def fitness(individual, file_name_list, file_lines_list, test_time_list, test_coverage_list):
    first_test_for_line = []
    seq = []

    startTime_dict, _ = test_startTime_endTime_dict(individual, test_time_list)
    while len(startTime_dict) != 0:
        idx = min(startTime_dict.keys(), key=lambda k: startTime_dict[k])
        seq.append(idx)
        del startTime_dict[idx]


    for i in range(len(file_lines_list)):
        file_lines = file_lines_list[i]
        file_name = file_name_list[i]

        for line in file_lines:
            check = False
            for test_idx in seq:
                test_coverage = test_coverage_list[test_idx]
                for content in test_coverage:
                    if content['file'] == file_name and line in content['lines']:
                        first_test_for_line.append(test_idx)
                        check = True
                        break
                if check:
                    break

    m = len(first_test_for_line)
    total_time = sum(test_time_list)
    answer = 0.0

    for test_idx in first_test_for_line:
        temp = total_time
        i, j = find_index(individual, test_idx)
        test_seq = individual[i]
        for x in range(j+1):
            temp -= test_time_list[test_seq[x]]
        temp += 0.5 * test_time_list[test_seq[j]]
        answer += temp
    
    return round(answer/(total_time * m), 4)


def evaluate(population, file_name_list, file_lines_list, test_time_list, test_coverage_list):
    evaluation = []

    for individual in population:
        evaluation.append(fitness(individual, file_name_list, file_lines_list, test_time_list, test_coverage_list))

    return evaluation


def selection(population, evaluation):
    parents = []

    idx_list = list(range(len(population)))

    while len(parents) < PARENTS_NUM:
        selected_idx = random.sample(idx_list, TOURNAMENT_SELECTION)
        
        idx = 0
        max_fitness = 0.0

        for i in selected_idx:
            fitness = evaluation[i]
            
            if fitness > max_fitness:
                max_fitness = fitness
                idx = i
        
        parents.append(population[idx])
        idx_list.remove(idx)

    return parents


def crossover(parents, test_time_list, time_constraint):
    population = parents

    while len(population) < POPULATION_SIZE:
        parent1, parent2 = random.sample(parents, 2)

        time1 = individual_time(parent1, test_time_list)
        time2 = individual_time(parent2, test_time_list)
        time = max(time1, time2)

        cutpoint = random.random() * time

        parent1_startTime_dict, parent1_endTime_dict = test_startTime_endTime_dict(parent1, test_time_list)
        parent2_startTime_dict, parent2_endTime_dict = test_startTime_endTime_dict(parent2, test_time_list)

        offspring1 = [[] for _ in range(RESOURCE_NUM)]
        offspring2 = [[] for _ in range(RESOURCE_NUM)]

        for i in range(RESOURCE_NUM):
            test_seq = parent1[i]

            for test_idx in test_seq:
                if parent1_endTime_dict[test_idx] < cutpoint:
                    offspring1[i].append(test_idx)
                    del parent2_startTime_dict[test_idx]
                else:
                    break

        while len(parent2_startTime_dict) != 0:
            idx = min(parent2_startTime_dict.keys(), key=lambda k: parent2_startTime_dict[k])
            offspring1[shortest_test_seq(offspring1, test_time_list)].append(idx)
            del parent2_startTime_dict[idx]

        if satisfy_time_constraint(offspring1, time_constraint, test_time_list):
            population.append(offspring1)


        for i in range(RESOURCE_NUM):
            test_seq = parent2[i]

            for test_idx in test_seq:
                if parent2_endTime_dict[test_idx] < cutpoint:
                    offspring2[i].append(test_idx)
                    del parent1_startTime_dict[test_idx]
                else:
                    break

        while len(parent1_startTime_dict) != 0:
            idx = min(parent1_startTime_dict.keys(), key=lambda k: parent1_startTime_dict[k])
            offspring2[shortest_test_seq(offspring2, test_time_list)].append(idx)
            del parent1_startTime_dict[idx]

        if satisfy_time_constraint(offspring2, time_constraint, test_time_list):
            population.append(offspring2)

    if len(population) > POPULATION_SIZE:
        del population[-1]

    return population


def mutation(population, test_time_list, time_constraint):
    for i in range(len(population)):
        rand = random.random()
        
        if rand < MUTATION_RATE:
            individual = population[i]
            
            temp_list = list(range(len(individual)))
            test_seq_idx = random.choice(temp_list)
            test_seq = individual[test_seq_idx]

            while len(test_seq) == 1:
                temp_list.remove(test_seq_idx)
                test_seq_idx = random.choice(temp_list)
                test_seq = individual[test_seq_idx]
            
            idx1, idx2 = random.sample(range(len(test_seq)), 2)

            test_seq[idx1], test_seq[idx2] = test_seq[idx2], test_seq[idx1]
            
            while not satisfy_time_constraint(individual, time_constraint, test_time_list):
                test_seq[idx1], test_seq[idx2] = test_seq[idx2], test_seq[idx1]
                idx1, idx2 = random.sample(range(len(test_seq)), 2)
                test_seq[idx1], test_seq[idx2] = test_seq[idx2], test_seq[idx1]

    return   
            



def geneticAlgorithm():

    with open('data.json', 'r') as f:
        json_data = json.load(f)

    test_name_list = []
    test_time_list = []
    test_coverage_list = []

    for i in range(len(json_data)):
        test = json_data[i]
        test_name_list.append(test['name'])
        if test['time'] == 0.0:
            test_time_list.append(0.0001)
        else:
            test_time_list.append(test['time'])
        test_coverage_list.append(test['coverage'])
    
    file_name_list = []
    file_lines_list = []

    for coverage in test_coverage_list:
        for file_and_line in coverage:
            file_name = file_and_line['file']
            file_lines = file_and_line['lines'] #list of line

            if file_name not in file_name_list:
                file_name_list.append(file_name)
                file_lines_list.append(file_lines)
            
            else:
                idx = file_name_list.index(file_name)
                file_lines_list[idx] = list(set(file_lines_list[idx] + file_lines))


    
    generation = 0
    graph = []


    average_test_time = round(sum(test_time_list)/RESOURCE_NUM, 4)
    time_constraint = max(test_time_list)
    #time_constraint = sum(test_time_list)

    # list of test case number
    test_time_large_list = []
    test_time_small_list = []

    for i in range(len(test_time_list)):
        test_time = test_time_list[i]
        
        if test_time > average_test_time:
            test_time_large_list.append(i)
        else:
            test_time_small_list.append(i)

    population = initialization(POPULATION_SIZE, test_time_list, 
                                test_time_large_list, test_time_small_list, time_constraint, RESOURCE_NUM)
    evaluation = evaluate(population, file_name_list, file_lines_list, test_time_list, test_coverage_list)
    graph.append(max(evaluation))

    while generation <= GENERATION_LIMIT:
        if generation % 10 == 0:
            print("generation{}...".format(generation))
        generation += 1
        parents = selection(population, evaluation)
        population = crossover(parents, test_time_list, time_constraint)
        mutation(population, test_time_list, time_constraint)
        evaluation = evaluate(population, file_name_list, file_lines_list, test_time_list, test_coverage_list)
        graph.append(max(evaluation))
    
    best_fitness = max(evaluation)
    graph.append(best_fitness)
    idx = evaluation.index(best_fitness)
    best_individual = population[idx]

    plt.plot(graph)
    plt.ylabel('fitness')
    plt.xlabel('generation')
    plt.show()

    for test_seq in best_individual:
        for i in range(len(test_seq)):
            test_idx = test_seq[i]
            test_seq[i] = test_name_list[test_idx]

    print()
    return best_individual, best_fitness


answer = geneticAlgorithm()
print(answer[0])
print(answer[1])