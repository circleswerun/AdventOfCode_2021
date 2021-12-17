#crab submarines can only move horizontally: data is the x position for each crab
#make all horizontal positions match with as few moves as possible
import statistics

with open("data.txt") as data:
    crabs = list(map(int,data.readline().split(',')))
print(crabs)

max_x = crabs[0]
min_x = crabs[0]
for crab in crabs:
    if crab < min_x:
        min_x = crab
    if crab > max_x:
        max_x = crab

median = int(statistics.median(crabs))

fuel_used = 0
for crab in crabs:
    if crab > median:
        fuel_used += crab - median
    else:
        fuel_used += median - crab

print(fuel_used)