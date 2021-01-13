# Depth First Search in Python
## Labrynth Solver
<br>

### Problem:

#### Labrynth puzzles move a marble around a maze until it finds a hole to drop though. This is a small version of that where a piece can move up, down, left and right to reach a hold in a grid. Given an two-dimentional array containing blank squares ('O'), wall squares ('X') and hole squares ('@'), find the minimun number of moves, horizontal and vertical, it takes to reach a hole from each square. If a path from a square is unatainable the distance should be negative. If the sqare is a hole the distance should be 0. An example input would be a text file containing the following information:

O X O O O <br>
O X O X X <br>
O O @ O O <br>
O O X X @ <br>
O O O O O <br>

#### The resulting output would be as follows:

4 -1 2 3 4 <br>
3 -1 1 -1 -1 <br>
2 1 0 1 1 <br>
3 2 -1 -1 0 <br>
4 3 3 2 1 <br>

### Solution:

The solution to this problem is written in Python and used depth first search. <br>
2-3 command line arguments are used, input file, output file and optional 1 for debugging messages to print. The holes are added to a stack, each adjacent square is checked for validity and if the value is adjusted that point is added to the stack to be checked again. Multiple inputs were used to check if code caught unusual cases. 