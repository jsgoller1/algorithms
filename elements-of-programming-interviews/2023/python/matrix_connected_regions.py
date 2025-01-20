from typing import List

from test_framework import generic_test

from collections import deque


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    if not image or not image[0]:
        return

    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < len(image) and 0 <= y < len(image[0])
    if not is_valid(x, y):
        return

    fill_color = not image[x][y]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        image[x][y] = fill_color
        for n_x, n_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if is_valid(n_x, n_y) and not (image[n_x][n_y] == fill_color):
                q.append((n_x, n_y))
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
