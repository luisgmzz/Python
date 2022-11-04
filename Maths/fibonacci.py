from math import sqrt, floor


def recursive_fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


def for_fib(n: int) -> int:
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def form_fib(n: int) -> int:
    golden_ratio = (1+sqrt(5))/2
    num = (1/sqrt(5))*(golden_ratio**n-(-1/golden_ratio)**n)
    return floor(num)


print(form_fib(11))
