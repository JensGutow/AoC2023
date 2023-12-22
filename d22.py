import re, copy
def read_puzzle(file):
    # item: name: set of (x,y,z) positions
    d = dict()
    for i, line in enumerate(open(file).readlines()):
        bricks = set()
        quader = line.strip()
        name = i
        coords = list(map(int,list(re.findall("[\d]+",quader))))
        start = coords[:3]
        end = coords[3:]
        for i in range(3): assert(start[i] <= end[i])
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                for z in range(start[2], end[2] + 1):
                    bricks.add((x,y,z))
        d[name] = bricks
    print("number of bricks:",len(d))
    return d

def min_z(bricks):
    return min([brick[2] for brick in bricks])

def move_quader_down(puzzle, quader, bs):
    if min_z(puzzle[quader]) == 1: return False, bs
    bs = bs.difference(puzzle[quader])
    result = False
    moved  = True
    q_down = copy.copy(puzzle[quader])
    while moved:
        q_down2 = {(item[0], item[1], item[2]-1) for item in q_down}
        if min_z(q_down2) >= 1 and not q_down2.intersection(bs):
            q_down = q_down2
            result = True
        else: 
            moved = False
    puzzle[quader] = q_down
    bs = bs.union(puzzle[quader])
    return result, bs

def minimize_puzzle(puzzle, bs):
    moves_are_possible = True
    result = False
    while moves_are_possible:
        moves_are_possible = False
        order = sorted([(min_z(puzzle[quader]), quader) for quader in puzzle])
        for _, quader in order:
            result_new, bs = move_quader_down(puzzle, quader, bs)
            if result_new:
                moves_are_possible = True
                result = True
    return result, bs

def solve1(puzzle):
    minz = min(min_z(bricks) for bricks in puzzle.values()) - 1
    for name, bricks in puzzle.items():
        puzzle[name] = {(brick[0], brick[1],brick[2]-minz) for brick in bricks}
    bs = set()
    for bs_ in puzzle.values(): bs = bs.union(bs_)
    result, bs = minimize_puzzle(puzzle, bs)
    part1 = 0
    part2 = 0
    for i, q in  enumerate(puzzle.keys()):
        p2 = copy.deepcopy(puzzle)
        p2.pop(q)
        bs = bs.difference(puzzle[q])
        result, _ = minimize_puzzle(p2, bs)
        bs = bs.union(puzzle[q])
        if not result:
            part1 += 1
        else:
            d2 = 0
            for q2 in p2:
                if p2[q2] != puzzle[q2]:
                    d2 +=1
            part2 += d2
    return part1, part2

puzzle = read_puzzle('d22.txt')

print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))