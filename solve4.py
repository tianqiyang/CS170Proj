import networkx as nx
from solve2 import algo2
from utils import is_valid_network, average_pairwise_distance







def algo4(G):
    #adding nodes after algo 2
    T = algo2(G.copy())
    used = set(list(T.nodes))
    if len(used) == 1:
        return T
    allNodes = set(list(G.nodes))
    rest = allNodes - used
    newT = removeNodes(G.copy(), T)
    newT = buildTree(G.copy(), list(newT.nodes))
    assert is_valid_network(G, newT)
    return newT

