from utils import is_valid_network, mwd, getComponents, connectComponents, buildTree

def algo1(G):
    """
    find the mdcs and connect them as components.
    Then find the min cost to connect components.
    """
    domin = mwd(G)
    components = getComponents(G, domin)
    nodes = connectComponents(G, components)
    T = buildTree(G, nodes)
    assert is_valid_network(G, T)
    return T
