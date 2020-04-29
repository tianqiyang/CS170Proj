import networkx as nx
from solve1 import algo1
from utils import is_valid_network, average_pairwise_distance
from helperFunctions import mwd, getComponents, findAllPath, sortPathHelper, connectComponents, oneNode, buildTree, addNodes, removeNodes

def algo5(G):
    T = algo1(G)
    used = set(list(T.nodes))
    if len(used) == 1:
        return T
    for i in range(4):
        allNodes = set(list(G.nodes))
        rest = allNodes - used
        newT = addNodes(G, T, rest)
        newT = buildTree(G, list(newT.nodes))
    return newT
