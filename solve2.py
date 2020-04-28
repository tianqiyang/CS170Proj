import networkx as nx

def algo2(G):
    n = len((G.nodes)) - 1
    nodes = sorted(list(G.nodes), key=lambda x: len(G[x]), reverse=True)
    if len(G[nodes[0]]) == n:
        onlyone = nx.Graph()
        onlyone.add_node(nodes[0])
        return onlyone
    tree = nx.minimum_spanning_tree(G, weight='weight')
    print(tree.nodes)
    #print('prim', average_pairwise_distance(nx.minimum_spanning_tree(G, weight='weight', algorithm='prim')))
    # print('boruvka', average_pairwise_distance(nx.minimum_spanning_tree(G, weight='weight', algorithm='boruvka')))
    # print('kruskal', average_pairwise_distance(nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')))
    
    fixed = []
    return tree