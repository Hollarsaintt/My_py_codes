print('Type any digit')
print('And i will list odds numbers in between the digit')
i = input()
for i in range(1, int(i)):
    if i%2 != 0:
        print(i)
