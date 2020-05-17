import networkx as nx
from utils import average_pairwise_distance

def nodesWeight(G, n):
    # return sorted node weight
    weightOfNodes = {}
    for node in G.nodes:
        if node < n:
            weightOfNodes[node] = 0

    for edge in G.edges():
        if edge[0] < n:
            weightOfNodes[edge[0]] += G[edge[0]][edge[1]]['weight']
        if edge[1] < n:
            weightOfNodes[edge[1]] += G[edge[0]][edge[1]]['weight']
    return sorted(weightOfNodes.items(), key=lambda item: item[1], reverse=True)


def algo9(G):
    T = nx.Graph()
    n = len(G)
    B = nx.Graph()
    # Add nodes with the node attribute "bipartite"
    B.add_nodes_from(G.nodes)
    for node in G.nodes():
        tmp = n + node
        B.add_node(tmp)

    for a in G.nodes():
        for b in nx.neighbors(G, a):
            # print(G[a][b]['weight'])
            B.add_edge(a, n + b, weight=G[a][b]['weight'])

    weightOfNodes = nodesWeight(B, n)


    currentNode = weightOfNodes[0][0]
    T.add_node(currentNode)
    B_prime = B.copy()
    for node in nx.neighbors(B_prime, currentNode):
        B.remove_node(node)
    B.remove_node(currentNode)

    print(B.edges, 1)

    i = 1
    while len(set(B.nodes) & set(range(n, 2*n))) != 0:
        candidate = set()
        for node in T.nodes():
            candidate = candidate | set(nx.neighbors(G, node))

        candidate -=  T.nodes()
        # print(candidate, 'candidate')

        for i in weightOfNodes:
            if i[0] in list(candidate):
                currentNode = i[0]
                break

        # print(currentNode, 'currentNode')

        shortest = float('inf')
        shortestNode = None
        for j in T.nodes:
            if ((currentNode, j) in G.edges) and (G[currentNode][j]['weight'] < shortest):
                shortest = G[currentNode][j]['weight']
                shortestNode = j
        # print(currentNode, shortestNode, G[currentNode][shortestNode]['weight'])
        T.add_edge(currentNode, shortestNode, weight=G[currentNode][shortestNode]['weight'])

        # currentNode = weightOfNodes[i][0]
        T.add_node(currentNode)
        B_prime = B.copy()
        for node in nx.neighbors(B_prime, currentNode):
            B.remove_node(node)
        B.remove_node(currentNode)

    return T