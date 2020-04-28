import networkx as nx
import random

def algo4(G):
    gVertices = set(list(G.nodes))
    gEdges = set(list(G.edges))
    S = list()
    degrees = dict()
    connectedMinSet = []
    while len(gVertices)!=0:
        def findDegrees():
            for vertex in gVertices:
                deg = 0
                for edge in gEdges:
                    if vertex in edge:	
                        deg = deg+1
                    else: None
                degrees[vertex] = deg
            return degrees
        findDegrees()
        maxDegree = max(degrees.values())
        for i in degrees:
            if degrees.get(i) == maxDegree:
                S.append(i)
                maxvertex= i
        nbrmaxvertex = set()
        nbrmaxvertex.add(maxvertex)
        gVerticesNew = set()
        for edg in enumerate(gEdges):
            
            if edg[1][0]==maxvertex:
                nbrmaxvertex.add(edg[1][1])
            elif edg[1][1]==maxvertex:
                nbrmaxvertex.add(edg[1][0])
        connectedMinSet.append(nbrmaxvertex)
        gVerticesNew = gVertices - nbrmaxvertex
        gVertices=gVerticesNew
        c = set(gEdges)
        for v in c:
            for e in c:
                if maxvertex in gEdges:
                    gEdges.remove(e)
        degrees = dict()
    print('\nMinimum independent dominating set in the graph = ',set(S))
    q = 0
    connq = set()
    while q < len(S):
        w = q+1
        while w < len(S)-q and w < len(connectedMinSet) and q < len(connectedMinSet):
            rs = set(connectedMinSet[q]).intersection(set(connectedMinSet[w]))
            if len(rs) ==1:
                connq |= rs
            if len(rs) >1:
                connq |= set(random.sample(rs,1))
            w +=1
        q +=1
    connq |= set(S)
    copy = G.copy()
    for re in copy:
        if re not in connq:
            G.remove_node(re)
    draw(G)
    return G