import networkx as nx
from parse import *
from utils import *
import sys

def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """

    # TODO: your code here!
    return G


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

def checkValidInput():
    paths = ["25", "50", "100"]
    for path in paths:
        if (not validate_file(path + ".in")):
            return False
    return True

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    assert checkValidInput()
    n = path.split(".")[0]
    G = read_input_file(path, int(n))
    T = solve(G)
    #assert is_valid_network(G, T)
    print("Average pairwise distance: {}".format(average_pairwise_distance(T)))
    write_output_file(T, f"{n}.out")
