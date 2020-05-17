# CS 170 Project Spring 2020

## Usage: 
> python3 solver.py

## Algorithm

We can analyze the graph.

### (1) Case one, if it has a node that connects to all other nodes,then we can just return that node which costs 0 because it satisfies the requirement.

### (2) Case two, if it is a cycle, we use a built- in function to check if the edges of the graph are thesame as the cycle of the graph.

### (3) Case three, we use the algorithm to find the minimum dominating set that is an approximate minimum weighted dominating set. Then we connect the nodes in the set if they are neighbors and have edges between them. Thus, we will get the components of the graph of dominating sets. After that, we use the minimum cost to connect those components. We get the subgraph of the original graph and the nodes of the subgraph satisfy the requirement of the problem. We can optimize it by adding nodes or removing redundant nodes in order to decrease the cost of the average pairwise distance.

## Citation
### (1) [Connected Dominating Sets and its Applications](https://www.youtube.com/watch?v=H4_Qk2Ijrj4)

### (2) Near-Optimal Distributed Approximation of Minimum-Weight Connected Dominating Set (Mohsen Ghaffari, 2014)

### (3) Approximation Algorithms (Vazirani, Vijay V. , Springer Science & Business Media, 2001)