import time

def read_puzzle(file):
    return [list(map(int, line.split())) for line in open(file).read().splitlines() ]

def find_nr_in_list(values):
    value = 0
    while any(i!=0 for i in values):
        value += values[-1]
        values = [v2 - v1 for v1, v2 in zip(values, values[1:])]
    return value

def solve1(puzzle):
    n1 = sum([find_nr_in_list(l) for l in puzzle])
    n2 = sum([find_nr_in_list(l[::-1]) for l in puzzle])
    return n1, n2

time_start = time.perf_counter()
print("Task 1/2", solve1(read_puzzle('d9.txt')))
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')