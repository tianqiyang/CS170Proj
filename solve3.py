import networkx as nx
from solve1 import algo1
from utils import is_valid_network, average_pairwise_distance
from helperFunctions import mwd, getComponents, findAllPath, sortPathHelper, connectComponents, oneNode, buildTree, addNodes

def algo3(G):
    #adding nodes after algo 2
    T = algo1(G)
    used = set(list(T.nodes))
    if len(used) == 1:
        return T
    allNodes = set(list(G.nodes))
    rest = allNodes - used
    newT = addNodes(G, T, rest)
    newT = buildTree(G, list(newT.nodes))
    assert is_valid_network(G, newT)
    return newT
    
