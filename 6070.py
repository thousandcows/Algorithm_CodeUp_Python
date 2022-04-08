month = int(input())
season = month // 3;
if season == 0 or season == 4:
    print('winter')
elif season == 1:
    print('spring')
elif season == 2:
    print('summer')
else:
    print('fall')