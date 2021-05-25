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
    p = Point(2, 3)
    q = Point(3, 2)

    r = Point(4, 3)
    s = Point(3, 5)

    v = Vector(p, q)
    u = Vector(r, s)
    print(v*u)
    