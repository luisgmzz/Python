

values = { "A": 10, "B": 11 , "C": 12, "D": 13, "E": 14, "F": 15 }

def hexadecimal(number: string):
    number = number[::-1]
    hexadecimal_number = 0
    position = 1
    for word in number:
        try:
            hexadecimal_number += int(word) * position
        except ValueError:
            hexadecimal_number += values[word.upper()] * position
        position *= 16
    return hexadecimal_number

if __name__ == "__main__":
    num = input()
    print(hexadecimal(num))