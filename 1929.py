
def Collatz(n):

    if n == 1:
        print(1)
        return

    if n % 2 != 0:
        Collatz(3 * n + 1)
    else:
        Collatz(n / 2)

    print(int(n))

Collatz(int(input()))
