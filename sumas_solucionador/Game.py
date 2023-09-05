from os import getcwd
from colorama import init, Back, Fore

init()


class Number:
    _active = True
    _selected = False

    def __init__(self, num):
        self.num = int(num)

    def __repr__(self):
        return str(self.num)

    def deactivate(self):
        if not self._selected:
            self._active = False

    def select(self):
        if self._active:
            self._selected = True

    def is_active(self):
        return self._active

    def is_selected(self):
        return self._selected

    def get_color(self):
        if not self._active:
            return ""
        elif self._selected:
            return Fore.RED
        return Fore.BLACK


class Game:
    _sums_x: list[int] = []
    _sums_y: list[int] = []
    _grid: list[list[Number]] = []
    _solution: list[list[Number]] = []
    _dim = 0
    _file_name = ""

    def __init__(self, file_name: str):
        self._file_name = file_name

    def create(self):
        file = f"{getcwd()}\\{self._file_name}"

        with open(file, "r") as f:
            self._sums_x = list(map(lambda x: int(x), f.readline().split(" ")))
            self._sums_y = list(map(lambda x: int(x), f.readline().split(" ")))
            self._dim = len(self._sums_x)

            for _ in range(self._dim):
                # Mapping raw str to Number
                line = list(map(lambda x: Number(
                    x), f.readline()[:-1].split(" ")))
                self._grid.append(line)

            for _ in range(self._dim):
                solved_line = list(
                    map(lambda x: Number(x), f.readline()[:-1].split(" ")))

                for j in range(self._dim):
                    solved_line[j].deactivate(
                    ) if solved_line[j].num == 0 else solved_line[j].select()

                self._solution.append(solved_line)

    def _get_rep(self, is_solution: bool):
        table = self._solution if is_solution else self._grid
        # Sums of the columns
        rep = f"+ {Back.GREEN}{' '.join(map(lambda x: str(x), self._sums_x))}{Back.RESET}\n"

        for i in range(self._dim):
            # Sums of the rows
            rep += f"{Back.GREEN}{self._sums_y[i]}{Back.RESET} "

            # Numbers
            for j in range(self._dim):
                color = table[i][j].get_color()
                # Wheter choose a from the solution or from the grid
                if is_solution and table[i][j].is_active():
                    number = self._solution[i][j]
                else:
                    number = self._grid[i][j]
                rep += f"{Back.WHITE}{color}{number} {Back.RESET}{Fore.RESET}"
            rep += "\n"
        return rep

    def __repr__(self):
        return self._get_rep(False)

    def show_solution(self):
        print(self._get_rep(True))

    def _execute(self, x, y):
        if self._solution[x][y].num != 0:
            self._grid[x][y].select()
        else:
            self._grid[x][y].deactivate()

    def deactivate(self, x, y):
        self._execute(x, y)
        return self._solution[x][y].num == 0

    def select(self, x, y):
        self._execute(x, y)
        return self._solution[x][y].num != 0

    def is_completed(self):
        for i, j in zip(self._grid, self._solution):
            for tile, sol in zip(i, j):
                if (not tile.is_selected()) and sol.is_selected():
                    return False
        return True

    def get_dimension(self):
        return self._dim

    def get_sums(self):
        return {
            "x": self._sums_x,
            "y": self._sums_y
        }


if __name__ == "__main__":
    g = Game("game.txt")
    g.create()

    lives = 3
    while True:
        print(g)
        choose = input("Want to deactivate(d) or select(s)?: ").lower()
        x = int(input("Insert row: ")) - 1
        y = int(input("Insert column: ")) - 1

        if x > g.get_dimension() or y > g.get_dimension():
            print(f"Choose a number between 1 and {g.get_dimension()}")
            continue

        good_move = True

        if choose == "d":
            good_move = g.deactivate(x, y)
        elif choose == "s":
            good_move = g.select(x, y)
        else:
            print("Choose a correct option")

        if not good_move:
            print("You lost a life!")
            lives -= 1

        if lives == 0:
            print("You lost")
            break

        if g.is_completed():
            print("You won!")
            break
