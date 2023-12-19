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

def split_list(l, op, value):
    inx = None
    for i, item in enumerate(l):
        if item[0] <= value or item[0] >= value:
            inx = i
            break
    assert(inx != None)
    left = []
    right = [[value]]


    return l,l

def counts(wfls, wfl, input):
    if wfl  in ["A", "R"] : return input 

    for cond, act in zip(wfls[wfl]):
        if "<" in cond or ">" in cond:
            inx = "xmas".index(cond[0])
            op = cond[1]
            value = int(cond[2:])
            l1, r1 = split_list(input[inx], op, value)
            left = [copy.copy(input[i]) if i!=inx else l1 for i in range(4)]
            right = [copy.copy(input[i]) if i!=inx else r1 for i in range(4)]
            input = counts(wfls, act, left)
            input = [a.extend(b) for a,b in zip(right, input)]
        else:
            input = counts(wfls, act, input)

    return input

def solve2(puzzle):
    wfls, _ = puzzle
    x = [[0,4000]]
    m = [[0,4000]]
    a = [[0,4000]]
    s = [[0,4000]]
    results = counts(wfls, "in", [x,m,a,s])
    return math.prod(len(res) for res in results)

puzzle = read_puzzle('d19.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))