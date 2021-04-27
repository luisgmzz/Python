from random import randrange


RANGE = 100

random_number = randrange(RANGE + 1)
print(random_number)

loops = 1

logs = open("logs.txt", "r,a")
lines = logs.readlines()
game = lines[0]
points = lines[1]

while True:
    user_number = int(input("Enter a number:\n"))

    if random_number < user_number:
        print("Number is to big")
        logs.append("hola")
    elif random_number > user_number:
        print("Number is to small")
    elif random_number == user_number:
        print("Winner!")
        break

    loops += 1

print(logs.readlines())


print(f"You needed {loops} tries.")
