import re, math
def read_puzzle(file):
    items = re.findall("[0-9A-Z]+", open(file).read())
    cmds = items[0]
    navi = dict()
    for i in range(len(items)//3):
        navi[items[3*i+1]] = (items[3*i+2], items[3*i+3])
    return cmds, navi

def get_n(navi, cmds, start, ziel):
    n = 0
    s = start
    while not start in ziel:
        dir_inx = 0 if cmds[n % len(cmds)] == "L" else 1
        start = navi[start][dir_inx]
        n += 1
    return n

def solve1(puzzle):
    cmds, navi = puzzle
    return get_n(navi, cmds, "AAA", {"ZZZ"})

def solve2(puzzle):
    cmds, navi = puzzle
    starts = {start for start in list(navi.keys()) if start[-1]=="A" }
    ends = {start for start in list(navi.keys()) if start[-1]=="Z" }
    n = [get_n(navi, cmds, start, ends) for start in starts]
    return math.lcm(*n)

puzzle = read_puzzle('d8.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))