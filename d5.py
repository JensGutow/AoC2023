import re

def calc_seed_revers_from_rule_in_hirarchie(rules, level, value):
    for rule in rules[level,0,-1]:
        y,x,delta = rule[1]
        rule_rev = ["rev", [x,y,delta]]
        value = apply_rule()

    pass

def calc_seeds_revers_from_rules(rules):
    seed_dict = dict()
    pass

def create_rule(s):
    args = s[0].split(" ")[0].split("-to-")
    rules = [list(map(int,re.findall("[\d]+", rule))) for rule in s[1:]]
    return (args, rules)

def apply_subrule(y_start, x_start, delta, x):
    y = x
    if x_start <= x and x <= x_start + delta:
        y = y_start + (x - x_start)
    return y

def apply_rule(rule, x):
    y = x
    for sub_rule in rule[1]:
        y = apply_subrule(*sub_rule, x)
        if x != y: break
    return y

def apply_rules(rules, x):
    y = x
    for rule in rules:
        y = apply_rule(rule, y)
    return y    

def read_puzzle(file):
    p = open(file).read().split("\n\n")
    p = [p_.split("\n") for p_ in p]
    seed = list(map(int,re.findall("[\d]+", p[0][0])))
    rules = list(map(create_rule, p[1:]))
    return seed, rules

def solve1(puzzle):
    seeds, rules = puzzle
    l = lambda seed: apply_rules(rules, seed)
    s1 = min(list(map(l, seeds)))
    # ## task2
    # seeds2 = []
    # for i in range(len(seeds)//2):
    #     for j in range(seeds[2*i+1]):
    #         seeds2.append(seeds[2*i]+j)
    # s2 = min(list(map(l, seeds2)))
    
    return s1

puzzle = read_puzzle('d5.txt')


print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))