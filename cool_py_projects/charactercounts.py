

counts = {}
j = 0
name = input('Type anything and i will count number of its characters: ')
for i in name:
    counts.setdefault(i,j)
    counts[i] = counts[i] + 1
print(counts)
input()
