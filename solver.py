import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
import sys
import os
from bestSolve import findTree

# Usage: python3 solver.py

if __name__ == '__main__':
    testing = True
    if testing:
        path = 'small-1.in'
        G = read_input_file('inputs/' + path)        
        print(path)
        T = findTree(G)
        assert is_valid_network(G, T)
        print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
    else:
        files = [filename for root, dirs, file in os.walk("./inputs") for filename in file ]
        for f in files:
            G = read_input_file("./inputs/" + f)
            print(f)
            T = findTree(G)
            assert is_valid_network(G, T)
            print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
            write_output_file(T, f'out/{f.replace(".in", ".out")}')
        files = [filename for root, dirs, file in os.walk("./out") for filename in file ]
        print(len(files))
