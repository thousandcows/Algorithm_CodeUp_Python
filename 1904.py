def recurOdd(start, end):
    if start > end:
        return

    if end % 2 == 1:
        recurOdd(start, end - 2)

        print(end, end=" ")
    else:
        recurOdd(start, end - 1)


start, end = map(int, input().split())

recurOdd(start, end)