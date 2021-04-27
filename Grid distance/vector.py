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
        self.value = (b.x - a.x, b.y - a.y)
        self.module = sqrt(self.value[0]**2 + self.value[1]**2)
