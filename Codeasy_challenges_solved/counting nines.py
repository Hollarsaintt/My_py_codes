num_lst = []
for i in range(1, 101):
    num_lst.append(str(i))
num_str = ''.join(num_lst)

print(num_str.count('9'))
