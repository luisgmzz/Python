a = "101"
b = "111"

def xor(a, b):
    if (not (a or b) or (a and b)):
        return False
    return True

def _or(a, b):
    if a or b:
        return True
    return False 

def _and(a, b):
    if a and b:
        return True
    return False

if len(a) > len(b):
    xd = len(a)-len(b)
    