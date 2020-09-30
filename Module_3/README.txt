MazeReader reads a text file containing the maze as input with the following format:

WALL: #
OPEN SPACE: .
START: o
FINISH: *

Every row of the maze should be of uniform length.


The MazeReaded constructor asks for the filename to be input in the command line, then reads the file and stores the maze.

The MazeSolver constructor takes a MazeReader object as an argument. The solve() function will output the solution to the maze contained in the MazeReader object. solve() outputs an empty list if no solution exists.

Also included is main.py, which demonstrates how to use the MazeReader and MazeSolver classes.