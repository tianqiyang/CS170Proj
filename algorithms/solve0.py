import networkx as nx

def algo0(G):
    """
    find mst of G
    """
    return nx.minimum_spanning_tree(G.copy(), weight='weight')