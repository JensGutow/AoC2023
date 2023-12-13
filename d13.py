# 
def read_puzzle(file):
    return [p.split() for p in  open(file).read().split("\n\n")]

def count_mirror(pattern):
    n = 0
    l = len(pattern)
    for k in range(1,l):
        test = True
        for j in range(min(k,l-k )):
            inx1 = k-j-1
            inx2 = k+j
            n=k
            if pattern[inx1] != pattern[inx2]:
                test = False
                n = 0
                break
        if test: break
    return n

def solve1(puzzle):
    h = v = 0
    for i, p in enumerate(puzzle):
        #print("pattern", i)
        #print("horz")
        h += count_mirror(p)
        #print("vert")
        v += count_mirror(list(zip(*p)))

        #print("horz",h, "vert",v )
    return h*100 + v

puzzle = read_puzzle('d13.txt')

print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))