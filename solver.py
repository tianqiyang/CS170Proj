import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
import sys
import os
import matplotlib.pyplot as plt
from solve0 import algo0
from solve1 import algo1
from solve2 import algo2
from solve3 import algo3
from solve4 import algo4
from solve5 import algo5

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
    func = [algo0, algo1, algo2, algo3, algo4, algo5]
    if testing:
        path = 'medium-258.in'
        G = read_input_file('inputs/' + path)        
        Ts = [i(G.copy()) for i in func]
        print(path)
        for t in range(len(Ts)):
            print("{}   distance: {}".format(t, average_pairwise_distance(Ts[t])))
        T = findMin(Ts)
        assert is_valid_network(G, T)
        print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
    else:
        files = [filename for root, dirs, file in os.walk("./inputs") for filename in file ]
        for f in files:
            G = read_input_file("./inputs/" + f)
            print(f)
            Ts = [i(G.copy()) for i in func]
            T = findMin(Ts)
            for t in range(len(Ts)):
                print("{}   distance: {}".format(t, average_pairwise_distance(Ts[t])))
            assert is_valid_network(G, T)
            print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
            write_output_file(T, f'out/{f.replace(".in", ".out")}')
        files = [filename for root, dirs, file in os.walk("./out") for filename in file ]
        print(len(files))
