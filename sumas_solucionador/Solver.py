from Game import Game


class Solver:
    def __init__(self, game: Game):
        self.game = game


g = Game("game.txt")


def create_posibilities(num: int) -> tuple[int]:
    for i in range(num):
        for j in range(num):
            if i+j == num:
                yield (i, j)


print(set(create_posibilities(100)))

for i in g.get_sums()["x"]:
    pass
    # create_posibilities(i)
