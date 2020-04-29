import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
import sys
import os
import matplotlib.pyplot as plt
from solve1 import algo1
from solve2 import algo2
from solve3 import algo3
from solve4 import algo4

def draw(G):
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.subplot(122)
    nx.draw_shell(G, with_labels=True, font_weight='bold')
    plt.show()

# Usage: python3 solver.py
def findMin(li):
    return min(li, key=lambda x: average_pairwise_distance(x))

if __name__ == '__main__':
    testing = True
    if testing:
        path = 'large-193.in'
        G = read_input_file('inputs/' + path)
        T0 = nx.minimum_spanning_tree(G.copy(), weight='weight')
        T1 = algo1(G.copy())
        T2 = algo2(G.copy())
        # T3 = algo3(G.copy())
        # T4 = algo4(G.copy())
        print(path)
        print("0   distance: {}".format(average_pairwise_distance(T0)))
        print("1   distance: {}".format(average_pairwise_distance(T1)))
        print("2   distance: {}".format(average_pairwise_distance(T2)))
        # print("3   distance: {}".format(average_pairwise_distance(T3)))
        Ts = [T0, T1, T2]
        T = findMin(Ts)
        assert is_valid_network(G, T)
        print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
    else:
        files = [filename for root, dirs, file in os.walk("./inputs") for filename in file ]
        for f in files:
            G = read_input_file("./inputs/" + f)
            print(f)
            T0 = nx.minimum_spanning_tree(G.copy(), weight='weight')
            T1 = algo1(G.copy())
            T2 = algo2(G.copy())
            # T3 = algo3(G)
            Ts = [T0, T1, T2]
            T = findMin(Ts)
            assert is_valid_network(G, T)
            print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
            write_output_file(T, f'out/{f.replace(".in", ".out")}')
        files = [filename for root, dirs, file in os.walk("./out") for filename in file ]
        print(len(files))
