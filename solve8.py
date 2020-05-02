import networkx as nx
from utils import average_pairwise_distance

def algo8(G):
    """
    if cycle, we remove two nodes that has largest edges
    """
    cur = float('inf')
    for i in nx.find_cycle(G):
        copy = G.copy()
        copy.remove_nodes_from(i)
        temp = average_pairwise_distance(copy)
        if temp < cur:
            cur = temp
            returnG = copy
    return returnG