def read_puzzle(file):
    return [list(map(int, line.split())) for line in open(file).read().splitlines() ]

def find_nr_in_list(values):
    ends = []
    while any(i!=0 for i in values):
        ends.append(values[-1])
        values = [values[i+1] - values[i] for i in range(len(values)-1)]
    return sum(ends)

def solve1(puzzle):
    n1 = sum([find_nr_in_list(l) for l in puzzle])
    n2 = sum([find_nr_in_list(l[::-1]) for l in puzzle])
    return n1, n2

print("Task 1/2", solve1(read_puzzle('d9.txt')))