# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. 
# 5 Gleiche
# 4 Gleiche
# Full House: 2 Gleiche + 3 Gleiche
# 3 Gleiche + 2 unterschiedliche
# 2 Paare + ein andere
# 1 Paar
# Hohe Karte

# bei gleichen type: Reihenfolge bestimmt Ordnung (karten werden nicht sortiert)
# Rang der Hand bei N Teilnehmer
# Gebot * Rang

from collections import Counter
import copy

def read_puzzle(file):
    puzzle = []
    for line in open(file).read().splitlines():
        line = line.split()
        hand = line[0]
        bid = int(line[1])
        puzzle.append([hand, bid])
    return puzzle

def get_type_value(hand):
    rang_dict = {(5,):      0x700000, 
            (4,1):         0x600000, 
            (3,2):         0x500000, 
            (3,1,1):       0x400000, 
            (2,2,1):       0x300000, 
            (2,1,1,1):     0x200000, 
            (1,1,1,1,1):   0x100000}
    rang_cnt = Counter(hand)
    values = list(rang_cnt.values())
    values.sort(reverse=True)
    return (rang_dict[tuple(values)])

def get_rang_value(hand, part1):
    order_part1 = "AKQJT98765432"[::-1]
    order_part2 = "AKQT98765432J"[::-1]
    rang = 0
    step = 1
    for k in hand[::-1]:
        order = order_part1 if part1 else order_part2
        rang += step * order.index(k)
        step *= 16 
    rang_value = 0
    chs = set(hand)
    if (part1) or (not "J" in chs):
        rang_value = get_type_value(hand)
    else:
        rang_value = 0
        for c in chs:
            hand2 = hand.replace("J",c)
            rang_value = max(rang_value, get_type_value(hand2))
    rang += rang_value
    return rang

def solve1(puzzle, part1):
    rangs_values = []
    sorted_rangs_values = []
    for i, p in enumerate(puzzle):
        rangs_values.append(get_rang_value(p[0], part1))
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