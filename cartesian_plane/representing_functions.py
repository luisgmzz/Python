from grid import Grid
from lines_and_parables import Line, Parable
from vector import *
from colorama import init, Fore

# Initializing colorama
init(True)

grid = Grid(50)
parable = Parable(1, 10, 1)
line = Line(Vector)

for i in range(grid.size):
    a = parable.function(i)
    try:
        grid.data[a][i] = Fore.YELLOW + "r"
    except:
        continue

grid.show()
