import re, math

def read_puzzle(file):
    items = re.findall("\w+", open(file).read())
    navi = {items[3*i+1] : (items[3*i+2], items[3*i+3]) for i in range(len(items)//3)}
    return items[0], navi

def get_n(navi, cmds, start, ends):
    n = 0
    while not start in ends:
        dir_inx = 0 if cmds[n % len(cmds)] == "L" else 1
        start = navi[start][dir_inx]
        n += 1
    return n

def solve1(puzzle):
    cmds, navi = puzzle
    n1 = get_n(navi, cmds, "AAA", {"ZZZ"})
    starts = {start for start in list(navi.keys()) if start[-1]=="A" }
    ends = {start for start in list(navi.keys()) if start[-1]=="Z" }
    n2 = [get_n(navi, cmds, start, ends) for start in starts]
    print(n2, sum(n2))
    return n1, math.lcm(*n2)

print("Task 1/2", solve1(read_puzzle('d8.txt')))