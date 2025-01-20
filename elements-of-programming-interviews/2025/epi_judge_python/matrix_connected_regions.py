from typing import List

from test_framework import generic_test

def get_valid_neighbors(image, x,y):
    out = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(image) and 0 <= ny < len(image[0]):
            out.append((nx, ny))
    return out


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    if not (image and image[0]):
        return
    init_color = image[x][y]
    stack = [(x,y)]
    visited = set()
    while stack:
        x,y = stack.pop()
        image[x][y] = 0 if init_color == 1 else 1
        for nx, ny in get_valid_neighbors(image,x,y):
            if image[nx][ny] == init_color and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append((nx,ny))
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
