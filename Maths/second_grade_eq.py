from math import sqrt


def scg(a, b, c):
    print((b**2)-4*a*c)
    return (-b+sqrt(b**2-4*a*c))/2*a, (-b-sqrt(b**2-4*a*c))/2*a


print(scg(1, -6, -8))
