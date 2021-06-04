from statistics import mean
from random import randrange

# Number of sets
tries = int(input(
    "How many sets of groups do you want to simulate? (Every set contains 100 groups)\n"))

# Number of people per group
RANGE = int(input(
    "Enter the number of people per group (The most famous number for this paradox is 23)\n"))

#
sets_mean = []

# Loop of the sets
for i in range(tries):
    # percentagecentage of every group
    percentage = 0

    # Loop of the groups
    for j in range(100):
        # Every birthday of the people in the group
        birthdays = [randrange(366) for i in range(1, RANGE + 1)]

        birthdays.sort()

        coincidences = 0  # If there is any coincidance p += 1
        last_node = 0
        previous_last_node = 0

        for num in birthdays:
            if num == last_node:
                if num != previous_last_node:
                    coincidences += 1
                    pli = last_node
            else:
                previous_last_node = last_node
                last_node = num

        if coincidences >= 1:
            percentage += 1

    print(f"{i}- percentage is {percentage}%")
    sets_mean.append(percentage)

print(f"The average of the percentages is {mean(sets_mean)}")
