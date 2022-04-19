import sys
sys.setrecursionlimit(1000000)


def getTotal(n):
    if n == 1:
        return 1

    return n + getTotal(n - 1)


n = int(input())

print(getTotal(n))





