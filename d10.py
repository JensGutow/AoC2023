import heapq

Y_MAX = X_MAX = 0

def read_puzzle(file):
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


DIRS = "NESW"
DIRS_BY_PIPE = {"-":"EW","|":"SN","F":"SE","J":"NW","L":"NE","7":"WS"}
MOVES = {"N":(0,-1), "E":(1,0),"S":(0,1),"W":(-1,0)}
PIPES = "S-|FJL7"
NEXT_PIPES ={"E":"J7-", "S":"J|L", "W":"-LF", "N":"|7F"}

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
        x1_mod = x1%X_MAX
        y1 = (y + deltay)
        y1_mod = y1%Y_MAX
        if (x1_mod, y1_mod) in pipes:
            c = pipes[(x1_mod,y1_mod)] 
            if c in NEXT_PIPES[dir]:
                next_items.add((x1,y1))
                if (x1,y1) not in pipes:
                    pipes[(x1,y1)] = c
                    print("add ",x1,y1)
    return next_items

print_pipes = dict()
def print_counts(queue):
    pipes = dict()
    for item in queue:
        count, pos = item 
        print_pipes[pos] = count
    for y in range(Y_MAX):
        l = ""
        for x in range(Y_MAX):
            c = print_pipes[(x,y)] if (x,y) in print_pipes else "."
            l += str(c)
        print(l)
    print("")
    return
    

def solve1(puzzle):
    start, pipes = puzzle
    visited = set()
    queue = []
    pos = start
    replace_S(start, pipes)
    heapq.heappush(queue, (0, pos))
    max_pos = (0,0)
    max_count = 0
    n1 = 0
    while queue:
        count, pos = heapq.heappop(queue)
        count += 1
        if pos in visited: continue
        visited.add(pos)
        for item in get_next_items(pipes, pos):
            if item in visited: continue
            heapq.heappush(queue, (count, item))
            if count > max_count:
                max_count = count
                max_pos = item
            #print_counts(queue)
    return max_pos, max_count

puzzle = read_puzzle('d10.txt')

print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))