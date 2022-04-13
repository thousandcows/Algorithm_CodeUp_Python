# 1. Read the board of 10 * 10
board = []

for i in range(10):
    board.append(list(map(int, input().split())))



# 2. Find the fastest route for the ant
# Starting point
x = 1
y = 1

while True:
    # Mark the route
    if board[x][y] == 0:
        board[x][y] = 9
    elif board[x][y] == 2:
        board[x][y] = 9
        break

    # Break condition: no route or reach the bottom right edge of the board
    if (board[x][y + 1] == 1 and board[x + 1][y] == 1) or (x == 9 and y == 9):
        break

    # Find the path
    if board[x][y+1] != 1:
        y += 1
    elif board[x + 1][y] != 1:
        x += 1

# 3. Print the result
for i in range(10):
    for j in range(10):
        print(board[i][j], end = " ")
    print()