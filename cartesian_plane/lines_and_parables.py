from vector import *


""" class Line:
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
        return int(self.slope * x + self.coord_at_origin) """

class Line:
    def __init__(self, director_vector: Vector, coord_at_origin: int = 0):
        self.director_vector = director_vector
        self.a = -director_vector.b
        self.b = director_vector.a
        self.c = coord_at_origin
        self.implicit_equation = f"{self.a}x + {self.b}y + {self.c}"

    def function(self, x: int):
        return (self.a*x + self.c) // self.b

class Parable:
    def __init__(self, a, b, c):
       self.a = a
       self.b = b
       self.c = c

       self.formula = f"{self.a}x² + {self.b}x + {c}"


    def function(self, x):
        return self.a*x**2 + self.b*x + self.c

if __name__ == "__main__":
    l = Line(3, 3, 4)