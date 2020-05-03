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
    for _ in range(3):
        newT = addNodes(G, T, allNodes - set(list(T.nodes)))
        newT = removeNodes(G.copy(), newT)
    assert is_valid_network(G, newT)
    return newT
