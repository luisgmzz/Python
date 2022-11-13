from mcd import mcd

def bezout_identity(a: int, b: int)-> list[int]:
    d = mcd(a, b)
    table: list = d["table"]
    index: int = d["iterations"]

    values: list = [[] for i in range(index)]
    values.append([1, 0])
    for i in range(index-1, -1, -1):
        last_iteration = values[i+1]
        quotient: int = table[i][3]    

        # ∃ m, n ϵ Z: d = ax + by
        x = last_iteration[1]
        y = last_iteration[0] - last_iteration[1]*quotient

        values[i] = [x, y]
    
    return values[0]

if __name__ == "__main__":
    a = 2342313
    b = 9
    
    bz = bezout_identity(a, b)
    d = mcd(a, b)["mcd"]

    x = bz[0]
    y = bz[1]
    
    print(d)
    print(a*x+b*y == d)




