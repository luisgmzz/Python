import random
from vector import Point
from colorama import init, Fore

init(autoreset=True)


class Grid:
    def __init__(self, size: int):
        # Initializing the grid
        self.size = size

        self.data = [["x" for i in range(self.size)] for i in range(self.size)]

    def put_nums(self):
        self.__origin = Point(random.randrange(0, self.size),
                              random.randrange(0, self.size - 1))
        self.__destiny = Point(random.randrange(0, self.size),
                               random.randrange(0, self.size - 1))
        while self.__destiny == self.__origin:
            self.__destiny = (random.randrange(0, self.size),
                              random.randrange(0, self.size - 1))

        self.data[self.__origin.coords[0]][self.__origin.coords[1]] = "0"
        self.data[self.__destiny.coords[0]][self.__destiny.coords[1]] = "1"
    
    def put_rect(self):
        pass

    def show(self):
        for i in self.data:
            for j in i:
                if j == "0" or j == "1":
                    j = Fore.YELLOW + j
                print(j, end="   ")
            print()
            print()
