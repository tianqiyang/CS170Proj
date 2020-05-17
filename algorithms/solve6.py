from algorithms.solve5 import algo5
from utils import is_valid_network, average_pairwise_distance, addNodes, removeNodes

def algo6(G):
    """
    remove and add nodes from previous tree.
    """
    T = algo5(G.copy())
    T = removeNodes(G, T)
    count = 3
    allNode = set(list(G.nodes))
    while not is_valid_network(G, T) and count:
        T = addNodes(G, T, allNode - set(list(T.nodes)))
        T = removeNodes(G, T)
        count -= 1
    return T