import copy, re
def read_puzzle(file):
    out = []
    for line in open(file).read().splitlines():
        cond_record, groups = line.split()
        groups = list(map(int,groups.split(",")))
        out.append([cond_record, groups])
    return out

def test_arrangement(test, groups):
    test2 = copy.copy(test)
    test = re.findall("#[#?]*", test)
    check2 = [len(s) for s in test ]
    if "?" in test2:
        result  = len(check2) <= len(groups)
    else:
        result  = len(check2) == len(groups)
    if result:
        for sub, a,b in zip(test, check2, groups):
            if "?" in sub:
                sub_check = re.findall("#+", sub)
                if sub_check:
                    if len(sub_check[0]) > b:
                        result = False
            else:
                result = a == b
            if not result: break
    else:
        pass
    #print(test2, result, groups)
    return result

def find_arrangement(line):
    cond_record, groups = line
    #print("org")
    #print(cond_record, groups)
    #print("---")
    results = set()
    results.add(cond_record)
    weiter = "?" in cond_record

    while weiter:
        weiter = False
        temp = set()
        #print("-----------------")
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
        #print(inx)

    return results


def solve1(puzzle):
    n = 0
    for line in puzzle:
        menge = find_arrangement(line)
        print(len(menge))
        n += len(menge)
    return n

puzzle = read_puzzle('d12.txt')

print("Task 1", solve1(puzzle))
#print("Task 2", solve1(puzzle))