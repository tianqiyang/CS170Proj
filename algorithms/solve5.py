from algorithms.solve0 import algo0
from utils import is_valid_network, average_pairwise_distance, addNodes, removeNodes

def algo5(G):
    """
    remove and node from mst.
    """
    T = algo0(G.copy())
    allNodes = set(list(G.nodes))
    for _ in range(2):
        T = addNodes(G, T, allNodes - set(list(T.nodes)))
        T = removeNodes(G, T)
    assert is_valid_network(G, T)
    return T