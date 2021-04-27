from vector import *


class Line:
    def __init__(self, slope: int, coord_at_origin: int = 0):
        self.slope = slope
        self.coord_at_origin = coord_at_origin

        if coord_at_origin == 0:
            self.explicit_equation = f"{self.slope}x"
        elif coord_at_origin > 0:
            self.explicit_equation = f"{self.slope}x + {self.coord_at_origin}"
        else:
            self.explicit_equation = f"{self.slope}x - {abs(self.coord_at_origin)}"

        self.director_vector = Vector(
            Point(1, self.function(1)), Point(2, self.function(2)))

    def function(self, x: int):
        return int(self.slope * x + self.coord_at_origin)
