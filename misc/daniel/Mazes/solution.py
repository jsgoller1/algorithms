"""
- DFS
- BFS
- A*
---------------------------
- Read file from disk
- Convert to List[List[String]]
- Keep track of X and O for start and exit
- Begin search algorithm with loop and adding children to data structure
  - Keep track of prior visited with node -> parent mapping
  - (Will always be solution, no need to return false/throw error)
  - When exit is found, walk parent map to start, modify map
  - Write modified map to disk
"""

def readMaze(filepath):
  """
  """
  with open(filepath) as f:
    mazeData = f.read().split('\n')
    maze = [ list(line) for line in mazeData if line ]
  return maze

def euclideanDistance(y1, x1, y2, x2):
  return ((y2-y1)**2 + (x2-x1)**2)**.5

def minKey(listItem):
  return listItem[0]

def findPath(maze):
  """
  """
  start = None
  end = None

  # Find X and O
  for row, rowData in enumerate(maze):
    for col, colData in enumerate(rowData):
      if maze[row][col] == 'X':
        start = (row, col)
      elif maze[row][col] == 'O':
        end = (row, col)

  parents = {start: None}
  toVisit = [[0, start]]
  endY, endX = end

  # Traverse maze to find exit
  while toVisit:
    #print(toVisit)
    curr = min(toVisit, key=minKey)
    #print(curr)
    toVisit.remove(curr)
    y,x = curr[1]

    if (y,x) == end:
      break

    if y-1 >= 0 and maze[y-1][x] != '#' and (y-1,x) not in parents:
      parents[(y-1,x)] = (y,x)
      priority = euclideanDistance(endY, y-1, endX, x)
      toVisit.append([priority, (y-1,x)])
    if x-1 >= 0 and maze[y][x-1] != '#' and (y,x-1) not in parents:
      parents[(y,x-1)] = (y,x)
      priority = euclideanDistance(endY, y, endX, x-1)
      toVisit.append([priority, (y,x-1)])
    if y+1 < len(maze) and maze[y+1][x] != '#' and (y+1,x) not in parents:
      parents[(y+1,x)] = (y,x)
      priority = euclideanDistance(endY, y+1, endX, x)
      toVisit.append([priority, (y+1,x)])
    if x+1 < len(maze[0]) and maze[y][x+1] != '#' and (y,x+1) not in parents:
      parents[(y,x+1)] = (y,x)
      priority = euclideanDistance(endY, y, endX, x+1)
      toVisit.append([priority, (y,x+1)])

  # Walk parent list to draw path
  current = parents[end]
  while current != start:
    row, col = current
    maze[row][col] = '+'
    current = parents[current]
  return maze

def render(maze, filepath):
  """
  """
  for line in maze:
    print(''.join(line))
  print("\n")

if __name__ == '__main__':
  mazeFiles = ['maze1.txt','maze2.txt','maze3.txt','maze4.txt']
  for filepath in mazeFiles:
    maze = readMaze(filepath)
    modifiedMaze = findPath(maze)
    render(modifiedMaze, filepath)
