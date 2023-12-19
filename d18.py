import math
def read_puzzle(file):
    cmds = []
    for line in  open(file).read().splitlines():
        parts = line.split()
        cmds.append((parts[0], int(parts[1]), parts[2]))
    return cmds

R = [1,0]
D = [0,1]
U = [0,-1]
L = [-1,0]

DIRS = {0:"R", 1:"D", 2:"L", 3:"U"}

# trapezformel für polygone: https://de.wikipedia.org/wiki/Polygon#Fl%C3%A4che
def calc_area(coords):
    l = len(coords)
    a = 0
    for i in range(l):
        x2 = coords[i][0]
        x1 = coords[(i+1)%l][0]
        y2 = coords[i%l][1]
        y1 = coords[(i+1)%l][1]
        a += ((y1+y2)*(x2-x1))
    return a/2

def calc_distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    dx = x2 - x1
    dy = y2 -y1
    return math.sqrt(dx*dx + dy*dy)

def calc_length(coords):
    l = 0
    le = len(coords)
    for i in range(le):
        l += calc_distance(coords[i], coords[(i+1)%le])
    return l

def solve1(puzzle, part1=True):
    x, y = 0, 0
    coords = []
    for dir, dist, color in puzzle:
        if not part1:
            dist = int(color[2:7], 16)
            dir = DIRS[int(color[7], 16)]    
        dx, dy = eval(dir)
        x += dx * dist
        y += dy * dist
        coords.append((x,y))
    a = calc_area(coords)
    l = calc_length(coords)
    return int(a + l/2 + 1)
puzzle = read_puzzle('d18.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve1(puzzle, part1=False))