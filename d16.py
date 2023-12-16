from collections import defaultdict

Y_MAX = X_MAX = 0
Y_MIN = X_MIN = 1e10 

# DIRS: "DIR":(dx,dy) : welche Richtung ein Strahl einer Richtung in einem Schritt ausführt
DIRS = {"N":(0,-1),"E":(1,0),"S":(0,1),"W":(-1,0)}

# keys: (DIR, C)
#    DIR: Strahlrichtung, die in eine Zelle reingeht
#      C: Codierung der Zelle (ein Zeichen aus "|-/\.")
# values:
#   Menge von möglichen Strahlrichtungen, wenn der Stahl die Zelle verlässt
BEAM_RULES = {("N", "|"):"N" , ("S", "|"):"S", ("E", "|"):"SN", ("W", "|"):"SN",
              ("N", "-"):"EW", ("S", "-"):"EW",("E", "-"): "E", ("W", "-"):"W",
              ("N", "/"):"E" , ("S", "/"):"W", ("E", "/"): "N", ("W", "/"):"S",
              ("N","\\"):"W" , ("S","\\"):"E", ("E","\\"): "S", ("W","\\"):"N",
              ("N", "."):"N" , ("S", "."):"S", ("E", "."): "E", ("W", "."):"W"
              }

def read_puzzle(file):
    return {(x,y):[c, set()] for y, line in enumerate(open(file).read().splitlines()) for x, c in enumerate(line)}

def update_limits(puzzle):
    global Y_MAX, Y_MIN, X_MAX, X_MIN
    for x,y in puzzle.keys():
        Y_MAX = max(Y_MAX, y)
        Y_MIN = min(Y_MIN, y)
        X_MAX = max(X_MAX, x)
        X_MIN = min(X_MIN, x)


def get_nb(puzzle, pos, dirs):
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

def print_energy_status(puzzle):
    for y in range(Y_MIN, Y_MAX + 1):
        line = ""
        for x in range(X_MIN, X_MAX + 1):
            _, dirs = puzzle[(x,y)]
            pattern = "#" if dirs else "."
            line += pattern
        print(line)

def get_energy(puzzle):
    return sum([1 for _, dirs in puzzle.values() if dirs])

def calc_energy(puzzle,start, dir):
    # modifizierte Breitensuche
    # puzzle: Dictonary (pos=x,y):(Zeichen, Richtungen von Strahlen, die die Zelle passiert haben)
    # start: (äussere) Zelle, die vom Strahl als erstes getroffen wird
    # dir: in welcher Richtung der Strahl verläuft
    visited = defaultdict(set) # pos:dirs
    queue = defaultdict(set) # pos:dirs
    queue[start] = dir
    while queue:
        pos = list(queue.keys())[0]
        dirs = queue.pop(pos)
        # nächsten Eintrag wenn:
        #   - es gibt einen "pos" Eintrag in visited UND
        #   - alle dirs sind dort schon eingetragen
        if set(dirs).issubset(visited[pos]): continue
        # Values vom puzzle dict sind: (das aktuelle Zeichen, bisherige Strahl-Richtungen)
        p_c, p_dirs = puzzle[pos]
        # update der Strahl-Richtungen im Puzzle (max. hinzufügen - nicht löschen)
        puzzle[pos] = (p_c, p_dirs.union(dirs))
        #optimierung: nur die die dirs behandeln, die nicht in visited[pos] enthalten sind
        dirs =  "".join(list((set(dirs) - set(visited[pos]))))
        visited[pos] = "".join(set(visited[pos]).union(dirs))
        for next_pos_dir in  get_nb(puzzle, pos, dirs):
            n_pos, n_dir = next_pos_dir
            # update der dirs für n_pos (wenn Eintrag existiert)
            # oder einen neuen Eintrag einfügen
            queue[n_pos] = queue[n_pos].union(set(n_dir))
    #print_energy_status(puzzle)
    return get_energy(puzzle)

def reset(puzzle):
    return {k:[v[0],set()] for k,v in puzzle.items()}

def solve1(puzzle):
    return calc_energy(puzzle, (0,0), "E")

def solve2(puzzle):
    check_points = [
    ("E", [(X_MIN, y) for y in range(Y_MIN, Y_MAX + 1)]),
    ("W", [(X_MAX, y) for y in range(Y_MIN, Y_MAX + 1)]),
    ("S", [(x, Y_MIN) for x in range(X_MIN, X_MAX + 1)]),
    ("N", [(x, Y_MAX) for x in range(X_MIN, X_MAX + 1)])
    ]

    energy_value = 0
    pos = None
    for cp in check_points:
        dir, starts = cp
        for start in starts:
            puzzle = reset(puzzle)
            ev = calc_energy(puzzle, start, dir) 
            if ev > energy_value:
                energy_value = ev
                pos = start
            print(dir, start, ev)

    return energy_value, pos

puzzle = read_puzzle('d16.txt')
update_limits(puzzle)
print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))