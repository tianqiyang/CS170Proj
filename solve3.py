import networkx as nx
from solve1 import algo1
from utils import is_valid_network, average_pairwise_distance
from helperFunctions import buildTree, addNodes, removeNodes

def algo3(G):
    """
    remove notes from previous algotirm.
    """
    T = algo1(G.copy())
    newT = removeNodes(G.copy(), T)
    newT = buildTree(G.copy(), list(newT.nodes))
    assert is_valid_network(G, newT)
    return newT

