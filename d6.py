# haltezeit: th=0..tr
# speed = th
# s=v*t1 = v*(tr-th)

import re,math
def read_puzzle(file):
    lines = list(map(int,re.findall("[\d]+", open(file).read())))
    l = len(lines)
    return lines[:l//2], lines[l//2:]

def find_n(t_game, s_game):
    p_2 = -t_game/2
    q = s_game
    term1 = math.sqrt(p_2**2-q)
    s1 = -p_2 - term1
    s2 = -p_2 + term1
    return  math.ceil(s2) - math.floor(s1) - 1

def solve1(puzzle):
    p = 1
    for t_max,s in list(zip(*puzzle)):
        n= 0
        for t_h in range(0,t_max):
            s_v = t_h * (t_max-t_h)
            if (s_v > s):n += 1
        p *= n
    return p

def get_nr_from_list(l):
    return int("".join(list(map(str, l))))

def solve2(puzzle):
    t_game = get_nr_from_list(puzzle[0])
    s_game = get_nr_from_list(puzzle[1])
    return find_n(t_game, s_game)

puzzle = read_puzzle('d6.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))