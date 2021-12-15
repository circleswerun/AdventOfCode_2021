with open("data.txt") as file:
    init_fish = list(map(int, file.readline().split(',')))

print(init_fish)
days = 80

for x in range(days):
    for y in range(len(init_fish)):
        if init_fish[y] > 0:
            init_fish[y] -= 1
        else:
            init_fish[y] = 6
            init_fish.append(8)

print(len(init_fish))
