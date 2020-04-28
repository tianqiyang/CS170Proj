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

def buildTree(G, T):
    need = set()
    for i in range(len(T)):
        for j in range(i+1, len(T)):
            for k in nx.shortest_path(G, source=T[i], target=T[j], weight='weight'):
                if k not in T:
                    need.add(k)
    T += [i for i in need]
    copy = G.copy()
    unused = []
    for re in copy:
        if re not in T:
            G.remove_node(re)
            unused.append(re)
    return G, copy, unused, T

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
    # tree, G, unused, used = buildTree(G, T)
    # tree, G, unused, used = removeNode(G, used)
    # tree = nx.minimum_spanning_tree(tree, weight='weight', algorithm='kruskal')
    # cur = average_pairwise_distance(tree)
    # for i in unused:
    #     tree.add_node(i)
    #     for n in G[i]:
    #         if n in used:
    #             tree.add_edge(i, n)
    #             tree[i][n]['weight'] = G[i][n]['weight']
    #     if nx.is_tree(tree):
    #         newdis = average_pairwise_distance(tree)
    #         if newdis > cur:
    #             tree.remove_node(i)
    #         else:
    #             used.append(i)
    #             cur = min(cur, newdis)
    #     else:
    #         tree.remove_node(i)

    # tree = nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')
    # nodes = list(tree.nodes)
    # print(sorted(nodes))
    # does not check if they cover all graph after remove the node(invalid part)
    # cur = average_pairwise_distance(tree)
    # needRecover = False
    # for i in nodes:
    #     w = tree[i]
    #     tree.remove_node(i)
    #     if nx.is_connected(tree):
    #         newdis = average_pairwise_distance(tree)
    #         if newdis > cur:
    #             needRecover = True
    #         cur = min(cur, newdis)
    #     else:
    #         needRecover = True
    #     if needRecover:
    #         tree.add_node(i)
    #         for n in w:
    #             tree.add_edge(i, n)
    #             tree[i][n]['weight'] = w[n]['weight']
    #         needRecover = False
    # print(sorted(list(tree.nodes)))
    draw(tree)
    return tree
    
def solve2(G):
    n = len((G.nodes)) - 1
    nodes = sorted(list(G.nodes), key=lambda x: len(G[x]), reverse=True)
    if len(G[nodes[0]]) == n:
        onlyone = nx.Graph()
        onlyone.add_node(nodes[0])
        return onlyone
    tree = nx.minimum_spanning_tree(G, weight='weight')
    print(tree.nodes)
    #print('prim', average_pairwise_distance(nx.minimum_spanning_tree(G, weight='weight', algorithm='prim')))
    # print('boruvka', average_pairwise_distance(nx.minimum_spanning_tree(G, weight='weight', algorithm='boruvka')))
    # print('kruskal', average_pairwise_distance(nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')))
    
    fixed = []
    return tree
    
def solve3(G):
    n = len((G.nodes)) - 1
    nodes = sorted(list(G.nodes), key=lambda x: len(G[x]), reverse=True)
    if len(G[nodes[0]]) == n:
        onlyone = nx.Graph()
        onlyone.add_node(nodes[0])
        return onlyone
    tree = nx.minimum_spanning_tree(G, weight='weight')
    print(tree.nodes)
    
    
    fixed = []
    return tree

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    testing = True
    if testing:
        path = 'inputs/large-160.in'
        G = read_input_file(path)
        #draw(G)
        T = solve3(G)
        assert is_valid_network(G, T)
        print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
        #write_output_file(T, 'out/25.in')
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
