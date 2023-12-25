import copy, math
from collections import defaultdict
from itertools import combinations
import networkx.algorithms.connectivity.stoerwagner
import networkx as nx

# min cutoff problem
# -> Kargers algorithm
# -> Wagner Stoer algorithm
#    -> lib networx -> stoerwanger 
#   (https://networkx.org/documentation/networkx-2.4/reference/algorithms/generated/networkx.algorithms.connectivity.stoerwagner.stoer_wagner.html)

def read_puzzle(file):
    conns=set()
    nbs=defaultdict(set)
    comps = set()
    for line in open(file).readlines():
        left, right = line.strip().split(":")
        right = right.strip().split(" ")
        groups_conns = set()
        comps.add(left)
        for r in right:
            groups_conns.add(r)
            nbs[r].add(left)
            conns.add((left,r))
            comps.add(r)
        nbs[left] = nbs[left].union(groups_conns)
    return conns, nbs, comps

def get_group(comp, nbs):
    group = {comp}
    l = 0
    visited = set()
    while l != len(group):
        l = len(group)
        news = set()
        for c in group.difference(visited):
            news.add(c)
            group = group.union(nbs[c])
        visited = visited.union(news)
    return group


def solve1(puzzle):
    conns, nbs, comps = puzzle
    g = nx.Graph()
    for conn in conns:
        a,b = conn
        g.add_edge(a,b, weight=3)
    cut_value, partition = nx.stoer_wagner(g)
    return math.prod(list(map(len, partition)))


puzzle = read_puzzle('d25.txt')

print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))