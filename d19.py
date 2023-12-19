import re, math, copy

def read_puzzle(file):
    rules_d = dict()
    rules_out = []
    wfls, parts = open(file).read().split("\n\n")
    for line in wfls.splitlines():
        k1 = line.index("{")
        k2 = line.index("}")
        r_name = line[0:k1]
        rules = line[k1+1:-1].split(",")
        rules_out = []
        for rule in rules:
            if ":" in rule: 
                cond, act = rule.split(":")
            else:
                cond, act = "True",rule
            rules_out.append((cond, act))
        rules_d[r_name] = rules_out
    part_list = []
    for part in parts.splitlines():
        part_list.append(list(map(int,list(re.findall("\d+", part)))))
    return rules_d, part_list
        
def check_rules(rules, part):
    x, m, a, s = part
    ret = None
    for cond, act in rules:
        if eval(cond):
            ret=act
            break
    return ret

def check_wfl(wfls, wfl, part):
    result = None
    while True:
        wfl = check_rules(wfls[wfl], part)
        if wfl == "A": 
            result = True
            break
        elif wfl == "R":
            result = False
            break
    return result
   
def solve1(puzzle):
    wfls, parts = puzzle
    part1 = 0
    for part in parts:
        x,m,a,s = part
        if check_wfl(wfls, "in", part):part1 += (x + m + a + s)
    return part1

def counts(wfls, wfl, areas):
    if wfl == "A": return math.prod([area[1]-area[0]+1 for area in areas])
    if wfl == "R": return 0

    ammounts = 0
    for cond, act in wfls[wfl]:
        if "<" in cond or ">" in cond:
            inx = "xmas".index(cond[0])
            op = cond[1]
            value = int(cond[2:])
            low, high = areas[inx]
            areas_new = copy.copy(areas)
            if op == "<":
                areas_new[inx] = (low, value-1)
                areas[inx] = (value, high)
            else:
                areas_new[inx] = (value + 1, high)
                areas[inx] = (low, value)
            ammounts += counts(wfls, act, areas_new)
        else:
            ammounts += counts(wfls, act, areas)

    return ammounts

def solve2(puzzle):
    wfls, _ = puzzle
    x = [1,4000]
    m = [1,4000]
    a = [1,4000]
    s = [1,4000]
    return  counts(wfls, "in", [x,m,a,s]) 

puzzle = read_puzzle('d19.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))