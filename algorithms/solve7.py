from algorithms.solve6 import algo6
import networkx as nx
from utils import is_valid_network, addNodes, removeNodes, build

def algo7(G):
    """
    build tree in different way.
    """
    T = algo6(G.copy())
    allNodes = set(list(G.nodes))
    for _ in range(1):
        T = addNodes(G, T, allNodes - set(list(T.nodes)))
        T = build(G, list(T.nodes))
        T = removeNodes(G, T)
        T = build(G, list(T.nodes))
    count = 3
    while not is_valid_network(G, T) and count:
        T = addNodes(G, T, allNodes - set(list(T.nodes)))
        T = removeNodes(G, T)
        count -= 1
    if not is_valid_network(G, T):
        return algo6(G.copy())
    return T