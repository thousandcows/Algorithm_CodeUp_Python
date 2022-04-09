# 바둑판 초기화
board = []

for i in range(19):
    board.append([])
    for j in range(19):
        board[i].append(0)

for i in range(19):
        board[i] = list(map(int, input().split()))

# 뒤집는 횟수
n = int(input())

for i in range(n):

    # 좌표 입력받기
    x, y = map(int, input().split())

    # 뒤집기
    # row => col
    for j in range(19):

        if board[x-1][j] == 0:
            board[x-1][j] = 1
        else:
            board[x-1][j] = 0

        if board[j][y-1] == 0:
            board[j][y-1] = 1
        else:
            board[j][y-1] = 0

# 결과 출력
for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ')
    print()
