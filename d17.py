import heapq, copy

Y_MAX = X_MAX = Y_MIN = X_MIN = 0
N = 0-1j
E = 1+0j
S = 0+1j
W = -1+0j
OTHER_DIRS = {N:[E,W], E:[N,S], S:[E,W], W:[S,N]}

def read_puzzle(file):
    global Y_MAX, X_MAX
    p=open(file).read().splitlines()
    Y_MAX = len(p)
    X_MAX = len(p[0])
    # puzzle sind nodes pos: (GesamtKosten, Pos_Vorgänger, KostenImKnoten)
    # pos: imaginäre Zahl
    return {x+y*(0+1j):(1e10, None, int(c)) for y, line in enumerate(p) for x, c in enumerate(line)}

class Node:
    def __init__(self, distance, pos, dir, straight_len):
        self.distance = distance
        self.pos = pos
        self.dir = dir
        self.straight_len = straight_len

    def get_all(self):
        return (self.pos, self.dir, self.straight_len)

    def __lt__(self, other):
        return (self.distance - 0.5*abs(self.pos)) < (other.distance - 0.5*abs(self.pos))

def get_nbs(p, node, part1):
    pos, dir, straight_len = node.get_all()
    distance = node.distance
    nbs = []
    pos_new = pos
    
    if part1 or straight_len >= 4: 
        for dir_new in OTHER_DIRS[dir]:
            pos_new = pos + dir_new
            if pos_new in p:
                new_distance = distance + p[pos_new][2]
                nbs.append(Node(new_distance, pos_new, dir_new, 1))
    pos_new = pos
    max_len = 3 if part1 else 10
    if straight_len < max_len:
        pos_new += dir
        if pos_new in p:
            straight_len += 1
            distance += p[pos_new][2]
            nbs.append(Node(distance, pos_new, dir, straight_len))
    else:
        pass
    return nbs

def solve1(puzzle,part1):
    # puzzle sind nodes pos: (GesamtKosten, Pos_Vorgänger, KostenImKnoten)
    # pos = x+yj
    visited = set() # pos, dir, straight_len)
    queue = [] # pos, dir, straight_len)
    start = 0+0j
    end = (X_MAX-1) + (Y_MAX-1)*(0+1j)
    heapq.heappush(queue, Node(0, start, E, 0))
    heapq.heappush(queue, Node(0, start, S, 0))
    while(queue):
        node = heapq.heappop(queue)
        if node.get_all() in visited: continue
        visited.add(node.get_all())
        if node.pos == end:
            break

        for nb in get_nbs(puzzle, node, part1):
            if nb.get_all() in visited: continue 
            p_distance, p_pos_prec, p_local_costs = puzzle[nb.pos]
            if nb.distance < p_distance:
                p_distance = nb.distance
                puzzle[nb.pos] = (p_distance, node.pos, p_local_costs)   
            heapq.heappush(queue, nb)  
    return node.distance

puzzle = read_puzzle('d17.txt')
p2 = copy.deepcopy(puzzle)
print("Task 1", solve1(puzzle, True))
print("Task 2", solve1(p2, False))