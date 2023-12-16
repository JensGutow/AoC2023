from copy import deepcopy

X_MAX = Y_MAX = X_MIN = Y_MIN = 0
DIRS = {"N":(0,-1),"E":(1,0),"S":(0,1),"W":(-1,0)}
BEAM_RULES = {("N", "|"):"N" , ("S", "|"):"S", ("E", "|"):"SN", ("W", "|"):"SN",
              ("N", "-"):"EW", ("S", "-"):"EW",("E", "-"): "E", ("W", "-"):"W",
              ("N", "/"):"E" , ("S", "/"):"W", ("E", "/"): "N", ("W", "/"):"S",
              ("N","\\"):"W" , ("S","\\"):"E", ("E","\\"): "S", ("W","\\"):"N",
              ("N", "."):"N" , ("S", "."):"S", ("E", "."): "E", ("W", "."):"W"
              }

def read_puzzle(file):
    d =  {(x,y):[c, set()] for y, line in enumerate(open(file).read().splitlines()) for x, c in enumerate(line)}
    max_y = max([y for _,y in d.keys() ])
    max_x = max([x for x,_ in d.keys() ])
    return d, max_x, max_y

def get_neighbors(puzzle, pos, dirs):
    x,y = pos
    c, _ = puzzle[pos]
    nbs = []
    for dir in dirs:
        for new_dir in BEAM_RULES[(dir, c)]:
            dx, dy = DIRS[new_dir]
            new_point = (x+dx, y+dy)
            if new_point in list(puzzle.keys()):
                nbs.append((new_point, new_dir)) # pos, dir
    return nbs

def get_energy_value(puzzle):
    return sum([1 for _, dirs in puzzle.values() if dirs])

def bfs(p,start, dir):
    puzzle = deepcopy(p)
    visited = set()
    queue = []
    queue.append((start, dir))
    while queue:
        pos, dir = queue.pop(0)
        if (dir, pos) in visited : continue
        p_c, p_dirs = puzzle[pos]
        puzzle[pos] = (p_c, p_dirs.union(dir))
        visited.add((dir, pos))
        for next_pos_dir in  get_neighbors(puzzle, pos, dir):
            queue.append(next_pos_dir)
    e = get_energy_value(puzzle)
    print(e)
    return e

def solve(puzzle):
    part1 =  bfs(puzzle, (0,0), "E")

    check_points = [("E", [(X_MIN, y) for y in range(Y_MIN, Y_MAX + 1)]),
                    ("W", [(X_MAX, y) for y in range(Y_MIN, Y_MAX + 1)]),
                    ("S", [(x, Y_MIN) for x in range(X_MIN, X_MAX + 1)]),
                    ("N", [(x, Y_MAX) for x in range(X_MIN, X_MAX + 1)])]
    part2 = 0
    for cp in check_points:
        dir, starts = cp
        for start in starts:
            part2 = max(part2, bfs(puzzle, start, dir))
    return part1, part2

puzzle, X_MAX, Y_MAX = read_puzzle('d16.txt')
print("Task 1/2", solve(puzzle))