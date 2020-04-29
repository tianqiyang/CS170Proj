from solve5 import algo5
from utils import is_valid_network, average_pairwise_distance
from helperFunctions import mwd, getComponents, findAllPath, sortPathHelper, connectComponents, oneNode, buildTree, addNodes, removeNodes

def algo6(G):
    T = algo5(G.copy())
    T = removeNodes(G, T)
    count = 3
    while not is_valid_network(G, T) and count:
        T = addNodes(G, T, allNodes - used)
        T = removeNodes(G, T)
        count -= 1
    return T