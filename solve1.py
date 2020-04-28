import networkx as nx

def getLeastNode(G):
    covered = set()
    T, rest = set(), set()
    for i in sorted(list(G.nodes), key=lambda x: len(G[x]), reverse=True):
        if i not in covered:
            T.add(i)
            for v in G[i]:
                covered.add(v)
    return T, rest

def buildTree(G, T):
    need = set()
    for i in range(len(T)):
        for j in range(i+1, len(T)):
            for k in nx.shortest_path(G, source=T[i], target=T[j], weight='weight'):
                if k not in T:
                    need.add(k)
    T += [i for i in need]
    copy = G.copy()
    unused = []
    for re in copy:
        if re not in T:
            G.remove_node(re)
            unused.append(re)
    return G, copy, unused, T

def algo1(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """
    T, rest = getLeastNode(G)
    if len(T) == 1:
        onlyone = nx.Graph()
        onlyone.add_node(T[0])
        return onlyone
    # tree, G, unused, used = buildTree(G, T)
    # tree, G, unused, used = removeNode(G, used)
    # tree = nx.minimum_spanning_tree(tree, weight='weight', algorithm='kruskal')
    # cur = average_pairwise_distance(tree)
    # for i in unused:
    #     tree.add_node(i)
    #     for n in G[i]:
    #         if n in used:
    #             tree.add_edge(i, n)
    #             tree[i][n]['weight'] = G[i][n]['weight']
    #     if nx.is_tree(tree):
    #         newdis = average_pairwise_distance(tree)
    #         if newdis > cur:
    #             tree.remove_node(i)
    #         else:
    #             used.append(i)
    #             cur = min(cur, newdis)
    #     else:
    #         tree.remove_node(i)

    tree = nx.minimum_spanning_tree(G, weight='weight', algorithm='kruskal')
    # nodes = list(tree.nodes)
    # print(sorted(nodes))
    # does not check if they cover all graph after remove the node(invalid part)
    # cur = average_pairwise_distance(tree)
    # needRecover = False
    # for i in nodes:
    #     w = tree[i]
    #     tree.remove_node(i)
    #     if nx.is_connected(tree):
    #         newdis = average_pairwise_distance(tree)
    #         if newdis > cur:
    #             needRecover = True
    #         cur = min(cur, newdis)
    #     else:
    #         needRecover = True
    #     if needRecover:
    #         tree.add_node(i)
    #         for n in w:
    #             tree.add_edge(i, n)
    #             tree[i][n]['weight'] = w[n]['weight']
    #         needRecover = False
    # print(sorted(list(tree.nodes)))
    return tree