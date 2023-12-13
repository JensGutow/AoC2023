def read_puzzle(file):
    return [p.split() for p in  open(file).read().split("\n\n")]

def count_mirrors(pattern, part1 = True):
    l = len(pattern)
    for k in range(1,len(pattern)):
        m = min(k, l-k)
        a = pattern[k-m:k][::-1]
        b = pattern[k:k+m]
        if part1:
            if a==b : return k
        else:
            if sum([c1 != c2 for l1, l2 in zip(a,b) for c1, c2 in zip(l1,l2)]) == 1: return k
    return 0

def solve1(puzzle):
    h2 = v2 = h = v = 0
    for p in puzzle:
        h += count_mirrors(p)
        v +=  count_mirrors(list(zip(*p)))
        h2 += count_mirrors(p, False)
        v2 +=  count_mirrors(list(zip(*p)), False)

    return h*100 + v, h2*100 + v2

puzzle = read_puzzle('d13.txt')

print("Task 1", solve1(puzzle))