n = int(input())

def findBefore(n):
    if n != 1:
        findBefore(n - 1)
    print(n)

findBefore(n)
