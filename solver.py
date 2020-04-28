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

if __name__ == '__main__':
    testing = True
    if testing:
        path = 'small-160.in'
        G = read_input_file('inputs/' + path)
        T = algo1(G)
        print(path)
        print('Valid tree:', is_valid_network(G, T))
        print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
    else:
        files = [filename for root, dirs, file in os.walk("./inputs") for filename in file ]
        for f in files:
            G = read_input_file("./inputs/" + f)
            print(f)
            T = solve1(G)
            assert is_valid_network(G, T)
            print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
            print()
            write_output_file(T, f'out/{f.replace(".in", ".out")}')
        files = [filename for root, dirs, file in os.walk("./out") for filename in file ]
        print(len(files))
