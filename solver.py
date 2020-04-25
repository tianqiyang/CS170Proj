import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
import sys
import os
import matplotlib.pyplot as plt

def draw(G):
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.subplot(122)
    nx.draw_shell(G, with_labels=True, font_weight='bold')
    plt.show()

def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """
    copy = G.copy()
    covered = {}
    T = []
    for i in sorted(list(G.nodes), key=lambda x: len(G[x]), reverse=True):
        if i not in covered:
            T.append(i)
            for v in G[i]:
                covered[v] = 1
    if (len(T) == 1):
        onlyone = nx.Graph()
        onlyone.add_node(T[0])
        return onlyone
    pos = set()
    for i in range(len(T)):
        for j in range(i+1, len(T)):
            temp = nx.shortest_path(G, source=T[i], target=T[j])
            for t in temp:
                pos.add(t)
    print(pos)
    copy = G.copy()
    for re in copy:
        if re not in pos:
            G.remove_node(re)
    tree = nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')
    if len(tree) == 0 or len(G.nodes) == 0:
        onlyone = nx.Graph()
        onlyone.add_node(list(copy.nodes)[0])
        return onlyone
    return tree


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    testing = False
    if testing:
        path = 'inputs/small-19.in'
        G = read_input_file(path)
        #draw(G)
        T = solve(G)
        assert is_valid_network(G, T)
        print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
        #write_output_file(T, 'out/25.in')
    else:
        files = [filename for root, dirs, file in os.walk("./inputs") for filename in file ]
        print(len(files))
        for f in files:
            G = read_input_file("./inputs/" + f)
            print(f)
            T = solve(G)
            assert is_valid_network(G, T)
            print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
            print()
            write_output_file(T, f'out/{f.replace(".in", ".out")}')
        files = [filename for root, dirs, file in os.walk("./out") for filename in file ]
        print(len(files))
