from sympy import FiniteSet

def valido(A, B):
    val = False
    for i in A:
        if i in B and not val:
            val = True
        elif i in B and val:
            return False
    return val

for n in range(1, 11):
    members = [i for i in range(1, n+1)]
    X = FiniteSet(*members)

    Px = X.powerset()

    vals = 0
    pares = []
    for i in Px:
        for j in Px:
            if valido(i, j) and {j, i} not in pares:
                pares.append({j, i})
                vals += 1
    print(n, ": ", vals)
