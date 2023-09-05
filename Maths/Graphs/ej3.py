from itertools import permutations
from math import factorial
vertices = {1, 2, 3, 4, 5, 6, 7, 8}



print("TODAS LAS PERMUTACIONES POSIBLES")
lista = list(permutations(vertices, 2))
print(len(lista))

print("TODOS LOS EJES POSIBLES")
no_repetidos = []
for i in lista:
    if ((i[1], i[0]) not in no_repetidos):
        no_repetidos.append(i)

print(no_repetidos)


def subconjuntos(lista):
    return sr([], sorted(lista))

def sr(actual, conjunto):
    if conjunto:
        return sr(actual, conjunto[1:]) + sr(actual + [conjunto[0]], conjunto[1:])
    return [actual]

total = factorial(len(no_repetidos)) /  factorial(len(no_repetidos) - 26)
print(total)