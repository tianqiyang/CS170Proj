import networkx as nx

def getNeighbor(start, edges):
    """
    start(int) : the vertex index
    edges(dictionary): the edges connect to other vertex
    """
    nb = set()
    for i in edges:
        if i[0] == start:
            nb.add(i[1])
        elif i[1] == start:
            nb.add(i[0])
    return nb

def findDegrees(vertex, edges):
    dic = dict()
    for v in vertex:
        deg = 0
        for e in edges:
            if v in e:
                deg += 1
        dic[v] = deg
    return dic

def algo3(G):
    n = len((G.nodes)) - 1
    nodes = sorted(list(G.nodes), key=lambda x: len(G[x]), reverse=True)
    if len(G[nodes[0]]) == n:
        onlyone = nx.Graph()
        onlyone.add_node(nodes[0])
        return onlyone
    nb = set()
    minDom = set()
    vertex = set(nodes)
    edges = set(list(G.edges))
    start = nodes[0]
    while vertex: 
        dic = dict()
        minDom.add(start)
        vertex.discard(start)
        nb = getNeighbor(start, edges)
        if len(nb) == 0:
            break
        vertex = vertex - nb
        if len(vertex) == 0:
            break
        remove = set()
        for v in nb:
            for s in edges:
                if v in s:
                    remove.add(s)
        edges = edges - remove
        if len(edges) == 1 or len(edges) == 2:
            last = random.sample(vertex, 1)
            minDom.add(last[0])
            break
        elif len(edges) == 0:
            break
        deg = findDegrees(vertex, edges)
        start = sorted(deg, key=lambda x: deg[x], reverse=True)[0]
    print(minDom)
    draw(G)
    return tree