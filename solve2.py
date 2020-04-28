import networkx as nx
import random
def mwd(G, weight='weight'):
    dom_set = set([])
    cost_func = dict((node, nd.get(weight, 1)) for node, nd in G.nodes(data=True))
    
    vertices = set(G)
    sets = dict((node, set([node]) | set(G[node])) for node in G)

    def _cost(subset):
        """ Our cost effectiveness function for sets given its weight
        """
        cost = sum(cost_func[node] for node in subset)
        return cost / float(len(subset - dom_set))

    while vertices:
        # find the most cost effective set, and the vertex that for that set
        dom_node, min_set = min(sets.items(),
                                key=lambda x: (x[0], _cost(x[1])))
        alpha = _cost(min_set)

        # reduce the cost for the rest
        for node in min_set - dom_set:
            cost_func[node] = alpha

        # add the node to the dominating set and reduce what we must cover
        dom_set.add(dom_node)
        del sets[dom_node]
        vertices = vertices - min_set

    return dom_set

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
    start = random.choice(list(needConnect))
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
        start = random.choice(list(needConnect))
    return components

def connectComponents(G, components, T):
    paths = []
    base = components.pop()
    while components:
        if len(components) == 1:
            break
        paths = []
        for i in base:
            for j in components:
                for k in j:
                    paths.append(nx.shortest_path(G, source=i, target=k, weight='weight'))
        paths = sorted(paths, key=lambda x: sum([G[x[i]][x[i+1]]['weight'] for i in range(0, len(x)-1)]))
        path = paths[0]
        start = path[0]
        end = path[-1]
        c = None
        for i in components:
            if start in i or end in i:
                c = i
                components.remove(i)
                break
        if c:
            part = set(base) | set(c) | set(path)
            components.insert(0, list(part))
        base = components.pop()
    return components[0]

def algo2(G):
    n = len((G.nodes)) - 1
    nodes = sorted(list(G.nodes), key=lambda x: len(G[x]), reverse=True)
    if len(G[nodes[0]]) == n:
        onlyone = nx.Graph()
        onlyone.add_node(nodes[0])
        return onlyone
    tree = mwd(G, 'weight')
    cover = set()
    for i in tree:
        cover.add(i)
        for j in G[i]:
            cover.add(j)
    assert (set(G.nodes) - cover) == set()
    
    
    
    # components = getComponents(G, tree)
    # print(components)
    # nodes = connectComponents(G, components, list(tree))
    # print(nodes)
    return getTree(G, nodes)
    
