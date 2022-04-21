import sys
sys.setrecursionlimit(100000)

def recursion(n, memoization):
    if n == 1:
        memoization[1] = 1
        return memoization[1]
    if n == 2:
        memoization[2] = 2
        return memoization[2]
    if n == 3:
        memoization[3] = 4
        return memoization[3]

    if memoization[n]:
        return memoization[n]
    else:
        memoization[n] = (recursion(n - 1, memoization) + recursion(n - 2, memoization) + recursion(n - 3, memoization)) % 1000
        return memoization[n]



n = int(input())

memoization = [0 for _ in range(n+1)]

print(recursion(n, memoization))



# n = int(input())
#
# stair = [0, 1, 2, 4]
#
# for i in range(4, n + 1):
#     stair.append((stair[i-3] + stair[i-2] + stair[i-1]) % 1000)
#
# print(stair[n])
#
