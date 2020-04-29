import networkx as nx
from solve2 import algo2
from utils import is_valid_network, average_pairwise_distance

def addNodes(G, tree, rest):
    cur = average_pairwise_distance(tree)
    node = list(tree.nodes)
    added = False
    for i in rest:
        tree.add_node(i)
        for n in G[i]:
            if n in node:
                tree.add_edge(i, n)
                tree[i][n]['weight'] = G[i][n]['weight']
        tree = nx.minimum_spanning_tree(tree, weight='weight')
        if is_valid_network(G, tree):
            newdis = average_pairwise_distance(tree)
            if newdis > cur:
                tree.remove_node(i)
            else:
                cur = min(cur, newdis)
        else:
            tree.remove_node(i)
    return tree

def buildTree(G, nodes):
    newG = nx.Graph()
    newG.add_nodes_from(nodes)
    for i in sorted(G.edges, key=lambda x: G[x[0]][x[1]]['weight']):
        if i[0] in nodes and i[1] in nodes:
            newG.add_edge(i[0], i[1], weight=G[i[0]][i[1]]['weight'])
    return nx.minimum_spanning_tree(newG, weight='weight')

def algo3(G):
    #adding nodes after algo 2
    T = algo2(G)
    used = set(list(T.nodes))
    if len(used) == 1:
        return T
    allNodes = set(list(G.nodes))
    rest = allNodes - used
    newT = addNodes(G, T, rest)
    newT = buildTree(G, list(newT.nodes))
    assert is_valid_network(G, newT)
    return newT
    
