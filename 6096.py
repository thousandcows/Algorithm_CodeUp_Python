# 바둑판 초기화
board = []

for i in range(20):
    board.append([])
    for j in range(20):
        board[i].append(0)

for i in range(19):
    numbers = list(map(int, input().split()))
    for j in range(19):
        board[i + 1][j + 1] = numbers[j]

# 뒤집는 횟수
n = int(input())

for i in range(n):

    # 좌표 입력받기
    row, col = map(int, input().split())
    # 뒤집기
    # row => col
    for j in range(1, 20):

        row_stone = board[row][j]
        col_stone = board[j][col]

        if row_stone == 0:
            row_stone = 1
        else:
            row_stone = 0

        if col_stone == 0:
            col_stone = 1
        else:
            col_stone = 0

# 결과 출력
for i in range(1, 20):
    for j in range(1, 20):
        print(board[i][j], end=' ')
    print()
