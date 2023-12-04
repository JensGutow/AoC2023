import re, math
def read_puzzle(file):
    return open(file).read().splitlines()

def solve(puzzle):
    cards = []
    s1 = 0
    for i, line in enumerate(puzzle):
        line = line.split(":")[1]
        line = line.split("|")
        winning_nr = set(map(int, re.findall("\d+", line[0])))
        my_nr = set(map(int, re.findall("\d+", line[1])))
        n = len(winning_nr&my_nr) 
        s1 += 1 << n-1 if n>0 else 0
        cards.append([i, 1, n])
    l = len(cards)
    for i, card in enumerate(cards[0:-1]):
        if (card[2]):
            _, k, n = card
            e = min(l, i+n+1)
            for j in range(i+1, e):
                cards[j][1] += k
    n =  sum([card[1] for card in cards])
    return s1, n

puzzle = read_puzzle('d4.txt')

print("Task 1/2", solve(puzzle))