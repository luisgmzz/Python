def sobre(a, b):
    if b == 0 or a == b:
        return 1
    else:
        return sobre(a-1, b) + sobre(a-1, b-1)

print(sobre(36, 26))