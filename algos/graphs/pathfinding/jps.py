"""
Implements the most basic version of Jump Point Search, as described in Harabor and Grastien's 2011 and
2012 papers. JPS is a variant of A* search for uniform cost grids where instead of considering every possible
neighbor of the current cell, we "jump" from the current cell to the next cell worthy of consideration in
the current direction we are heading (see the papers for a detailed explanation of why this permissible).
This allows us to skip unnecessary cells that bog down performance. We determine which cells are "worthy
of consideration" based on systematic pruning rules that are detailed below.

Assumptions:
  - Our grid is n x m (min 1x1), and contains either impassible wall cells or open traversable cells.
  - The grid has an entrance and an exit, both of which are traversable.
  - Every cell has between 0 and 8 adjacent traversable cells (cardinals and diagonals)
  - The cost of traversing from one cell to any adjacent cardinal cell is 1; diagonals cost sqrt(2).
  - Our heuristic is Chebyshev distance
-----------------------------------------------------------------------------------------
Pseudocode

direction(current, next):
  return direction needed to go from current to next

get_forced_neighbors(cell, direction):
  neighbors = []
  if direction is diagonal:
    if cell-horizontal component is wall:
      neighbors.add(cell-horizontal+vertical cell)
    if cell-vertical component is wall:
      neighbors.add(cell-vertical+horizontal cell)

  if direction is vertical:
    if left is wall:
      neighbors.add(left+vertical cell)
    if right is wall:
      neighbors.add(right+vertical cell)

  if direction is horizontal:
    if up is wall:
      neighbors.add(up+horizontal cell)
    if down is wall:
      neighbors.add(down+horizontal cell)

  return neighbors

get_natural_neighbors(cell, direction):
  neighbors = []
  if direction is diagonal:
    add next diagonal after cell, plus each cardinal neighbor for each cardinal component
  if direction is horizontal/vertical:
    add next horizontal/vertical cell after cell
  return neighbors

# Is start actually necessary?
jump(cell, direction, start, exit):
  next = cell + direction
  if next is invalid or a wall:
    return null
  if next is exit:
    return next
  if get_forced_neighbors(cell, direction):
    return next
  if direction is diagonal:
    for each cardinal component of the diagonal
      return jump(next, cardinal direction, start, exit) if it's not null
  return jump(next, direction, start, goal)

successors(cell, parents):
  to_visit = empty set
  neighbors = get_natural_neighbors(cell, direction(
      cell, parents[cell])) + get_forced_neighbors(cell, direction(cell, parents[cell]))
  for each in neighbors:
    d = direction(cell, each)
    to_visit.add(jump(each, dir)) if jump returns non-null
  return to_visit


jps(maze, start, exit):
  parents = dictionary initialized with neighbor: start for every traversable neighbor of start
  pq = priority queue initialized for all valid neighbors of start; queue elements are read "(priority, cost, cell)",
       so each valid neighbor is initialized as (heuristic+cost, cost, cell)
  while pq is nonempty:
    _, cost, current = dequeue lowest priority element
    if current == goal:
      return parents
    pq.enqueue(successors(current, parents))
"""
import collections
from graphs.pathfinding.heuristic_search import chebyshev_distance
from graphs.pathfinding.maze import HORIZONTALS, VERTICALS, DIAGONALS, DIRECTIONS


def get_natural_neighbors(current, direction):
    neighbors = [(current[0]+direction[0], current[1]+direction[1])]
    if direction in DIAGONALS:
        neighbors.append((current[0], current[1]+direction[1]))
        neighbors.append((current[0]+direction[0], current[1]))
    return neighbors


def get_forced_neighbors(maze, current, direction):
    neighbors = []
    if direction in HORIZONTALS:
        if maze.is_wall((current[0] - 1, current[1])):
            neighbors.append((current[0] - 1, current[1]+direction[1]))
        if maze.is_wall((current[0] + 1, current[1])):
            neighbors.append((current[0] + 1, current[1]+direction[1]))
    elif direction in VERTICALS:
        if maze.is_wall((current[0], current[1]-1)):
            neighbors.append((current[0]+direction[0], current[1]-1))
        if maze.is_wall((current[0], current[1]+1)):
            neighbors.append((current[0]+direction[0], current[1]+1))
    elif direction in DIAGONALS:
        if maze.is_wall((current[0]-direction[0], current[1])):
            neighbors.append((current[0]-direction[0], current[1]+direction[1]))
        if maze.is_wall((current[0], current[1]-direction[1])):
            neighbors.append((current[0]+direction[0], current[1]-direction[1]))
    return neighbors


def jump(maze, cell, direction):
    next_cell = (cell[0] + direction[0], cell[1] + direction[1])
    if not maze.is_visitable(next_cell):
        return None
    if next_cell == maze.exit:
        return next_cell
    if get_forced_neighbors(next_cell, direction):
        return next_cell
    if direction in DIAGONALS:
        if jump(maze, next_cell, (direction[0], 0)) or jump(maze, next_cell, (0, direction[1])):
            return next_cell
    return jump(maze, next_cell, direction)


def successors(maze, current, direction):
    successors = []
    neighbors = get_natural_neighbors(current, direction) + get_forced_neighbors(current, direction)
    for cell in neighbors:
        jump_neighbor = jump(maze, cell, direction)
        if jump_neighbor:
            successors += jump_neighbor
    return successors


def initialize(maze):
    parents = {}
    costs = {}
    pq = collections.deque([])
    for direction in DIRECTIONS:
        neighbor = (maze.entrance[0] + direction[0], maze.entrance[1] + direction[1])
        if maze.is_visitable(neighbor):
            priority = 1 + chebyshev_distance(neighbor, maze.exit)
            pq.append((priority, 1, neighbor))
            parents[neighbor] = maze.entrance
            costs[neighbor] = 1
    return parents, costs, pq


def jps(maze, show_state=False):
    parents, costs, pq = initialize(maze)
    while pq:
        _, cost, current = pq.popleft()
        if show_state:
            maze.draw_search_state(parents.keys(), [item[2] for item in pq], current)
            print(pq)
        if current == maze.exit:
            break
        parent = parents[current]
        direction = (current[0]-parent[0], current[1]-parent[1])
        jump_neighbors = successors(maze, current, direction)
        for jn_cost, jn_cell in jump_neighbors:
            if jn_cell not in parents:
                parents[jn_cell] = current
                cost[jn_cell] = cost + jn_cost
                distance = chebyshev_distance(current, jn_cell)
                pq.append((cost[jn_cell] + distance, cost[jn_cell], jn_cell))
            elif jn_cost < costs[jn_cell]:
                costs[jn_cell] = jn_cost + cost
                parents[jn_cell] = current

    return parents if maze.exit in parents else None
