
def Collatz(n):

    print(int(n))

    if n == 1:
        return

    if n % 2 != 0:
        return Collatz(3 * n + 1)
    else:
        return Collatz(n / 2)

Collatz(int(input()))
