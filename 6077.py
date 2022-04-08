number = int(input())

sum = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        sum += i

print(sum)