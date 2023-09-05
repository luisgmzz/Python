UPPER_BOUND = 100

def primes(upper_bound):
    initial_list = [{"x": i, "labeled": False} for i in range(2, upper_bound+1)]
    i = 0
    while initial_list[i]["x"]**2 <= upper_bound:
        for 