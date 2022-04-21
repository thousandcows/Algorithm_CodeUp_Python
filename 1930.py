# Memoization
dp = [[0 for i in range(15)] for j in range(15)]
for i in range(15):
    dp[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

# function SuperSum
def SuperSum(k, n):
    # k == n
    if k == 0:
        return n

    return dp[k][n]

# Read k, n
while True:

    # Read input
    line = input()

    # EOF : break
    if line == "EOF":
        break

    # Parse input as k, n
    k, n = map(int, line.split())

    # Print SuperSum result
    print(SuperSum(k, n))
