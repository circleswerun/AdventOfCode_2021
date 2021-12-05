#complete
data = open("D:\\AdventOfCode_2021\\Day3\\data.txt").read().splitlines()

gamma = ''
epsilon = ''

for x in range(len(data[0])):
    count_1 = 0
    count_0 = 0
    for y in range(len(data)):
        if int(data[y][x]) == 1:
            count_1 += 1
        else:
            count_0 += 1

    if count_1 > count_0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print("gamma " + gamma)
print("epsilon " + epsilon)

print("result: gamma * epsilon in decimal: ", int(gamma,2)*int(epsilon,2))