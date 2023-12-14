import re
def read_puzzle(file):
    return open(file).read().splitlines()
 
# Richtung -> (drehen Matrix, drehen linie)
dirs = {"N":(True, False), "S":(True, True), "W":(False, False), "E":(False, True)}
 
def tilt_mirror(mirrors, dir):
    trnsp_mirrors, trnsp_line = dir
    if trnsp_mirrors: mirrors = list(zip(*mirrors))
    for i, line in enumerate(mirrors):
        line = "".join(line)
        if trnsp_line:
            line = "".join(list(reversed(line)))
        weiter = True
        while weiter:
            weiter = False
            matches = [match for match in re.finditer("[.]+[O]+",line)]
            if matches:
                match = matches[-1]
                weiter = True
                e = match.end()
                s = match.start()
                temp = line[s: e]
                n = temp.count("O")
                temp = "O"*n + "."*(e-s-n)
                line = line[:s]+temp+line[e:]
        if trnsp_line: line = "".join(list(reversed(line)))
        mirrors[i] = line
    if trnsp_mirrors: mirrors = list(zip(*mirrors))
    mirrors = ["".join(line) for line in mirrors]
    return mirrors
 
def count_load(mirrors):
    count = 0
    n = len(puzzle)
    for i, line in enumerate(mirrors):
        count += n * line.count("O")
        n -= 1
    return count
   
 
def solve1(puzzle):
    puzzle = tilt_mirror(puzzle, dirs["N"])
    n = count_load(puzzle)
    return n
 
def solve2(puzzle):
    MAX = 1000000000
    count = 0
    checker = []
    for i in range(MAX):
        for dir in "NWSE":
            puzzle = tilt_mirror(puzzle, dirs[dir])
        count = count_load(puzzle)
        hash_value = (count, hash(tuple(puzzle)))
        #print("i", i, " hash", hash_value, " count", count)
        if hash_value not in checker:
            checker.append(hash_value)
        else:
            j = checker.index(hash_value)
            zyklusL = i-j
            k = (MAX-1-j) % zyklusL
            index = k + j
            count,_  = checker[index]
            return count
    return 0
        
 
puzzle = read_puzzle("d14.txt")
print("Task1:", solve1(puzzle))
print("Task2:", solve2(puzzle))
