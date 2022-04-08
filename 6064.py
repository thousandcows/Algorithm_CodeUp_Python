a,b,c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)

print(a if (a < (b if (b < c) else c) ) else (b if (b < c) else c))