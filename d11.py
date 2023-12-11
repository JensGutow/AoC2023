from itertools import combinations
def read_puzzle(file):
    return open(file).read().splitlines() 

def dist(p1, p2, cols, rows, repeat):
    x1, y1 = p1
    x2, y2 = p2
    dx1 = abs(x2 - x1)
    dy1 = abs(y2 - y1)
    dx2 = len([1 for c in cols if min(x1,x2) < c < max(x1,x2)]) * repeat
    dy2 = len([1 for c in rows if min(y1,y2) < c < max(y1,y2)]) * repeat
    return dx1 + dx2 + dy1 + dy2

def solve1(puzzle):
    rows = [i for i,line in enumerate(puzzle) if "#" not in line]
    cols = [i for i,line in enumerate(zip(*puzzle)) if "#" not in line]
    galaxies  =  [(x,y)  for y, line in enumerate(puzzle) for x,c in enumerate(line) if c=="#" ]
    pairs = list(combinations(galaxies, 2))
    d1 =  sum([dist(g1,g2, cols, rows, 2-1)  for g1, g2 in pairs])
    d2 =  sum([dist(g1,g2, cols, rows, 1000000-1)  for g1, g2 in pairs])
    return d1, d2

puzzle = read_puzzle('d11.txt')

print("Task 1/2", solve1(puzzle))