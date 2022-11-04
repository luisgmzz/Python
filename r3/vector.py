from math import sqrt


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.__data = [x, y, z]

    def module(self):
        return sqrt(self.x**2+self.y**2+self.z**2)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def cannonical_basis(self):
        returned = []
        unit_vectors = "ijk"
        for i in range(len(self.__data)):
            print(self.__data[i], self.__data[i] != 0)
            if self.__data[i] != 0:
                if self.__data[i] == 1:
                    returned.append(unit_vectors[i])
                else:
                    returned.append(str(self.__data[i]) + unit_vectors[i])

        return " + ".join(returned)


v = Vector(1, 0, 2)
print(v.cannonical_basis())
