import re 
from collections import defaultdict

def read_puzzle(file):
    return "".join(open(file).read().splitlines()).split(",")

class Box:
    def __init__(self, i):
        self.box_nr = i
        self.objectives = defaultdict(int)

    def update(self, label, focus):
        self.objectives[label] = focus

    def delete(self, label):
        self.objectives.pop(label, None)

    def getFocus(self):
        return (self.box_nr+1)*(sum([v*(j+1) for j, v in enumerate(self.objectives.values())]))

    def __str__(self):
        s=""
        if self.objectives:
            s += "Box " + str(self.box_nr) +":"
            for label in self.objectives.keys():
                s += "["+ label + str(self.objectives[label]) +"] "
            s+="\n"
        return s 
    
def calcHash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v = v % 256
    return v

def solve1(puzzle):
    return sum([calcHash(s) for s in puzzle])

def print_boxes(boxes, p):
    print("after ", p)
    for i, box in enumerate(boxes):
        print(box, end="")

def solve2(puzzle):
    boxes = [Box(i) for i in range(256)]
    for p in puzzle:
        label = re.findall("[a-zA-Z]+",p)[0]
        box_nr = calcHash(label)
        if  "=" in p:
            objectiv = int(re.findall("[\d]+",p)[0])
            boxes[box_nr].update(label, objectiv)
        else:
            boxes[box_nr].delete(label)
        #print_boxes(boxes, p)
    return sum([box.getFocus() for box in boxes])
        
puzzle = read_puzzle('d15.txt')

print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))