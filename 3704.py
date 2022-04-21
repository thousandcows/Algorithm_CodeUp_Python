n = int(input())

stair = [0, 1, 2, 4]

for i in range(4, n + 1):
    stair.append((stair[i-3] + stair[i-2] + stair[i-1]) % 1000)

print(stair[n])

