import copy, re, functools
def read_puzzle(file):
    out = []
    for line in open(file).read().splitlines():
        cond_record, groups = line.split()
        groups = tuple(map(int,groups.split(",")))
        out.append([cond_record, groups])
    return out

def test_arrangement(test, groups):
    test2 = copy.copy(test)
    test = re.findall("[#?]+", test)
    check2 = [len(s) for s in test]
    result = True if "?" in test2 else len(check2) == len(groups)
    if result:
        for sub, a,b in zip(test, check2, groups):
            if not "?" in sub:
                if a != b:
                    result = False
                    break
            else:
                break
    return result

def find_arrangement(cond_record, groups):
    results = set()
    results.add(cond_record)
    weiter = "?" in cond_record
    inx_old = inx = 0
    
    while weiter:
        weiter = False
        temp = set()
        if inx_old != inx:
            print(inx)
            inx_old = inx
        while results:
            cond_record = results.pop()
            if not "?" in cond_record: 
                temp.add(cond_record)
                if test_arrangement(cond_record, groups):temp.add(cond_record)
                continue
            else:
                weiter = True
                inx = cond_record.index("?")
                test1 = copy.copy(cond_record)
                test2 = copy.copy(cond_record)
                #print("inx",inx)
                test1 = cond_record[0:inx]+ "#" + cond_record[inx+1:]
                test2 = cond_record[0:inx]+ "." + cond_record[inx+1:]
                if test_arrangement(test1, groups):temp.add(test1)
                if test_arrangement(test2, groups):temp.add(test2)
        results = results.union(temp)
    return results

# the solution was inspirated by Gravitar 64
# see: https://github.com/Gravitar64/Advent-of-Code-2023/blob/main/day12.py
# importand for part2
# saves known solution for lower arguments -> strong reduction of the necessary amount of calculation
# the function parameter are used as a key for an internal dictionary.
# if the function is called with arguments wich is saved in the dictonary, then the dict value 
# is returned instead of the whole function is calculated.
@functools.cache
def amounts(conds, gr):
    # eliminate all leading "." (have no influence)
    conds = conds.lstrip(".")

    # conds are empty: 
    #  -> gr is empty: counting is successfully -> return 1 (current search str is a valid combination)
    #  -> else: proof of failed -> current combination is invalid -> return 0
    if not conds: return not gr

    # groups are empty
    # when the "rest" conds contains only "?" or "." -> return 1 (its a valid combination)
    # but when the "rest" conds contains one ore more "#" -> conds/gr doesnt match -> return 0
    if not gr: return not "#" in conds
    
    ## if the first chare is a "#"
    if conds[0] == '#':
        # invalid condtions are (means: the current combination is invalid -> return 0)
        # - the rest conds has fewer chars as the first number in gr
        #   len(conds) < gr[0]
        # - there are no gr[0] consecutive # possible (the max amount of possibe # is to small)
        #  ('.' in conds[:gr[0]])
        #           <------- gr[0] ---------->
        # conds:    #******.******************       *: # or ?
        # - the minimal amount of possible # is to big (conds[gr[0]] == '#')
        #           <------- gr[0] --------->
        # conds:    #************************#       *: # or ?
        if  len(conds) < gr[0] or '.' in conds[:gr[0]] or conds[gr[0]] == '#': 
            return 0
        # now: all checks are passed, the number gr[0] is proceeded, also the 
        # next gr[0] chars from conds are proceeded
        # examine the amounts for the rest of conds and gr
        return amounts(conds[gr[0] + 1:], gr[1:])

    # first char is a "?"
    # -> ? is replaced with a "#" and a "." (result = sum of two counts)
    # no numbers from gr are used up here
    return amounts("#"+ conds[1:], gr) + amounts(conds[1:], gr)

def solve1(puzzle):
    n1 = n2 = 0
    for line in puzzle:
        cond_record, groups = line
        # avoid an error if an index acces after the end of line -> add a neutral "." 
        n1 += (amounts(cond_record+".", groups))
        conds2 = ((cond_record+"?")*4)+cond_record
        groups2 = groups * 5
        n2 += (amounts(conds2+".", groups2))
    return n1, n2

puzzle = read_puzzle('d12.txt')

print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))