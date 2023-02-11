i = [] #loop invariant - Holding the indices of values at all instants of time.
k = 0

a = [2,3,4,5,6,7,4,18,19,20,4,6,7,8,4,12,18,22]
v = 4
for j in a:
    if j == v:
      i.append(a.index(j, start=k)
    k += 1
if len(i) == 0:
    i = None
print(i)

