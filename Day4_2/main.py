import copy

boards = []
with open("D:\AdventOfCode_2021\Day4_2\data.txt") as data:
    calls = data.readline().split(',')
    board = []
    for line in data.readlines():
        line = line.rstrip()
        if line:
            boards.append(line.split())

board_size = 5
boards_split = [boards[x:x+board_size] for x in range(0, len(boards), board_size)]

results_board = copy.deepcopy(boards_split)

winner = -1
winning_val = -1
winners = []
for x in calls:
    for i in range(len(boards_split)):
        for j in range(5):
            for k in range(5):
                if(boards_split[i][j][k] == x) and len(winners) < 100:
                    results_board[i][j][k] = 'X'
                for y in range(5):
                    count = 0
                    if results_board[i][y].count('X') == 5 and boards_split[i] not in winners:
                        winners.append(boards_split[i])
                        winning_val = x
                        winner = i
                    for z in range(5):
                        if results_board[i][z][y] == 'X':
                            count += 1
                        if count == 5 and boards_split[i] not in winners:
                            winners.append(boards_split[i])
                            winning_val = x
                            winner = i

filtered_board = []
for w in range(5):
    filtered_board.append(list(filter(('X').__ne__, results_board[winner][w])))
int_winner = [[int(str) for str in subarray] for subarray in filtered_board]

print("Answer: ",sum(sum(int_winner,[])) * int(winning_val))