#1. Input data
h, w = map(int, input().split())

#2. Use multiple dimetional list to create board
board = [[0 for i in range(w)] for j in range(h)]

#3. Place sticks on the board
n = int(input())

for i in range(n):

    l, d, x, y = map(int, input().split())

    if d == 0:
        for i in range(y, y + l):
            board[x - 1][i - 1] = 1
    else:
        for i in range(x, x + l):
            board[i - 1][y - 1] = 1

#4. Print the result
for i in range(h):
    for j in range(w):
        print(board[i][j], end=" ")
    print()

