"""
Given a robot cleaner in a room modeled as a grid. Each cell in the grid can be empty or blocked.
The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made
is 90 degrees. When it tries to move into a blocked cell, its bumper sensor detects the obstacle
and it stays on the current cell. Design an algorithm to clean the entire room using only the 4
given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}

Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

Notes:
- The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
- The robot's initial position will always be in an accessible cell.
- The initial direction of the robot will be facing up.
- All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
- Assume all four edges of the grid are all surrounded by wall.
---------------------------------------------------------------
- In: list[list[int]]
- Out: None

- For this problem, we need to visit every cell on the grid. This can be accomplished
  with a graph search. BFS will not be appropriate because we will need to "teleport" as
  our next node from the priority queue will not be adjacent to our current node. For a
  DFS, we can represent popping the stack by going back to a previously visited cell.
  We can do this but need to be careful about how we use our visited array.
- A complication exists around determining what cell we are in. Since we are only able to
  turn left or right, if we move forward given a heading and position, we can determine what
  cell we land in.
- Should we construct a MST?
- Does this reduce to the TSP? Sort of - not a shortest trip, but does need to visit every
  cell.
- Does "try to visit every neighbor, return to parent if impossible" work?
-------------------------------------------------------------------
canVisit()
  false if cell is within bounds
  false if cell is a 0
  otherwise true

cleanRoom()
  keep visited set
  initialize heading to up
  set cleaning to true
  set current to (1,3)
  set parents to {(1,3): None}
  while cleaning:
    clean current if not previously cleaned
    get all neighbors; if canVisit(), go to the first

move(start cell, end cell, current heading)
  adjust heading to face correct direction
  call robot.move()
------------------------------------------
- Is the stack necessary? Could we just rescan for available cells?
- Should we keep a from-dictionary and just return to parent if no cells can be visited?
"""

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]


class Solution(object):
    def canVisit(self, cell):
        return

    def move(self, src, dest, heading):
        return

    def cleanRoom(self, robot):
        visited = set()
        heading = UP

        while stack:
            self.move(parent, curr, heading)
            robot.clean()
            for direction in DIRECTIONS:
                visitableNeighbors = False
                if self.canVisit(curr + direction):
                    stack.append(curr + direction, curr)
                    visitableNeighbors = True
            if not visitableNeighbors:

        return
