import networkx as nx
import random

def getLeastNode(G):
    covered = set()
    T = set()
    for i in sorted(list(G.nodes), key=lambda x: sum([G[i][x]['weight'] for i in G[x]]), reverse=True):
        if i not in covered:
            T.add(i)
            for v in G[i]:
                covered.add(v)
    return T, covered

def getComponents(G, needConnect):
    """
    G = nx.Graph()
    G.add_nodes_from([1,2,3,4,5,6])
    G.add_edges_from([(1,2),(2,3),(3,4),(3,5)])
    need = set()
    tree = set()
    needConnect = {1,2,3,4,5,6}
    input: G, needConnect
    return: [[6], [1, 2, 3, 4, 5]]
    """
    start = random.sample(needConnect, 1)[0]
    components = []
    while needConnect:
        needConnect.discard(start)
        part = [start]
        edges = set(G[start])
        queue = [start]
        while queue:
            start = queue.pop()
            for e in set(G[start]):
                if e in needConnect:
                    needConnect.discard(e)
                    part.append(e)
                    queue.append(e)
        components.append(part)
        if len(needConnect) == 0:
            break
        start = random.sample(needConnect, 1)[0]
    return components

def connectComponents(G, components, T):
    paths = []
    for i in range(len(T)):
        for j in range(i+1, len(T)):
            paths.append(nx.shortest_path(G, source=T[i], target=T[j], weight='weight'))
    paths = sorted(paths, key=lambda x: sum([G[x[i]][x[i+1]]['weight'] for i in range(0, len(x)-1)]))
    nodes = set()
    while components:
        if len(paths) == 0 or len(paths) == 1:
            break
        path = paths.pop()
        start = path[0]
        end = path[-1]
        first = None
        second = None
        for i in components:
            if start in i:
                first = i
            if end in i:
                second = i
            if first and second:
                break
        if first and second:
            components.remove(first)
            components.remove(second)
            for i in first:
                nodes.add(i)
            for i in second:
                nodes.add(i)
            for i in path:
                nodes.add(i)
    if components:
        paths = []
        for v in components[0]:
            for i in nodes:
                paths.append(nx.shortest_path(G, source=v, target=i, weight='weight'))
        paths = sorted(paths, key=lambda x: sum([G[x[i]][x[i+1]]['weight'] for i in range(0, len(x)-1)]))
        for i in paths[0]:
            nodes.add(i)
    return nodes


def getTree(G, T):
    """
    G: original graph
    T: needed nodes 
    
    return tree
    """
    copy = G.copy()
    for re in copy:
        if re not in T:
            G.remove_node(re)
    return G

def algo1_2(G):
    T, baseNode = getLeastNode(G)
    if len(T) == 1:
        onlyone = nx.Graph()
        onlyone.add_node(T[0])
        return onlyone
    components = getComponents(G, set(T))
    nodes = connectComponents(G, components, list(T))
    return getTree(G, nodes)