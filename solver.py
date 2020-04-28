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

def getLeastNode(G):
    covered = {}
    T, rest = [], []
    for i in sorted(list(G.nodes), key=lambda x: len(G[x]), reverse=True):
        if i not in covered:
            T.append(i)
            for v in G[i]:
                covered[v] = 1
                rest.append(v)
    return T, rest

def buildTree(T):
    tree = nx.Graph()
    usedNode = set()
    for i in range(len(T)):
        for j in range(i+1, len(T)):
            temp = nx.shortest_path(G, source=T[i], target=T[j], weight='weight')
            for t in range(len(temp)-1):
                a = temp[t]
                b = temp[t+1]
                tree.add_node(a)
                tree.add_node(b)
                tree.add_edge(a, b)
                tree[a][b]['weight'] = G[a][b]['weight']
                usedNode.add(a)
                usedNode.add(b)
    return tree, usedNode

def solve1(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """
    T, rest = getLeastNode(G)
    if len(T) == 1:
        onlyone = nx.Graph()
        onlyone.add_node(T[0])
        return onlyone
    tree, node = buildTree(T)
    cur = average_pairwise_distance(tree)
    added = False
    for i in rest:
        tree.add_node(i)
        for n in G[i]:
            if n in node:
                tree.add_edge(i, n)
                tree[i][n]['weight'] = G[i][n]['weight']
                newdis = average_pairwise_distance(tree)
                if newdis > cur:
                    tree.remove_edge(i, n)
                    tree.remove_node(i)
                else:
                    T.append(i)
                cur = min(cur, newdis)
    copy = G.copy()
    for re in copy:
        if re not in T:
            G.remove_node(re)
    tree = nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')
    #nodes = list(tree.nodes)
    #print(sorted(nodes))
    # cur = average_pairwise_distance(tree)
    # for i in nodes:
    #     w = list(tree[i])
    #     tree.remove_node(i)
    #     if nx.is_connected(tree):
    #         print(tree.nodes)
    #         newdis = average_pairwise_distance(tree)
    #         if newdis > cur:
    #            tree.add_node(i)
    #         cur = min(cur, newdis)
    #     else:
    #         tree.add_node(i)
    #print(sorted(list(tree.nodes)))
    return tree
    
def solve2(G):
    

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    testing = False
    if testing:
        path = 'inputs/large-160.in'
        G = read_input_file(path)
        #draw(G)
        T = solve1(G)
        assert is_valid_network(G, T)
        print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
        #write_output_file(T, 'out/25.in')
    else:
        files = [filename for root, dirs, file in os.walk("./inputs") for filename in file ]
        print(len(files))
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
