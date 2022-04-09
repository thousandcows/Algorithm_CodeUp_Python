n = int(input())
numbers = list(map(int, input().split()))

fastest = numbers[0]

for i in numbers:
    if i < fastest:
        fastest = i

print(fastest)