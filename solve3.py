import networkx as nx
from solve2 import algo2

def algo3(G):
    #adding nodes after algo 2
    T = algo2(G)
    used = set(list(T.nodes))
    if len(used) == 1:
        return T
    #print(T.nodes)
    allNodes = set(list(G.nodes))
    rest = allNodes - used
    if rest:
        print("not empty")
    
