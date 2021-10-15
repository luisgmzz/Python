def binary(number: int):
    binary_number = ""
    helper = 0
    if number == 1:
        return "1"
    elif number == 2:
        return "01"
    else:
        while number > 1:
            remainder = int(number) % 2
            binary_number += str(remainder)
            helper += remainder
            number /= 2
        if helper == 0:
            binary_number += "1"
        
        return binary_number[::-1]
    

if __name__ == "__main__":
    num = int(input())
    if num >= 0:
        binary(num)
    else:
        print("The number must be positive!")