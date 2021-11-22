from additional_greedy import additional_greedy, ADDITIONAL_GREEDY_PATH
from greedy import greedy, GREEDY_PATH
from read_data import read_json
from two_opt_additional_greedy import two_opt_additional_greedy, TWO_OPT_ADDITIONAL_GREEDY_PATH

import os


HERE = os.path.dirname(os.path.abspath(__file__))

def run_greedy():
    greedy()

def run_additional_greedy():
    additional_greedy()

def run_two_opt_additional_greedy():
    two_opt_additional_greedy()

def grade(order, report_name):
    files_coverage = {}
    deltas_per_file_per_test = []

    for test in order:
        total_delta = 0
        deltas_for_test = []

        for coverage_info in test['coverage']:
            file = coverage_info['file']
            lines = set(coverage_info['lines'])

            if file not in files_coverage:
                files_coverage[file] = set()

            before = len(files_coverage[file])
            files_coverage[file] = files_coverage[file].union(lines)
            after = len(files_coverage[file])

            delta = after - before
            total_delta += delta

            deltas_for_test.append((file, delta))

        deltas_per_file_per_test.append(deltas_for_test)

    with open(HERE + f"/{report_name}.txt", 'w') as out:
        total_lines = 0
        for file, coverage in files_coverage.items():
            total_lines += len(coverage)
            print(f"For file {file}, covered lines = {len(coverage)}", file=out)

        cumulative_delta = 0
        for i in range(len(deltas_per_file_per_test)):
            print(file=out)
            print(f"Test #{i + 1} started: {order[i]['name']}", file=out)

            total_delta = 0
            for delta in deltas_per_file_per_test[i]:
                total_delta += delta[1]
                print(f"For file {delta[0]} delta is {delta[1] / len(files_coverage[delta[0]]) * 100:.2f}%", file=out)

            cumulative_delta += total_delta
            print(f"Test #{i + 1} ended: {test['name']}, total_delta = {total_delta / total_lines * 100:.2f}%, cumulative_delta = {cumulative_delta / total_lines * 100:.2f}%", file=out)

def grade_greedy():
    g = read_json(GREEDY_PATH)
    grade(g, "greedy_report")

def grade_additional_greedy():
    ag = read_json(ADDITIONAL_GREEDY_PATH)
    grade(ag, "additional_greedy_report")

def grade_two_opt_additional_greedy():
    toag = read_json(TWO_OPT_ADDITIONAL_GREEDY_PATH)
    grade(toag, "two_opt_additional_greedy_report")

def run_all():
    run_greedy()
    run_additional_greedy()
    run_two_opt_additional_greedy()

def grade_all():
    grade_greedy()
    grade_additional_greedy()
    grade_two_opt_additional_greedy()

def benchmark_all():
    run_all()
    grade_all()


if __name__ == "__main__":
    # run_all()
    # grade_all()

    benchmark_all()

    # run_greedy()
    # grade_greedy()

    # run_additional_greedy()
    # grade_additional_greedy()

    # run_two_opt_additional_greedy()
    # grade_two_opt_additional_greedy()
