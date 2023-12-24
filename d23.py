
from collections import defaultdict
    
def read_puzzle(file):
    input = open(file).readlines()
    ymax = len(input)
    xmax = len(input[0].strip())
    line = input[0].strip()
    start = line.index(".") + 0j
    line = input[-1]
    end = line.index(".") + (ymax-1)*(1j)

    assert(xmax == ymax)

    d = dict()
    for y, line in  enumerate(input):
        for x, c in enumerate(line.strip()):
            d[(x+y*(1j))] = c

    return d, xmax,start, end

DIR_SOPE = {(1+0j):">", (-1+0j):"<", (0+1j):"v", (0-1j):"^"}

NBS = {">" :[(1+0j)], "<" :[(-1+0j)],"v" :[(0+1j)],"^" :[(0-1j)],
        ".":[(1+0j),(-1+0j),(0+1j),(0-1j)]}

def get_nbs(c, part1):
    if part1:
        NBS = {">" :[(1+0j)], "<" :[(-1+0j)],"v" :[(0+1j)],"^" :[(0-1j)],
        ".":[(1+0j),(-1+0j),(0+1j),(0-1j)]}
        return NBS[c]
    else:
        return [(1+0j),(-1+0j),(0+1j),(0-1j)]


def get_points(d, start, end, part1):
    stack = [start]
    visited = []
    points = [start, end]
    while stack:
        point = stack.pop()
        if point in visited: continue
        visited.append(point)
        n = 0
        for dir in get_nbs(d[point], part1):
            point_n = point + dir
            if point_n in d and point_n not in visited and d[point_n]!="#": 
                stack.append(point_n)
                n += 1
        if n>=2: 
            points.append(point)
    return points

def build_graph(d, points, part1):
    graph = defaultdict(dict)
    for point in points:
        graph[point] = dict()
        visited = []
        stack = [(0, point)]
        while stack:
            n, point_n = stack.pop()
            if point_n in visited: continue
            visited.append(point_n)
            for dir in get_nbs(d[point_n], part1):
                point_k = point_n + dir
                if point_k in d and point_k not in visited and d[point_k]!="#": 
                    if point_k not in points:
                        stack.append((n+1, point_k))
                    else:
                        graph[point][point_k] = n + 1
    print("GRAPH")
    for pt in graph:
        print("(",pt.real,",",pt.imag,"): ",end="" )
        for 
    return graph

END = ()
VISITED = set()
GRAPH = dict()
def get_max_path_len(point):
    if point == END : return 0
    l = 0
    VISITED.add(point)
    for pt in GRAPH[point]:
        if pt in VISITED: continue
        l = max(get_max_path_len(pt), GRAPH[point][pt])
    VISITED.remove(point)
    return l

def solve1(puzzle, part1):
    global GRAPH, END
    d, maxxy, start, end = puzzle
    points = get_points(d, start, end, part1)
    print("points:", len(points))
    graph = build_graph(d, points, part1)
    print("graph", len(graph))
    END = end
    GRAPH = graph
    l =  get_max_path_len(start)
    return l


puzzle = read_puzzle('d23.txt')

print("Task 1", solve1(puzzle, part1 = True) )
print("Task 2", solve1(puzzle, part1 = False))