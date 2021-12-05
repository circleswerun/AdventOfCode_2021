import copy

boards = []
with open("D:\AdventOfCode_2021\Day4\data.txt") as data:
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
for x in calls:
    if winner > -1:
        break
    for i in range(len(boards_split)):
        if winner > -1:
            break
        # print(i)
        for j in range(5):
            if winner > -1:
                break
            for k in range(5):
                if winner > -1:
                    break
                # print(i, j, k)
                if(boards_split[i][j][k] == x):
                    results_board[i][j][k] = 'X'
                for y in range(5):
                    if winner > -1:
                        break
                    count = 0
                    if results_board[i][y].count('X') == 5:
                        print("winner: board #",i)
                        print(results_board[i])
                        winner = i
                        winning_val = x
                        break
                        # exit(1)
                    for z in range(5):
                        if results_board[i][z][y] == 'X':
                            count += 1
                        if count == 5:
                            print("winner: board #",i)
                            print(results_board[i])
                            winner = i
                            winning_val = x
                            break
                            # exit(1)

print(boards_split[winner])

filtered_board = []
for w in range(5):
    filtered_board.append(list(filter(('X').__ne__, results_board[winner][w])))

int_winner = [[int(str) for str in subarray] for subarray in filtered_board]

print("Answer: ",sum(sum(int_winner,[])) * int(winning_val))