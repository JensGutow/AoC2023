import re 
def read_puzzle(file):
    return "".join(open(file).read().splitlines()).split(",")

def calcHash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v = v % 256
    return v

def solve1(puzzle):
    return sum([calcHash(s) for s in puzzle])

def update_objectiv(box, label, objectiv):
    labels, objectives = box
    if label in labels: 
        inx = labels.index(label)
        objectives[inx] = (label, objectiv)
    else:
        labels.append(label)
        objectives.append((label, objectiv))
    return (labels, objectives)

def remove_objectiv(box, label):
    labels, objectives = box
    if label in labels:
        inx = labels.index(label)
        labels.pop(inx)
        objectives.pop(inx)
    return (labels, objectives)

def print_boxes(boxes, p):
    print("after ", p)
    for i, box in enumerate(boxes):
        labels, objectives = box
        if labels:
            print("Box ", i,":", end="")
            for objectiv in objectives:
                label, nr = objectiv
                print("[", label, nr,"] ", end="")
            print("")
    print("")

def get_focus(boxes):
    focus = 0
    for b, box in enumerate(boxes):
        labels, objectives = box
        if labels:
            for o, objectiv in enumerate(objectives):
                _, focus_o = objectiv
                focus_lokal = (b+1)*(o+1)*focus_o
                focus += focus_lokal
    return focus

def solve2(puzzle):
    boxes = [([], []) for i in range(256)]
    for p in puzzle:
        label = re.findall("[a-zA-Z]+",p)[0]
        box_nr = calcHash(label)
        if  "=" in p:
            objectiv = int(re.findall("[\d]+",p)[0])
            box = update_objectiv(boxes[box_nr], label, objectiv)
        else:
            box = remove_objectiv(boxes[box_nr], label)
        boxes[box_nr] = box
        #print_boxes(boxes, p)
    return get_focus(boxes)
        


puzzle = read_puzzle('d15.txt')


print("Task 1", solve1(puzzle))
print("Task 2", solve2(puzzle))