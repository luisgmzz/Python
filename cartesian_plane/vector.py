from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x, y)


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        self.points = (a.coords, b.coords)
        self.coords = (b.x - a.x, b.y - a.y)
        self.module = sqrt(self.coords[0]**2 + self.coords[1]**2)
    
    def __add__(self, other):
        return (self.coords[0] + other.coords[0], self.coords[1] + other.coords[1])
    
    def __sub__(self, other):
        return (self.coords[0] - other.coords[0], self.coords[1] - other.coords[1])

    def __mul__(self, other):
        return self.coords[0] * other.coords[0] + self.coords[1] * other.coords[1]


if __name__ == "__main__":
    p = Point(-4, 0)
    q = Point(4, 0)

    v = Vector(p, q)
    print(v.module)
    