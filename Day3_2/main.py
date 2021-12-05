#complete
data = open("D:\\AdventOfCode_2021\\Day3\\data.txt").read().splitlines()

oxygen = data.copy()
co2 = data.copy()


for x in range(len(oxygen[0])):
    count_1 = 0
    count_0 = 0
    store_0 = []
    store_1 = []
    for y in range(len(oxygen)):
        if len(oxygen) == 1:
            break
        if oxygen[y][x] == '1':
            count_1 += 1
            store_1.append(oxygen[y])
        else:
            count_0 += 1
            store_0.append(oxygen[y])

    if count_1 < count_0:
        for z in store_0:
            oxygen.remove(z)
    else:
        for z in store_1:
            oxygen.remove(z)


for x in range(len(co2[0])):
    count_1 = 0
    count_0 = 0
    store_0 = []
    store_1 = []

    for y in range(len(co2)):
        if len(co2) == 1:
            break
        if co2[y][x] == '1':
            count_1 += 1
            store_1.append(co2[y])
        else:
            count_0 += 1
            store_0.append(co2[y])

    if count_1 < count_0:
        for z in store_1:
            co2.remove(z)
    else:
        for z in store_0:
            co2.remove(z)
print("oxygen: " + oxygen[0])
print("co2: " + co2[0])

print("result: oxygen * co2 in decimal: ", int(oxygen[0],2)*int(co2[0],2))