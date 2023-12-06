import re

def apply_subrule_reverse(y_start, x_start, delta, value):
    x = value
    if y_start <= x and x < y_start + delta:
        x = x_start + (x - y_start)
    return x

def apply_rule_reverse(rule, value):
    x = value
    for sub_rule in rule[1]:
        x = apply_subrule_reverse(*sub_rule, x)
        if x != value: break
    return x

def calc_seed_reverse_by_level(rules, level, value):
    seed = value
    for rule in rules[level::-1]:
        seed = apply_rule_reverse(rule, seed)
    return seed


def calc_seeds_reverse_from_rules(rules):
    seeds = set()
    for i, rule in enumerate(rules):
        for sub_rule in rule[1]:
            y, _, delta = sub_rule
            seed1 = calc_seed_reverse_by_level(rules, i, y)
            seed2 = calc_seed_reverse_by_level(rules, i, y + delta - 1) + 1
            seeds.add(seed1)
            seeds.add(seed2)
    return seeds

def create_rule(s):
    args = s[0].split(" ")[0].split("-to-")
    rules = [list(map(int,re.findall("[\d]+", rule))) for rule in s[1:]]
    return (args, rules)

def apply_subrule(y_start, x_start, delta, x):
    y = x
    if x_start <= x and x < x_start + delta:
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
    return s1

def solve2(puzzle):
    l = lambda seed: apply_rules(rules, seed)
    seeds, rules = puzzle
    seed_checkpoints = calc_seeds_reverse_from_rules(rules)
    loc_min = 1000000000000000000000000000000000000000000000000
    for i in range(len(seeds)//2):
        s1 = seeds[2*i]
        s2 = seeds[2*i] + seeds[2*i + 1]
        seed_to_check = [seed for seed in seed_checkpoints if s1 <= seed <= s2]
        seed_to_check.append(s1)
        l1 = min(list(map(l, seed_to_check)))
        loc_min = min(loc_min,l1)
    return loc_min

puzzle = read_puzzle('d5.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))