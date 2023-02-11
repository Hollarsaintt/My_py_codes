#binary addition.
#def arr a and arr b
from random import randint
a = [randint(0,1) for _ in range(10**9)]
b = [randint(0,1) for _ in range(10**9)]
print(len(a))
r = 0
C = []
k, j = -1, 0
while j < len(a):
    if a[k] == 0 and b[k] == 0:
        if r == 0:
            C.append(0)
        else:
            C.append(1)
            r = 0
    elif a[k] == 0 and b[k] == 1:
        if r == 0:
            C.append(1)
        else:
            C.append(0)
            r = 1
    elif a[k] == 1 and b[k] == 0:
        if r == 0:
            C.append(1)
        else:
            C.append(0)
            r = 1
    else:
        if r == 0:
            r = 1
            C.append(0)
        else:
            C.append(1)
            r = 1
    k -= 1
    j += 1
else:
    if r == 1:
        C.append(r)
    else:
        C.append(0)
C = C[::-1]
print(C)
print(len(C))
