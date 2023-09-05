from sympy import FiniteSet

def isPrime(n):
    for i in range(1, n):
        if n%i == 0:
            return False
    return True 

def valido(X, Y):
    return len(X & Y) == 1 and isPrime(list(X&Y)[0])

X = FiniteSet(*[2, 3, 4, 5])
V = filter(lambda x: len(x) == 2, X.powerset())

for i in V:
print(list(V))
""" for n in range(1, 11):
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
 """