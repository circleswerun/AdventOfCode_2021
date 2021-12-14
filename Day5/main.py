#Pretty much entirely copied from https://github.com/KevinL10/advent-of-code-2021/blob/main/day5/part1.py
#Initially overcomplicated this problem by creating a flat array of all coordinates for every line
#Then checked for # of duplicate entries.

with open("D:\AdventOfCode_2021\Day5\data.txt") as data:
    lines = data.read().splitlines()

size = 1000
overlaps = [[0] * size for i in range(size)]
for line in lines:
    first, second = line.split(' -> ')
    x1, y1 = list(map(int, first.split(',')))
    x2, y2 = list(map(int, second.split(',')))

    #if verticle line:
    if x1 == x2:
        #if line is going down - reverse
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            overlaps[x1][y] += 1
    #if horizontal line
    elif y1 == y2:
        #if line goes from right to left - reverse
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            overlaps[x][y1] += 1

result = 0
for i in range(size):
    for j in range(size):
        if overlaps[i][j] > 1:
            result += 1

print(result)

