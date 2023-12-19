import shapely
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
    poly = shapely.Polygon(coords)
    a = shapely.area(poly)
    l = shapely.length(poly)
    return int(a + l/2 + 1)
puzzle = read_puzzle('d18.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve1(puzzle, part1=False))