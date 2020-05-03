import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
from helperFunctions import oneNode, draw, draw2
import sys
import os
from solve0 import algo0
from solve1 import algo1
from solve2 import algo2
from solve3 import algo3
from solve4 import algo4
from solve5 import algo5
from solve6 import algo6
from solve7 import algo7
from solve8 import algo8

func = [algo0, algo1, algo2, algo3, algo4, algo5, algo6, algo7]

def findMin(li):
    return min(li, key=lambda x: average_pairwise_distance(x))

def findTree(G):
    # it is a cycle
    try:
        ls = nx.find_cycle(G)
        if len(ls) == len(G.edges):
            return algo8(G)
    except:
        pass
    n = len((G.nodes))
    nodes = sorted(list(G.nodes), key=lambda x: len(G[x]), reverse=True)
    # one node connect to all nodes
    if len(G[nodes[0]]) == n or len(G[nodes[0]]) == n - 1:
        return oneNode(G, nodes)
    Ts = []
    for t in range(len(func)):
        Ts.append(func[t](G.copy()))
        value = average_pairwise_distance(Ts[t])
        print("{} distance: {}".format(t, value))
        if value == 0:
            return Ts[-1], t
    T = findMin(Ts)
    return T

if __name__ == '__main__':
    #testing = False
    # if testing:
    #     path = 'small-4.in'
    #     G = read_input_file('inputs/' + path)        
    #     print(path)
    #     T = findTree(G)
    #     assert is_valid_network(G, T)
    #     print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
    # else:
    if True:
        files = sorted([filename for root, dirs, file in os.walk("./inputs") for filename in file], key=lambda x: int(x.replace('large-', '').replace('small-', '').replace('medium-', '').replace('.in', '')))
        for count, f in enumerate(files, 1):
            G = read_input_file("./inputs/" + f)
            print(count)
            print(f)
            T = findTree(G)
            assert is_valid_network(G, T)
            print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
            write_output_file(T, f'out/{f.replace(".in", ".out")}')
        files = [filename for root, dirs, file in os.walk("./out") for filename in file ]
        print(len(files))