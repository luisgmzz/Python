import random
from vector import Point
from colorama import init, Fore
from lines_and_parables import *

# Initializing colorama with autoreset
init(autoreset=True)


class Grid:
    def __init__(self, size: int):
        self.size = size  # Dimensions of the grid (size*size)
        self.data = [["x" for i in range(self.size)] for i in range(
            self.size)]  # Matrix that represents the grid

    def put_nums(self):
        """
        Puts 2 points objetcs in the grid in random positions,
        the representation of this points are 0 and 1
        """
        self.__origin = Point(random.randrange(0, self.size),
                              random.randrange(0, self.size - 1))
        self.__destiny = Point(random.randrange(0, self.size),
                               random.randrange(0, self.size - 1))

        # We use this to handle if both points are in the same coordinates
        while self.__destiny == self.__origin:
            self.__destiny = (random.randrange(0, self.size),
                              random.randrange(0, self.size - 1))

        self.data[self.__origin.coords[0]][self.__origin.coords[1]] = "0"
        self.data[self.__destiny.coords[0]][self.__destiny.coords[1]] = "1"

    def put_rect(self):
        pass

    def show(self):
        for i in self.data[::-1]:
            for j in i:
                if j == "0" or j == "1":
                    j = Fore.YELLOW + j
                print(j, end="   ")
            print()
            print()
