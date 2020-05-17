import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt

def is_valid_network(G, T):
    """
    Checks whether T is a valid network of G.
    Args:
        G: networkx.Graph
        T: networkx.Graph

    Returns:
        bool: whether T is a valid network
    """

    return nx.is_tree(T) and nx.is_dominating_set(G, T.nodes)


def average_pairwise_distance(T):
    """
    Computes the average pairwise distance between vertices in T.
    This is what we want to minimize!

    Note that this function is a little naive, i.e. there are much
    faster ways to compute the average pairwise distance in a tree.
    Feel free to write your own!

    Args:
        T: networkx.Graph, a tree

    Returns:
        double: the average pairwise distance
    """
    if not nx.is_connected(T):
        raise ValueError("Tree must be connected")

    if len(T) == 1: return 0
    
    path_lengths = nx.all_pairs_dijkstra_path_length(T)
    total_pairwise_distance = sum([sum(length[1].values()) for length in path_lengths])
    return total_pairwise_distance / (len(T) * (len(T) - 1))


def average_pairwise_distance_fast(T):
    """Calculates the average pairwise distance for a tree in linear time.

    Since there is always unique path between nodes in a tree, each edge in the
    tree is used in all of the paths from the connected component on one side
    of the tree to the other. So each edge contributes to the total pairwise cost
    in the following way: if the size of the connected components that are
    created from removing an edge e are A and B, then the total pairwise distance
    cost for an edge is 2 * A * B * w(e) = (# of paths that use that edge) * w(e).
    We multiply by two to consider both directions that paths can take on an
    undirected edge.

    Since each edge connects a subtree to the rest of a tree, we can run DFS
    to compute the sizes of all of the subtrees, and iterate through all the edges
    and sum the pairwise distance costs for each edge and divide by the total
    number of pairs.

    This is very similar to Q7 on MT1.

    h/t to Noah Kingdon for the algorithm.
    """
    if not nx.is_connected(T):
        raise ValueError("Tree must be connected")

    if len(T) == 1: return 0

    subtree_sizes = {}
    marked = defaultdict(bool)
    # store child parent relationships for each edge, because the components
    # created when removing an edge are the child subtree and the rest of the vertices
    root = list(T.nodes)[0];
    
    child_parent_pairs = [(root, root)]

    def calculate_subtree_sizes(u):
        """Iterates through the tree to compute all subtree sizes in linear time

        Args:
            u: the root of the subtree to start the DFS

        """
        unmarked_neighbors = filter(lambda v: not marked[v], T.neighbors(u))
        marked[u] = True
        size = 0
        for v in unmarked_neighbors:
            child_parent_pairs.append((v, u))
            calculate_subtree_sizes(v)
            size += subtree_sizes[v]
        subtree_sizes[u] = size + 1
        return subtree_sizes[u]

    calculate_subtree_sizes(root)  # any vertex can be the root of a tree

    cost = 0
    for c, p in child_parent_pairs:
        if c != p:
            a, b = subtree_sizes[c], len(T.nodes) - subtree_sizes[c]
            w = T[c][p]["weight"]
            cost += 2 * a * b * w
    return cost / (len(T) * (len(T) - 1))



def draw(G):
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.subplot(122)
    nx.draw_shell(G, with_labels=True, font_weight='bold')
    plt.show()

def draw2(G, T):
    plt.subplot(221)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.subplot(222)
    nx.draw_shell(G, with_labels=True, font_weight='bold')
    plt.subplot(223)
    nx.draw(T, with_labels=True, font_weight='bold')
    plt.subplot(224)
    nx.draw_shell(T, with_labels=True, font_weight='bold')
    plt.show()

def mwd(G, weight='weight'):
    """This is source code of network.(min_weighted_dominating_set)
    """
    dom_set = set([])
    cost_func = dict((node, nd.get(weight, 1)) for node, nd in G.nodes(data=True))
    vertices = set(G)
    sets = dict((node, set([node]) | set(G[node])) for node in G)
    def _cost(subset):
        """Our cost effectiveness function for sets given its weight."""
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
    start = sorted(list(needConnect), key=lambda x: len(G[x]), reverse=True)[0]
    components = []
    while needConnect:
        needConnect.discard(start)
        part = [start]
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
        start = sorted(list(needConnect), key=lambda x: len(G[x]), reverse=True)[0]
    return components

def findAllPath(G, components):
    pathDic = {}
    for i in range(len(components)):
        for j in range(i+1, len(components)):
            A, B = components[i], components[j]
            for x in range(len(A)):
                for y in range(len(B)):
                    if A[x] != B[y]:
                        pathDic[(A[x], B[y])] = nx.shortest_path(G, A[x], B[y])
    return pathDic

def sortPathHelper(x):
    try:
        path = pathDic[x]
        return sum([G[path[i]][path[i+1]]['weight'] for i in range(0, len(path)-1)])
    except:
        return float('inf')

def common_member(a, b):
    return len(set(a).intersection(set(b) )) > 0

def connectComponents(G, components):
    components = sorted(components, key=lambda x: len(x), reverse=True)
    pathDic = findAllPath(G, components)
    while len(components) > 1:
        path = sorted(pathDic, key=lambda x: sortPathHelper(x))[0]
        first = second = None
        start = path[0]
        end = path[1]
        for i in components:
            if start in i:
                first = i
            elif end in i:
                second = i
            if first != None and second != None:
                break
        newComponent = set()
        components.remove(first)
        for i in first:
            newComponent.add(i)
        components.remove(second)
        for i in second:
            newComponent.add(i)
        for i in pathDic[path]:
            newComponent.add(i)
        if len(components) == 0:
            return newComponent
        components.insert(0, list(newComponent))
        unique = True
        while unique:
            unique = False
            for i in range(len(components)):
                for j in range(i+1, len(components)):
                    if components[i] != components[j] and common_member(components[i], components[j]):
                        unique = True
                        a = components[i]
                        b = components[j]
                        components.remove(a)
                        components.remove(b)
                        components.append(list(set(a) | set(b)))
                        break
        pathDic = findAllPath(G, components)
    return components[0]

def buildTree(G, nodes):
    newG = nx.Graph()
    newG.add_nodes_from(nodes)
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

def oneNode(G, nodes):
    onlyone = nx.Graph()
    onlyone.add_node(nodes[0])
    return onlyone

def addNodes(G, tree, rest):
    cur = float('inf')
    if is_valid_network(G, tree):
        cur = average_pairwise_distance(tree)
    node = sorted(list(tree.nodes), key=lambda x: len(G[x]), reverse=True)
    for i in sorted(list(rest), key=lambda x: len(G[x]), reverse=True):
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

def removeNodes(G, tree):
    nodes = sorted(list(tree.nodes), key=lambda x: len(G[x]), reverse=True)
    cur = float('inf')
    if is_valid_network(G, tree):
        cur = average_pairwise_distance(tree)
    li = list(nodes)
    for i in nodes:
        li.remove(i)
        temp = buildTree(G.copy(), li)
        if len(temp.nodes) > 0 and is_valid_network(G, temp) and average_pairwise_distance(temp) < cur:
            cur = average_pairwise_distance(temp)
        else:
            li.append(i)
    return buildTree(G, li)

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