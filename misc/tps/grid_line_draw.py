import click

"""
Terminal application that allows users to draw ascii art lines to a canvas

- User starts up program; user is shown canvas (empty) then prompt -> draw -> prompt loop
- how do they input format? should not have to say point by point. 
- skip any kind of user input / parsing; focus on rendering. Hardcode user inputs for now
- Start with assumption of horizontal and vertical; then add diagonals

Constraints:
- Draw lines for now (see zoom chat)
- Fixed size is fine; lives in terminal (not side of building)

Steps:
- fixed size (101 x 101) 2d array; initialized with border lines
- running loop:
    - gather input from user (start/end point)
    - calculate the line segment 
    - write into array 
    - present to user
"""
from collections import namedtuple
from enum import Enum


class Direction(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    DIAGONAL = 3


Point = namedtuple("Point", ["x", "y"])


class Line:
    """
    Line segment; can be horizontal, vertical, or diagonal.
    Diagonals cannot be on non-cardinal directions (would need to use something
    like Bresenham's line algorithm per GPT)
    """

    def __init__(self, start, end, axis):
        self.axis = axis
        if axis in [Direction.HORIZONTAL, Direction.DIAGONAL]:
            self.start, self.end = (start, end) if start.x < end.x else (end, start)
        else:
            self.start, self.end = (start, end) if start.y < end.y else (end, start)

    def _get_draw_delta(self):
        if self.axis == Direction.HORIZONTAL:
            return Point(1, 0)
        elif self.axis == Direction.DIAGONAL:
            return Point(1, 1)
        else:
            return Point(0, 1)

    def get_points(self):
        delta = self._get_draw_delta()
        curr = [self.start.y, self.start.x]
        points = []
        while curr != [self.end.y, self.end.x]:
            points.append([curr[0], curr[1]])
            curr[0] += delta.y
            curr[1] += delta.x
        return points


class Grid:
    def __init__(self):
        self.height = 20
        self.width = 50

        middle_row = ["|"] + [" "] * self.width + ["|"]
        vertical_border_row = [" "] + ["-"] * (self.width)

        self.data = []
        self.data.append(vertical_border_row)
        for i in range(self.height):
            self.data.append(middle_row[:])
        self.data.append(vertical_border_row)

    def draw(self):
        for row in self.data:
            print("".join(row))

    def _validate_line(self, line):
        return (
            (0 <= line.start.x < self.width)
            and (0 <= line.start.y < self.height)
            and (0 <= line.end.x < self.width)
            and (0 <= line.end.y < self.height)
        )

    def add_line(self, line: Line):
        for point in line.get_points():
            if not self._validate_line(line):
                raise ValueError(
                    f"Cannot draw line from {line.start} to {line.end}; points must be between (0,0) and ({self.width, self.height})"
                )
            # NOTE: +1 to ensure it doesn't draw over the border
            self.data[point[0] + 1][point[1] + 1] = "."


# TODO: type hints
def get_horizonal_line():
    return Line(Point(1, 1), Point(10, 1), Direction.HORIZONTAL)


def get_vertical_line():
    return Line(Point(4, 10), Point(4, 19), Direction.VERTICAL)


def get_diagonal_line():
    return Line(Point(15, 5), Point(20, 10), Direction.DIAGONAL)


def get_invalid_line():
    return Line(Point(5, 5), Point(200, 200), Direction.DIAGONAL)


if __name__ == "__main__":
    grid = Grid()
    grid.add_line(get_horizonal_line())
    grid.add_line(get_vertical_line())
    grid.add_line(get_diagonal_line())
    try:
        grid.add_line(get_invalid_line())
    except ValueError as e:
        print(f"{e}")
        print("Skipping invalid line.")
    grid.draw()
