def triangle(n):

    if n == 1:
        print("*")
        return
    else:
        triangle(n - 1)

    print("*" * n)

triangle(int(input()))
