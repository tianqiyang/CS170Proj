import networkx as nx
import random
from utils import is_valid_network
from helperFunctions import mwd, getComponents, findAllPath, sortPathHelper, connectComponents, oneNode, buildTree

def algo1(G):
    n = len((G.nodes))
    nodes = sorted(list(G.nodes), key=lambda x: len(G[x]), reverse=True)
    if len(G[nodes[0]]) == n or len(G[nodes[0]]) == n - 1:
        return oneNode(G, nodes)
    domin = mwd(G, 'weight')
    components = getComponents(G, domin)
    nodes = connectComponents(G, components)
    T = buildTree(G, nodes)
    assert is_valid_network(G, T)
    return T
