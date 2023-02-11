#implementation of insertion sort algorithm
from random import randint
a = [randint(1, (10**6)) for _ in range(10**6)]
print(a)
'''for j in range(1, len(a)):
    i = j - 1
    while a[i] > a[i+1]:
        a[i], a[i+1] = a[i+1], a[i]
        if i != 0:
            i -= 1
print(a)'''
