import networkx as nx
from solve2 import algo2
from utils import is_valid_network
from helperFunctions import addNodes, removeNodes

def algo4(G):
    """
    add and remove notes from tree.
    """
    T = algo2(G)
    allNodes = set(list(G.nodes))
    for i in range(2):
        used = set(list(T.nodes))
        newT = addNodes(G, T, allNodes - used)
        newT = removeNodes(G.copy(), newT)
    assert is_valid_network(G, newT)
    return newT
