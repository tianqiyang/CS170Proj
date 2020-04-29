import matplotlib.pyplot as plt
import networkx as nx
from utils import is_valid_network, average_pairwise_distance
from solve0 import algo0
from solve1 import algo1
from solve2 import algo2
from solve3 import algo3
from solve4 import algo4
from solve5 import algo5
from solve6 import algo6
from solve7 import algo7

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

def findMin(li):
    return min(li, key=lambda x: average_pairwise_distance(x))

def findTree(G):
    #draw(G)
    func = [algo0, algo1, algo2, algo3, algo4, algo5, algo6, algo7]
    Ts = []
    for t in range(len(func)):
        Ts.append(func[t](G.copy()))
        value = average_pairwise_distance(Ts[t])
        print("{} distance: {}".format(t,value))
        if value == 0:
            return Ts[-1]
    T = findMin(Ts)
    #draw2(G, T)
    return T