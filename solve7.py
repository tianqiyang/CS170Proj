from solve6 import algo6
import networkx as nx
from utils import is_valid_network, average_pairwise_distance
from helperFunctions import buildTree, addNodes, removeNodes

def build(G, nodes):
    newG = nx.Graph()
    nodes = sorted(list(nodes), key=lambda x: len(G[x]))
    if nodes:
        newG.add_node(nodes.pop(0))
    if nodes:
        newG.add_node(nodes.pop(0))
    cur = float('inf')
    if is_valid_network(G, newG):
        cur = average_pairwise_distance(newG)
    while nodes or is_valid_network(G, newG):
        for i in sorted(G.edges, key=lambda x: G[x[0]][x[1]]['weight']):
            if i[0] in nodes and i[1] in nodes:
                newG.add_edge(i[0], i[1], weight=G[i[0]][i[1]]['weight'])
        temp = nx.minimum_spanning_tree(newG, weight='weight', algorithm='kruskal')
        if is_valid_network(G, temp):
            thisValue = average_pairwise_distance(newG)
            if thisValue < cur:
                cur = thisValue
                newG = temp
        if nodes:
            newG.add_node(nodes.pop(0))
    for i in sorted(G.edges, key=lambda x: G[x[0]][x[1]]['weight']):
        if i[0] in nodes and i[1] in nodes:
            newG.add_edge(i[0], i[1], weight=G[i[0]][i[1]]['weight'])
    newG = nx.minimum_spanning_tree(newG, weight='weight', algorithm='kruskal')
    for i in sorted(list(newG.nodes), key=lambda x: len(G[x])):
        if len(G[i]) == 1:
            newG.remove_node(i)
        if len(G[i]) > 1:
            break
    return newG

def algo7(G):
    """
    build tree in different way.
    """
    T = algo6(G.copy())
    allNodes = set(list(G.nodes))
    for _ in range(1):
        used = set(list(T.nodes))s
        T = addNodes(G, T, allNodes - used)
        T = build(G, list(T.nodes))
        T = removeNodes(G, T)
        T = build(G, list(T.nodes))
    count = 3
    while not is_valid_network(G, T) and count:
        T = addNodes(G, T, allNodes - used)
        T = removeNodes(G, T)
        count -= 1
    if not is_valid_network(G, T):
        return algo6(G.copy())
    return T