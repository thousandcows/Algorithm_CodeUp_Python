import sys

sys.setrecursionlimit(100000)

stair = [0]
# 1. Read the stairs
n = int(input())

for i in range(n):
    stair.append(int(input()))

# 2. Find the maximum points
memo = [0, stair[1], stair[1] + stair[2], max(stair[1], stair[2]) + stair[3]]

for i in range(4, n+1):
        memo.append(max(stair[i - 1] + memo[i - 3], memo[i - 2]) + stair[i])

print(memo[n])