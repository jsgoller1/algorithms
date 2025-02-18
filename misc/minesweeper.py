"""
Constraints:
- N x M fits in memory 
- 0 to N x M mines 
- Don't need to worry about user interaction specifically (nice to have)

- Board is an N x M grid -> 2D array 
    - Each cell has 3 states:
        - Revealed, with numn
        - Hidden, no bomb
        - Hidden, bomb
        - Hidden, game over 

- Use game loop
    - Init with random number of bombs
    - State starts as RUNNING
    - waits for input from user (x,y) -> translate to y,x
    - If cell is open, reject and re-prompt
    - If cell is closed, check if bomb 
    - If bomb, set game state to LOST 
    - Otherwise, do BFS starting from cell setting all non-bomb cells to open
        - BFS traverses closed neighbors iff all neighbors (8) are non-bomb; otherwise, cell is revealed with number
"""
import random
from collections import deque 
# NOTE: C style; decomposition into functions
# TODO: should have classes passed between function; may use raw types for time constraint 
# TODO: type hints

# TODO: do these as enums
# Probably better to have consistent types in array
HIDDEN_NO_BOMB = 'HNB'
HIDDEN_BOMB = 'HB'
REVEALED = ''
REVEALED_BOMB = 'B'

# Game statuses
PLAYING = 0
LOST = 1
WON = 2

def add_bombs_to_board(grid, bomb_count):
    """
    Randomly add bombs til we have enough
    """
    if not grid:
        return 

    height, width = len(grid), len(grid[0])

    bombs_added = 0
    while bombs_added < bomb_count:
        y = random.randint(0, height-1)
        x = random.randint(0, width-1)
        if grid[y][x] == HIDDEN_NO_BOMB:
            grid[y][x] = HIDDEN_BOMB
            bombs_added += 1 
    
class BoardCreationError(Exception):
    pass

def create_board(height, width, bomb_count):
    if width * height < bomb_count:
        raise BoardCreationError(f"Cannot fit {bomb_count} into {height}*{width} grid")
    # Start with empty grid
    grid = []
    for row_i in range(height):
        row = [HIDDEN_NO_BOMB for _ in range(width)]
        grid.append(row)

    add_bombs_to_board(grid, bomb_count)
    return grid

def get_valid_neighbors(grid, y, x):
    """
    Bounds checking helper function 
    """
    deltas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    neighbors = []
    for dy, dx in deltas:
        ny, nx = y + dy, x + dx 
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            neighbors.append((ny, nx))
    return neighbors

def get_bomb_neighbors(grid, neighbors):
    bomb_count = 0 
    for ny, nx in neighbors:
        if grid[ny][nx] == HIDDEN_BOMB:
            bomb_count += 1 
    return bomb_count

def bfs(grid, y, x):
    """
    Mutates board in-place
    """
    if grid[y][x] is not HIDDEN_NO_BOMB:   
        return 
    q = deque([(y,x)])
    visited = set([(y,x)])
    while q: 
        cy, cx = q.popleft()
        neighbors = get_valid_neighbors(grid, cy, cx)
        bomb_count = get_bomb_neighbors(grid, neighbors)
        grid[cy][cx] = bomb_count
        if bomb_count == 0:
            for ny, nx in neighbors:
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    q.append((ny, nx))

def apply_choice(grid, y, x) -> int:
    """
    Modify grid in place:
    - Ignore choice on revealed square
    - Lose on hidden bomb
    - BFS on hidden no bomb 

    Return new game state
    """
    if grid[y][x] == REVEALED:
        return PLAYING

    if grid[y][x] == HIDDEN_BOMB:
        grid[y][x] = REVEALED_BOMB
        return LOST

    bfs(grid, y, x)
    return PLAYING

def test_board_creation(height, width, bombs_needed):
    # Test: board is correctly created
    grid = create_board(height, width, bombs_needed)
    bomb_count = 0
    for row in grid:
        for cell in row: 
            bomb_count += 1 if cell == HIDDEN_BOMB else 0
    assert bomb_count == bombs_needed

for height, width, bombs in [
    (10, 10, 20),
    (10, 10, 0),
    (10, 10, 20000),
]:
    try:
        test_board_creation(height, width, bombs)
        print(f"PASS: Board {height} x {width} is initialized correctly created {bombs} bombs")
    except BoardCreationError:
        print(f"PASS: Board {height} x {width} is initialized correctly handled with {bombs} bombs")

def compare_boards_with_click_action(input_board, expected_board, click_action):
    y, x = click_action
    apply_choice(input_board, y, x)
    for row_actual, row_expected in zip(input_board, expected_board):
        try:
            assert row_actual == row_expected
        except AssertionError:
            for row in input_board:
                print(row)

            for row in expected_board:
                print(row)

            f"FAIL: {row_actual} != {row_expected}"
            raise 
    print(f"Pass: Click action {click_action} on boards")


# Test reveal on clicking on non-bombed square in rightmost column
board = [
    [HIDDEN_BOMB, HIDDEN_NO_BOMB, HIDDEN_NO_BOMB],
    [HIDDEN_BOMB, HIDDEN_NO_BOMB, HIDDEN_NO_BOMB],
    [HIDDEN_BOMB, HIDDEN_NO_BOMB, HIDDEN_NO_BOMB]
]
expected_reveal = [
    [HIDDEN_BOMB, 2, 0],
    [HIDDEN_BOMB, 3, 0],
    [HIDDEN_BOMB, 2, 0]
]
click_action = (0, 2)
compare_boards_with_click_action(board, expected_reveal, click_action)

# Test reveal on clicking on non-bombed square in rightmost column
board_bomb_click = [
    [HIDDEN_BOMB, HIDDEN_NO_BOMB, HIDDEN_NO_BOMB],
    [HIDDEN_BOMB, HIDDEN_NO_BOMB, HIDDEN_NO_BOMB],
    [HIDDEN_BOMB, HIDDEN_NO_BOMB, HIDDEN_NO_BOMB]
]
expected_reveal_bomb_click = [
    [REVEALED_BOMB, HIDDEN_NO_BOMB, HIDDEN_NO_BOMB],
    [HIDDEN_BOMB, HIDDEN_NO_BOMB, HIDDEN_NO_BOMB],
    [HIDDEN_BOMB, HIDDEN_NO_BOMB, HIDDEN_NO_BOMB]
]
click_action = (0, 0)
compare_boards_with_click_action(board_bomb_click, expected_reveal_bomb_click, click_action)
