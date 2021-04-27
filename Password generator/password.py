import random as rd


abc = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m",
       14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}


def create_password(n):
    password = ""
    f = ""
    while len(password) < n:
        for word in abc:
            rb = rd.randrange(3)
            rn = rd.randint(1, 37)
            if len(password) == n:
                break
            elif rn == word:
                if rb == 0:
                    password += abc[word].upper()
                else:
                    password += abc[word]

    return password


if __name__ == "__main__":
    password_length = int(input())
    print(create_password(password_length))
