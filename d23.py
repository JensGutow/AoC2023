#Dijkstra
import heapq
def read_puzzle(file):
    start = None
    end = None
    d = dict()
    for y, line in  enumerate(open(file).readlines()):
        for x, c in enumerate(line.strip()):
            if not start and c == ".": start=(x,y)
            d[(x,y)] = (0,None,c)
        end = (line.index("."),y)
    for pos in d:
        dist, prec, c = d[pos]
        dist = (x+1)*(y+1)
        d[pos] = (dist, prec, c)
    return d, x,y,start, end

DIR_SOPE = {(1,0):">", (-1,0):"<", (0,1):"v", (0,-1):"^"}

def solve1(puzzle):
    d, maxx, maxy,start, end = puzzle
    visited = set()
    queue = []
    heapq.heappush(queue, ((maxx+1)*(maxy+1), start))
    while queue:
        dist, pos = heapq.heappop(queue)
        if pos in visited: continue
        if pos == end: break
        visited.add(pos)
        x,y = pos
        dist_new = dist - 1
        for delta in [(1,0),(-1,0),(0,1),(0,-1)]:
            dx,dy = delta
            point_new = (x+dx,y+dy)
            if point_new not in d: continue
            dist_check, _, c = d[point_new]
            if c == "#": continue
            if c != "." and c!=DIR_SOPE[delta] :continue
            if dist_new < dist_check:
                d[point_new] =(dist_new, pos, c)
            heapq.heappush(queue, (dist_new, point_new))   
    return (maxx+1)*(maxy+1) - d[end][0]

puzzle = read_puzzle('d23.txt')

print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))