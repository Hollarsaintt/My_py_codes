counter = 0
m = 1
for k in range(1, 1000):
    for z in range(m, 1000):
        if (k+z) == 1000:
            counter += 1
    m += 1
print(counter)
