num = int(input())
for i in range(1, num + 1):
    test = i % 10
    x = [3, 6, 9]
    if test in x:
        print("X", end = ' ')
    else:
        print(i, end = ' ')
