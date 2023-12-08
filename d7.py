from collections import Counter

def read_puzzle(file):
    puzzle = []
    for line in open(file).read().splitlines():
        line = line.split()
        puzzle.append([line[0], int(line[1])])
    return puzzle

def get_type_value(hand, part1):
    rang_cnt = Counter(hand)

    if not part1 and "J" in rang_cnt.keys(): 
        rang_cnt[rang_cnt.most_common(1)[0][0]] +=1
        rang_cnt["J"] -= 1

    if 5 in rang_cnt.values(): return 0x700000
    if 4 in rang_cnt.values(): return 0x600000
    if 3 in rang_cnt.values() and 2 in rang_cnt.values(): return 0x500000
    if 3 in rang_cnt.values(): return 0x400000
    if list(rang_cnt.values()).count(2) == 2: return 0x300000
    if 2 in rang_cnt.values(): return 0x200000
    return 0x100000

def get_rang_value(hand, part1):
    order_part1 = "AKQJT98765432"[::-1]
    order_part2 = "AKQT98765432J"[::-1]
    order = order_part1 if part1 else order_part2
    rang = sum([k*16**i  for i, k in enumerate([order.index(k) for k in hand[::-1]])])
    rang_value = get_type_value(hand, part1)
    rang += rang_value
    return rang

def solve1(puzzle, part1):
    rangs_values = []
    sorted_rangs_values = []
    for i, p in enumerate(puzzle):
        rangs_values.append(get_rang_value(p[0], part1))
        print(p[0], hex(get_rang_value(p[0], part1)))
    sorted_rangs_values = rangs_values.copy()
    sorted_rangs_values.sort()
    rang = [sorted_rangs_values.index(rang) + 1 for rang in rangs_values] 
    s1 = 0
    for i in range(len(puzzle)):
        s1 += rang[i] * puzzle[i][1]
    return s1

puzzle = read_puzzle('d7.txt')

print("Task 1", solve1(puzzle, part1 = True))
print("Task 2", solve1(puzzle, part1 = False))