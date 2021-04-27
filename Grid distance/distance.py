from grid import Grid
from vector import *

try:
    size = int(input("Enter grid's dimensions:\n"))
except ValueError:
    raise ValueError("Input must be a number")

if size > 100:
    raise ValueError("Grid size is to big")
elif size < 2:
    raise ValueError("Grid size is to small")


# Functions to get both y and x components
def get_y_component(matrix: list, identifier: str):
    for i in matrix:
        if identifier in i:
            return matrix.index(i)


def get_x_component(matrix: list, y_component: list, identifier: str):
    for i in matrix[y_component]:
        if i == identifier:
            return matrix[y_component].index(i)


# Initializing our grid
grid = Grid(size)

grid.put_nums()

grid.show()

""" 
Grid example:
grid = [
    ["x", "x", "x"],
    ["x", "0", "x"],
    ["x", "x", "1"]
]
"""

# Building our points and assigning them to a number
origin = Point(None, None)
destiny = Point(None, None)

relations = {"0": origin, "1": destiny}

# Applying the functions to both points
for i in range(2):
    relations[str(i)].y = get_y_component(grid.data, str(i))
    relations[str(i)].x = get_x_component(
        grid.data, relations[str(i)].y, str(i))

# Finally finding the vector and it's module
vector = Vector(origin, destiny)

print(vector.module)
