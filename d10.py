import heapq

Y_MAX = X_MAX = 0
DIRS = "NESW"
DIRS_BY_PIPE = {"-":"EW","|":"SN","F":"SE","J":"NW","L":"NE","7":"WS"}
MOVES = {"N":(0,-1), "E":(1,0),"S":(0,1),"W":(-1,0)}
PIPES = "S-|FJL7"
NEXT_PIPES ={"E":"J7-", "S":"J|L", "W":"-LF", "N":"|7F"}

def read_puzzle(file, part1=True):
    global X_MAX
    global Y_MAX
    pipes = dict() # x,y: (Pipe, count)
    start = 0
    for y, line in enumerate(open(file).read().splitlines()):
        for x, c in enumerate(line):
            if c == "S":start = (x,y)
            if c in PIPES: pipes[(x,y)] = c
    X_MAX = x + 1
    Y_MAX = y + 1
    return start, pipes

def replace_S(start, pipes):
    valid_conn = {"SN":"|", "NS":"|", "WE":"-","EW":"-", 
                  "NE":"L", "EN":"L", "NW":"J", "WN":"J",
                  "SE":"F", "ES":"F", "SW":"7", "WS":"7"}
    valid_dirs = ""
    x, y = start
    for dir in DIRS:
        deltax, deltay = MOVES[dir]
        x1 = x+deltax
        y1 = y+deltay
        if (x1,y1) in pipes:
            c = pipes[(x1,y1)]
            if c in NEXT_PIPES[dir]:
                valid_dirs += dir
    start_replace = valid_conn[valid_dirs]
    pipes[start] = start_replace

def get_next_items(pipes, item):
    x, y = item
    next_items = set()
    for dir in DIRS_BY_PIPE[pipes[item]]:
        deltax, deltay = MOVES[dir]
        x1 = (x + deltax)
        y1 = (y + deltay)
        if (x1, y1) in pipes:
            c = pipes[(x1, y1)] 
            if c in NEXT_PIPES[dir]:
                next_items.add((x1,y1))
    return next_items
    
def get_cross_points(pipes, visited, x,y):
    n = 0
    for point in visited:
        xp, yp = point
        if y == yp and xp > x:
            c = pipes[point]
            if c in "|F7": n += 1
    return n
    
def solve1(puzzle):
    start, pipes = puzzle
    visited = set()
    queue = []
    pos = start
    replace_S(start, pipes)
    heapq.heappush(queue, (0, pos))
    while queue:
        count, pos = heapq.heappop(queue)
        count += 1
        if pos in visited: continue
        visited.add(pos)
        for item in get_next_items(pipes, pos):
            if item in visited: continue
            heapq.heappush(queue, (count, item))
    # part 2: Punkt-in-Polygon-Test nach Jordan 
    #wagerechte Linien: L---J  
    N = 0
    for x in range(X_MAX):
        for y in range(Y_MAX):
            if (x,y) in visited: continue
            n = get_cross_points(pipes, visited, x,y)
            if (n%2):
                N += 1
    return count, N
    
puzzle = read_puzzle('d10.txt')
print("Task 1", solve1(puzzle))