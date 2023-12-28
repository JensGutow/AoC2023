import re, math
import itertools
from sympy import symbols, Eq, solve
def read_puzzle(file):
    hairs = []
    for i, line in enumerate(open(file).readlines()):
        hairs.append(list(map(int, re.findall("-?[\d]+", line))))
    return hairs

def transform_to_mn_form(line):
    x,y,z, vx, vy, vz = line
    m = vy/vx
    n = y-(x*(vy/vx))
    return (m,n) 

PARALLEL = 1
IDENTICAL = 2
CROSSINGS = 3
def calc_crossing(l1, l2):
    x1,y1,z1,vx1,vy1,vz1 = l1
    x2,y2,z2,vx2,vy2,vz2 = l2
    m1,n1, = transform_to_mn_form(l1)
    m2,n2, = transform_to_mn_form(l2)
    if m1==m2:
        if n1 == n1 : 
            if (x1,y1,vx1,vy1)==(x2,y2,vx2,vy2):
                print("parallele lines:",)
                print("    l1")
                print("    l1")
                print()
            return (IDENTICAL, (m1,n1), (x1,y1,vx1,vy1)==(x2,y2,vx2,vy2))
        else: 
            return (PARALLEL, None, False)
    else: 
        x = (n2-n1)/(m1-m2)
        y = m1*x + n1
        t1 = (x-x1)/vx1
        t2 = (x-x2)/vx2
        return (CROSSINGS,(x,y), (t1>=0) and (t2>=0))

def solve1(puzzle):
    range = [200000000000000,400000000000000]
    n = 0
    rmin, rmax = range
    for l1, l2 in list(itertools.combinations(puzzle, 2)):
        check = calc_crossing(l1,l2)
        if check[0] == PARALLEL: 
            pass
        elif check[0] == IDENTICAL: 
            if check[2]:
                n += 1
        else:
            x,y =  check[1]
            if (rmin <= x <= rmax) and (rmin <= y <= rmax):
                if check[2]:
                    n +=1
    return n

def eq(x, i):
    eq_l = f"{x}+V{x}*t{i}"
    eq_r = f"{x}st+V{x}st*t{i}"
    return eq_l, eq_r

def std_v(vect):
    l = math.sqrt(sum([v*v for v in vect]))
    k = 1 if vect[0]>0 else -1
    v2 = [v*k/l for v in vect ]
    return v2

def solve2(puzzle):
    l = len(puzzle)
    Xst, Yst, Zst, VXst, VYst, VZst, t0, t1, t2 = symbols("Xst Yst Zst VXst VYst VZst t0 t1 t2")
    eqs = []
    i = 0
    v_vectors = []
    j = 0
    while i < 3:
        X, Y, Z, VX, VY, VZ = puzzle[j]
        j += 1
        sv = std_v([VX,VY,VZ])
        if sv in v_vectors: continue
        v_vectors.append(sv)
        for v in "XYZ":
            eq_l, eq_r = eq(v,i)
            eqs.append(Eq(eval(eq_l),eval(eq_r)))
        i += 1
    solution = solve(tuple(eqs), (Xst, Yst, Zst, VXst, VYst, VZst, t0, t1, t2))
    return sum(solution[0][:3])


puzzle = read_puzzle('d24.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))