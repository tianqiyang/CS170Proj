import networkx as nx
from solve2 import algo2
from utils import is_valid_network, average_pairwise_distance
from helperFunctions import mwd, getComponents, findAllPath, sortPathHelper, connectComponents, oneNode, buildTree, addNodes, removeNodes

def algo4(G):
    """
    add notes to tree
    """
    T = algo2(G)
    used = set(list(T.nodes))
    if len(used) == 1:
        return T
    allNodes = set(list(G.nodes))
    for i in range(2):
        rest = allNodes - used
        newT = addNodes(G, T, rest)
        newT = buildTree(G, list(newT.nodes))
        newT = removeNodes(G.copy(), newT)
        newT = buildTree(G.copy(), list(newT.nodes))
        used = set(list(newT.nodes))
    assert is_valid_network(G, newT)
    return newT
