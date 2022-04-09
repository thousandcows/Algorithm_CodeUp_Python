n = int(input())

board = [[0 for i in range(20)]for j in range(20)]

for i in range(n):
    row, col = map(int,input().split())
    board[row][col] = 1


for i in range(1,20):
    for j in range(1,20):
        print(board[i][j], end=' ')
    print()