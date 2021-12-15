import copy

with open("data.txt") as file:
    init_fish = list(map(int, file.readline().split(',')))

days = 256

all_fish = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]
fish_update = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]

for fish in init_fish:
    all_fish[fish][1] += 1

print(all_fish)
for x in range(days):
    num_new_fish = all_fish[0][1]
    all_fish[0][1] = 0
    all_fish[7][1] += num_new_fish
    all_fish[9][1] += num_new_fish

    fish_update = copy.deepcopy(all_fish)
    for y in range(len(all_fish)-1):
        all_fish[y][1] = fish_update[y+1][1]
    all_fish[9][1] = 0
    print("day ", x + 1, all_fish)

result = 0
for x in range(len(all_fish)):
    result += all_fish[x][1]

print(result)
