num = int(input())
sum = 0
for i in range(1, num + 1):
    sum = sum + i
    if sum >= num:
        print(sum)
        break