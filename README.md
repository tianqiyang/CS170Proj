# CS 170 Project Spring 2020

Take a look at the project spec before you get started!

Requirements:

You'll only need to install networkx to work with the starter code. For installation instructions, follow: https://networkx.github.io/documentation/stable/install.html

Files:
- `parse.py`: functions to read/write inputs and outputs
- `solver.py`: where you should be writing your code to solve inputs
- `utils.py`: contains functions to compute cost and validate NetworkX graphs

When writing inputs/outputs:
- Make sure you use the functions `write_input_file` and `write_output_file` provided
- Run the functions `read_input_file` and `read_output_file` to validate your files before submitting!
  - These are the functions run by the autograder to validate submissions


algo0:
find mst

algo1:
find mds and connect them together.

algo2:
add some nodes to minimize value.

algo3:
remove some nodes to minimize value.

algo4:
repeatly remove and add nodes to minimize value.

algo5:
if mst has less value than other, try to remove some nodes or add nodes based on mst.