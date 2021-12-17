# crab submarines can only move horizontally: data is the x position for each crab
# make all horizontal positions match with as few moves as possible
# each move increases the cost of fuel by +1 (i.e., first move is 1, second is 2 ...)
import statistics
import math


def get_fuel(spaces_moved):
    return (spaces_moved * (spaces_moved + 1)) / 2


def main():
    with open("data.txt") as data:
        crabs = list(map(int, data.readline().split(',')))
    print(crabs)

    max_x = crabs[0]
    min_x = crabs[0]
    for crab in crabs:
        if crab < min_x:
            min_x = crab
        if crab > max_x:
            max_x = crab

    mean = statistics.mean(crabs)
    means = [math.ceil(mean), math.floor(mean)]

    fuel_results = []
    for avg in means:
        fuel_used = 0
        for crab in crabs:
            if crab > mean:
                fuel_used += get_fuel(crab - avg)
            else:
                fuel_used += get_fuel(avg - crab)
        fuel_results.append(int(fuel_used))

    print(min(fuel_results))


main()
