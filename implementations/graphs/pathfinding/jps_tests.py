import graphs.pathfinding.maze as maze
from graphs.pathfinding.jps import get_forced_neighbors, get_natural_neighbors


def assert_list_equal(list1, list2):
    assert sorted(list1) == sorted(list2)


if __name__ == '__main__':
    empty_matrix = [[' ' for _ in range(2)] for _ in range(2)]

    horizontal_test_1 = [
        [' ', ' ', ' '],
        ['O', ' ', 'X'],
        [' ', '#', ' ']
    ]
    horizontal_test_matrix = maze.Maze(matrix=horizontal_test_1)
    assert_list_equal(get_natural_neighbors(horizontal_test_matrix, (1, 1), maze.RIGHT), [(1, 2)])
    assert_list_equal(get_forced_neighbors(horizontal_test_matrix, (1, 1), maze.RIGHT), [(2, 2)])

    horizontal_test_2 = [
        [' ', '#', ' '],
        ['O', ' ', 'X'],
        [' ', ' ', ' ']
    ]
    horizontal_test_matrix = maze.Maze(matrix=horizontal_test_2)
    assert_list_equal(get_natural_neighbors(horizontal_test_matrix, (1, 1), maze.RIGHT), [(1, 2)])
    assert_list_equal(get_forced_neighbors(horizontal_test_matrix, (1, 1), maze.RIGHT), [(0, 2)])

    vertical_test_1 = [
        [' ', 'X', ' '],
        [' ', ' ', '#'],
        [' ', 'O', ' ']
    ]
    vertical_test_matrix = maze.Maze(matrix=vertical_test_1)
    assert_list_equal(get_natural_neighbors(vertical_test_matrix, (1, 1), maze.UP), [(0, 1)])
    assert_list_equal(get_forced_neighbors(vertical_test_matrix, (1, 1), maze.UP), [(0, 2)])

    vertical_test_2 = [
        [' ', 'X', ' '],
        ['#', ' ', ' '],
        [' ', 'O', ' ']
    ]
    vertical_test_matrix = maze.Maze(matrix=vertical_test_2)
    assert_list_equal(get_natural_neighbors(vertical_test_matrix, (1, 1), maze.UP), [(0, 1)])
    assert_list_equal(get_forced_neighbors(vertical_test_matrix, (1, 1), maze.UP), [(0, 0)])

    diag_test_1 = [
        [' ', ' ', 'X'],
        ['#', ' ', ' '],
        ['O', ' ', ' ']
    ]
    diag_test_matrix = maze.Maze(matrix=diag_test_1)
    assert_list_equal(get_natural_neighbors(diag_test_matrix, (1, 1), maze.UP_RIGHT), [(0, 1), (0, 2), (1, 2)])
    assert_list_equal(get_forced_neighbors(diag_test_matrix, (1, 1), maze.UP_RIGHT), [(0, 0)])

    diag_test_1 = [
        [' ', ' ', 'X'],
        [' ', ' ', ' '],
        ['O', '#', ' ']
    ]
    diag_test_matrix = maze.Maze(matrix=diag_test_1)
    assert_list_equal(get_natural_neighbors(diag_test_matrix, (1, 1), maze.UP_RIGHT), [(0, 1), (0, 2), (1, 2)])
    assert_list_equal(get_forced_neighbors(diag_test_matrix, (1, 1), maze.UP_RIGHT), [(2, 2)])
