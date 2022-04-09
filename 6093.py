n = int(input())

numbers = input().split(' ')

list = []

# list 초기화
for i in range(n):
    list.append(numbers[i])

for i in range(n-1, -1, -1):
    print(list[i], end = " ")