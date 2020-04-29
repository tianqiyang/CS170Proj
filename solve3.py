import networkx as nx
from solve1 import algo1
from utils import is_valid_network, average_pairwise_distance
from helperFunctions import mwd, getComponents, findAllPath, sortPathHelper, connectComponents, oneNode, buildTree, addNodes, removeNodes

def algo3(G):
    """
    remove notes to tree
    """
    T = algo1(G.copy())
    used = set(list(T.nodes))
    if len(used) == 1:
        return T
    allNodes = set(list(G.nodes))
    rest = allNodes - used
    newT = removeNodes(G.copy(), T)
    newT = buildTree(G.copy(), list(newT.nodes))
    assert is_valid_network(G, newT)
    return newT

