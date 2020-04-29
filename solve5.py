from solve0 import algo0
from utils import is_valid_network, average_pairwise_distance
from helperFunctions import mwd, getComponents, findAllPath, sortPathHelper, connectComponents, oneNode, buildTree, addNodes, removeNodes

def removeUnused(G, T):
    for i in sorted(list(T.nodes), key=lambda x: len(G[x]), reverse=True):
        if len(G[i]) == 1:
            T.remove_node(i)
    return T

def algo5(G):
    T = algo0(G.copy())
    allNodes = set(list(G.nodes))
    for _ in range(2):
        used = set(list(T.nodes))
        T = addNodes(G, T, allNodes - used)
        T = removeNodes(G, T)
    assert is_valid_network(G, T)
    return T