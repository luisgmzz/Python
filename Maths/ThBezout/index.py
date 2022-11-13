from thbezout import bezout_identity
from mcd import mcd

a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))

d = mcd(a, b)["mcd"]
bz = bezout_identity(a, b)
print(f"mcd({a}, {b}) = {d}")
print(f"La indentidad de bezout es: {a}*({bz[0]}) + {b}*({bz[1]}) = {d}")





    