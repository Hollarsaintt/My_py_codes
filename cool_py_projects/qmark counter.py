chck_str = input('Kindly type!: ')
ctr_str = list(chck_str)
mrk_lst = []

for i in ctr_str:
    if i == '?':
        mrk_lst.append(ctr_str.pop(ctr_str.index(i)))
print(mrk_lst)
if len(mrk_lst) >= 3:
    print('True')
else:
    print('False')

