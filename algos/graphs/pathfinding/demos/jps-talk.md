# JPS talk
## Intro
Let's start with some Polya-ing:

**Problem, v1**
(Show multiple paths maze)
Suppose we are playing a maze game. The maze is represented by a N x M grid of cells.
The player starts in cell O at (y1, x1) and wins by navigating to cell X at (y2,x2).
Every cell is either empty, or contains an impenetrable wall. How do we find the
shortest path from O to X?

Input: array of array of strings; " " represents a traversable cell, "#" represents
a wall, "O" represents the start and "X" the exit.
Output: array of (y,x) pairs representing the shortest path.

**Understand**
- This sounds like a graph problem. So what do we need to know?
  - `What are the nodes and edges?`
    - The nodes are cells, and edges are between any two cells who are
      adjacent on the cardinal directions or a diagonal.
  - `What does shortest mean? (i.e. is the graph weighted?)`
    - Shortest will mean the set of edges starting at X and ending at O,
      in order, that have the lowest total cost to traverse.
    - Not weighted - the cost of going from cell to cell is the same.
  - `Is the graph directed?`
    - No - it is possible to go from any neighboring cell to any neighboring
      cell given
  - `Is the graph complete?`
    - Not necessarily! It is possible no path exists from X to O, in which case
      we should return an empty array.
  - `What constraints are there on the input?`
    - We will always have an array of at least one array of at least two strings,
      one of which will always be "X" and the other will always be "O".
    - The maze could be very, very large (get largest from papers).

**Plan**
To quote our Lord and Savior Steve Skiena, we want to invent `graphs, not graph algorithms`. So
what algorithms should we reach for?
- DFS will find a path, but not necessarily the shortest one.
- BFS will find the shortest path, but exhaustively.
  - Djikstra's algorithm _is_ just a BFS for unweighted graphs.
  - How does BFS work? Review and execute.
  - Demo BFS
- A* search is excellent and will get us most of the way there.
  - How does A* work? Review

**Execute**
Show that A* works.

**Review**
Show that A* wastes space on graphs with open zones.
