sum = 0

n = int(input())

for i in range(n + 1):

    sum = sum + i

    if sum >= n:
        print(i)
        break