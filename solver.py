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
from solve5 import algo5

def draw(G):
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.subplot(122)
    nx.draw_shell(G, with_labels=True, font_weight='bold')
    plt.show()

# Usage: python3 solver.py
def findMin(li):
    dic = {}
    for i in li:
        dic[i] = average_pairwise_distance(i)
    # print(average_pairwise_distance(li[0])-average_pairwise_distance(li[1]))
    return min(dic.keys(), key=lambda x: dic[x])

if __name__ == '__main__':
    testing = True
    if testing:
        path = 'large-160.in'
        G = read_input_file('inputs/' + path)
        T0 = nx.minimum_spanning_tree(G.copy(), weight='weight')
        # T1 = algo1(G.copy())
        # T2 = algo2(G.copy())
        # T3 = algo3(G.copy())
        # T4 = algo4(G.copy())
        T5 = algo5(G.copy())
        # print(path)
        # print('Valid tree1:', is_valid_network(G, T1))
        # print("0   distance: {}".format(average_pairwise_distance(T0)))
        # print("1   distance: {}".format(average_pairwise_distance(T1)))
        # print("2   distance: {}".format(average_pairwise_distance(T2)))
        # print("3   distance: {}".format(average_pairwise_distance(T3)))
        # print("5   distance: {}".format(average_pairwise_distance(T5)))
        # Ts = [T0, T2, T3, T5]
        # T = findMin(Ts)
        # print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
    else:
        files = [filename for root, dirs, file in os.walk("./inputs") for filename in file ]
        for f in files:
            G = read_input_file("./inputs/" + f)
            # print(f)
            T0 = nx.minimum_spanning_tree(G, weight='weight')
            # T1 = algo1(G)
            # T2 = algo2(G)
            # T3 = algo3(G)
            T5 = algo5(G)
        #     Ts = [T0, T2, T3]
        #     T = findMin(Ts)
        #     print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
        #     assert is_valid_network(G, T)
        #     write_output_file(T, f'out/{f.replace(".in", ".out")}')
        # files = [filename for root, dirs, file in os.walk("./out") for filename in file ]
        print(len(files))
