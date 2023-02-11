k = 2
a = 1*1*5
for b in range(2, 13):
    for z in range(k,13):
        if (b != 5) and (z != 5) and ((b+z)== 13):
            print(a*b*z)
    k += 1
