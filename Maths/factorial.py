def recursive_fact(n: int):
    if n == 0:
        return 1
    elif n < 0:
        return None
    return n * recursive_fact(n-1)

def fact(n: int):
    helper = 1
    for i in range(1, n+1):
        helper *= i

    return helper

if __name__ == '__main__':
    print(recursive_fact(4))