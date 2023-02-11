l = 2
for i in range(6):
    print('\n')
    for j in range(l):
        if j == 0 or j == l-1:
            print('#', end='')
        else:
            print(' ',end='')
    l+=1
