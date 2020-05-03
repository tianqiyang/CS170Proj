import networkx as nx
from solve1 import algo1
from utils import is_valid_network
from helperFunctions import buildTree, addNodes

def algo2(G):
    """
    add notes to previous algorithm.
    """
    T = algo1(G)
    newT = addNodes(G, T, set(list(G.nodes)) - set(list(T.nodes)))
    newT = buildTree(G, list(newT.nodes))
    assert is_valid_network(G, newT)
    return newT
