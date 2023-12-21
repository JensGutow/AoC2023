import copy 
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial

def read_puzzle(file):
    d = set()
    S = None
    xmax = ymax = 0
    for y, line in enumerate(open(file).read().splitlines()):
        for x, c in enumerate(line):
            coord = x + y*(0+1j)
            if c == "S": 
                S = coord
                d.add(coord)
            if c == ".": 
                d.add(coord)
        xmax = x
    ymax = y
    return S, d, xmax+1, ymax+1

N = 0-1j
E = 1+0j
S = 0+1j
W = -1+0j

def solve1(puzzle):
    s, navi,xmax, ymax = puzzle
    edge = set()
    edge.add(s)
    for i in range(64):
        edge2 = set()
        for point in edge:
            for d in [N,E,S,W]:
                test = d+point
                if test not in navi: continue
                edge2.add(test)
        edge = copy.copy(edge2)
    return len(edge)

def solve2(puzzle):
    s, navi,xmax, ymax = puzzle
    edge = set()
    edge.add(s)
    part2 = 0
    points=[]
    steps2 = 26501365
    for i in range(steps2):
        edge2 = set()
        for point in edge:
            for d in [N,E,S,W]:
                test = d+point
                test_navi = (test.real%xmax)+(test.imag%ymax)*1j
                if test_navi not in navi: continue
                edge2.add(test)
        edge = copy.copy(edge2)
        if i%xmax == steps2%xmax:
            print("point ", len(points), "found", " i=",i," value=",len(edge))
            points.append(len(edge))
            if len(points)==3:
                poly = lagrange([0,1,2], points)
                part2 = Polynomial(poly.coef[::-1])(26501365//xmax)
                break     
    return part2

puzzle = read_puzzle('d21.txt')
p = copy.deepcopy(puzzle)
print("Task 1", solve1(puzzle))
print("Task 2", solve2(p))