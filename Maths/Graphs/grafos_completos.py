from itertools import permutations

def sumatorio(inicio, final=0):
    suma = 0
    if final != 0:
        for i in range(inicio, final+1):
            suma += i
    else:
        for i in range(1, inicio+1):
            suma += i
    return suma
NUM_VERTICES = 4
for i in range(2, 11):
    vertices = {j for j in range(i)}

    lista = list(permutations(vertices, 2))

    # Filtrar ejes repetidos
    for j in range(len(lista)):
        lista[j] = tuple(set(lista[j]))
    no_repetidos = set(lista) 

    print("Vertices:", i, "Ejes:", len(no_repetidos), "Suma", sumatorio(i-1))