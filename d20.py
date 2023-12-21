from collections import defaultdict
import copy, math
LOW = 0
HIGH = 1

# connections:  dictonary [node_from]:node_to
# nodes: dictonary [node]: [type, content]
#   type:  (b) broadcast, (%) FlipFlop, (&)Conjunction
#   content:
#       if type == % : 
#           LOW or HIGH = node-status
#       if type == &
#           save the pulse status from all the "from_nodes"
#           dictonary: [node_from]: bool (last pulse from the node "node_from")

def read_puzzle(file):
    nodes = dict()
    connections=defaultdict(list)
    for line  in open(file).readlines():
        left, right = line.strip().split(" -> ")
        rigths = right.strip().split(", ")
        type = left[0]
        name = left[1:] if type != "b" else left
        nodes[name] = [type, dict()]
        for r in rigths:
            connections[name].append(r) 
    for node_from, nodes_to in connections.items():
        for node_to in nodes_to:
            if node_to in nodes:
                nodes[node_to][1][node_from] = LOW
            else:
                nodes[node_to] = ["e", {node_from:0}]
    for key in nodes.keys():
        type, l = nodes[key]
        if type == "%": nodes[key]= [type, LOW]

    return nodes, connections

def handle_commands(nodes, connections, cmds, test_nodes):
    n_low = 1
    n_high = 0
    result = [0]*4
    while cmds:
        node_from, nodes_to, pulse = cmds.pop(0)
        if node_from in test_nodes and pulse:
            result[test_nodes.index(node_from)] = 1
        for node_to in nodes_to:
            if pulse: n_high+=1
            else: n_low+=1
            type, inputs = nodes[node_to]
            if type == "%":
                if pulse == LOW:
                    inputs = not inputs #change pulse state
                    nodes[node_to] = [type, inputs]
                    cmds.append([node_to, connections[node_to], inputs])
            elif type == "&":
                inputs[node_from] = pulse
                all_1 =  all(list(inputs.values()))
                cmds.append([node_to, connections[node_to], not all_1])

    return result

def solve1(puzzle):
    nodes, connections = puzzle
    n1 = n2 = 0
    for _ in range(1000):
        cmds = [("broadcaster", connections["broadcaster"], LOW)]
        n1_t,n2_t = handle_commands(nodes, connections, cmds)
        n1 += n1_t
        n2 += n2_t
    return n1 * n2

def solve2(puzzle):
    nodes, connections = puzzle
    n1 = n2 = 0
    test_nodes = "rp","lb",	"nj","cl"

    i = 0
    l = 0
    timings= [[], [], [], []]
    while True:
        i+=1
        cmds = [("broadcaster", connections["broadcaster"], LOW)]
        results = handle_commands(nodes, connections, cmds, test_nodes)
        if any(results):
            for inx, j in enumerate(results):
                if j:
                    timings[inx].append(i)
                    if min([len(item) for item in timings]) > 20:
                        l = [t[20] - t[19] for t in timings]
                        l = math.lcm(*l)
                        break    
    return l

puzzle = read_puzzle('d20.txt')
p2 = copy.deepcopy(puzzle)
#print("Task 1", solve1(puzzle))
print("Task 2", solve2(p2))