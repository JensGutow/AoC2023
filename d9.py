import re 
def read_puzzle(file):
    return [list(map(int, re.findall("[-]?[\d]+", line))) for line in open(file).read().splitlines() ]

def find_nr_in_list(values):
    n = 0
    start_values = []
    while any(i!=0 for i in values):
        n += 1
        start_values.append(values[0])
        values = [values[i+1] - values[i] for i in range(len(values)-1)]
    values.append(0)
    for i in range(n):
        l1 = [start_values[n-i-1]]
        for v in values:
            l1.append(l1[-1]+v)
        values = l1
    first = 0
    for v in start_values[::-1]:
        first = v - first
    return(values[-1], first )

def solve1(puzzle):
    solutions = [find_nr_in_list(l) for l in puzzle]
    return[sum(values)  for values in zip(*solutions)]

puzzle = read_puzzle('d9.txt')

print("Task 1", solve1(puzzle))