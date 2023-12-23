import copy
import heapq
def read_puzzle(file):
    start = None
    end = None
    d = dict()
    for y, line in  enumerate(open(file).readlines()):
        for x, c in enumerate(line.strip()):
            if not start and c == ".": start=(x,y)
            d[(x,y)] = c
        end = (line.index("."),y)
    assert(x==y)
    return d, x,start, end

DIR_SOPE = {(1,0):">", (-1,0):"<", (0,1):"v", (0,-1):"^"}

def get_max_path_len(path, end, d, maxy):
    if path[-1] == end: return len(path)

    max_len = len(path)
    point = path[-1]
    x,y = point
    path2 = copy.copy(path)
    new_points = []
    append = True
    consecutive_points = []
    while append:
        append = False
        for delta in [(1,0),(-1,0),(0,1),(0,-1)]:
            dx,dy = delta
            point_new = (x+dx,y+dy)
            if point_new not in d: continue
            if point_new in path: continue
            if point_new in consecutive_points: continue
            c = d[point_new]
            if c == "#": continue
            #if c != "." and c!=DIR_SOPE[delta] :continue
            new_points.append(point_new)
            if point_new == end: 
                return max_len + len(new_points) + len(consecutive_points)
        if len(new_points)==0:return 0
        if len(new_points) == 1:
            append = True
            x, y = new_points.pop()
            consecutive_points.append((x,y))
    path2.extend(consecutive_points)
    for new_p in new_points:
        path2.append(new_p)        
        max_len = max(max_len, get_max_path_len(path2,end,d,maxy))
        path2.pop(-1)
    return max_len


def solve1(puzzle):
    d, maxxy, start, end = puzzle

    max_len = get_max_path_len([start], end,d, maxxy)
    return max_len-1


puzzle = read_puzzle('d23.txt')

print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))