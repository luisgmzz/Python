class Matrix:
    def __init__(self, data):
        self.data = data
        self.i = len(data)
        self.j = len(data[0])

    def __repr__(self):
        representation = ""
        for i in self.data:
            representation += "[ "
            for j in i:
                representation += str(j) + " "
            representation += "]\n"
        return representation 

    def __add__(self, other):
        new_matrix = []

        for i in range(len(self.data)):
            new_matrix.append([])
            for j in range(len(self.data[i])):
                new_matrix[i].append(self.data[i][j] + other.data[i][j])

        return Matrix(new_matrix)

    def __sub__(self, other):
        return self + (other * -1)

    def __mul__(self, other):
        new_matrix = []

        if (isinstance(other, int)):
            for i in self.data:
                new_matrix.append(list(map(lambda x: other*x, i)))

        return Matrix(new_matrix)


if __name__ == "__main__":
    m = Matrix([
        [2, 2],
        [2, 3]
    ])

    n = Matrix([
        [2, 3],
        [2, 3]
    ])

    print(m)