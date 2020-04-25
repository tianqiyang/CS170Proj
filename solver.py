import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
import sys

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
    new = []
    # print(T)
    for i in range(len(T)):
        temp = []
        for j in range(i+1, len(T)):
            temp.append(nx.shortest_path(G, source=T[i], target=T[j]))
        short = sorted(temp, key=lambda x: sum([G[m][m+1]['weight'] for m in range(len(temp)-1)]))[0]
        for v in short:
            if v not in T:
                T.append(v)
    copy = G.copy()
    for re in copy:
        if re not in T:
            G.remove_node(re)
    # print(G.nodes)
    return G


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G = read_input_file(path)
    T = solve(G)
    assert is_valid_network(G, T)
    print("Average  pairwise distance: {}".format(average_pairwise_distance(T)))
    write_output_file(T, 'out/25.out')
