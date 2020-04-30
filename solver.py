import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
import sys
import os
from bestSolve import findTree

# Usage: python3 solver.py

if __name__ == '__main__':
    testing = False
    if testing:
        path = 'medium-27.in'
        G = read_input_file('inputs/' + path)        
        print(path)
        T, c = findTree(G)
        assert is_valid_network(G, T)
        print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
    else:
        files = sorted([filename for root, dirs, file in os.walk("./inputs") for filename in file], key=lambda x: int(x.replace('large-', '').replace('small-', '').replace('medium-', '').replace('.in', '')))
        counter = [0] * 8
        for count, f in enumerate(files, 1):
            G = read_input_file("./inputs/" + f)
            print(count)
            print(f)
            T, c = findTree(G)
            counter[c] += 1
            assert is_valid_network(G, T)
            print("Average pairwise distance: {}\n".format(average_pairwise_distance(T)))
            write_output_file(T, f'out/{f.replace(".in", ".out")}')
        files = [filename for root, dirs, file in os.walk("./out") for filename in file ]
        print(len(files))
        print(counter)
