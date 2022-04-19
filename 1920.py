import sys
sys.setrecursionlimit(1000000)

def toBinary(n):

    if n == 0:
        return "0"
    if n == 1:
        return "1"

    if n % 2 != 0:
        return toBinary(int(n / 2)) + "1"
    else:
        return toBinary(int(n / 2)) + "0"

print(toBinary(int(input())))

print(3 / 2)