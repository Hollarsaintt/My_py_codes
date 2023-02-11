#can check the number of zero in a row of list of list without a row having all zero.
Main_lst = [] ##User should type in the list of list here
def Main_lst_chck(Main_lst):
    zero_counter = []
    zero0_len = []
    global Main_lst
    for z in range(len(Main_lst)): #z locate a row, [z][d] locates element in the row
               for d in range(len(Main_lst[z])):
                     if Main_lst[z][d] == 0:
                            zero_counter.append('a')
               if len(zero_counter) != len(Main_lst[0]):
                 zero0_len.append(len(zero_counter))
               else:
                 5/0 #Makes every mathematical invalid user input Error.
               zero_counter = []
    return zero0_len
               
#check for the row with the Highest Num of zero and rearrange main_lst

zero_len = Main_lst_chck(Main_lst)
zero_len_copy = zero_len.copy()

def chck_if_elmnt_is_same(): #check if there is tie in the number of zeros had in rows
    jip = 0                      #if all element in the zero_len_copy is same it returns 0 else return 1
    s_it = zero_len_copy[0]
    for zep in zero_len_copy:
        if zep != s_it:
            jip = 1
        else:
            s_it = zep
    return jip
    

for rw_number in range(len(zero_len)): #sub loop that rearrange in order of decreasing zero len
    find_Hhst = 0
    for i in zero_len_copy:
        if i > find_Hhst:
            find_Hhst = i
    if find_Hhst != 0 and (chck_if_elmnt_is_same() != 0):
        Main_lst[rw_number], Main_lst[zero_len.index(find_Hhst)] = Main_lst[zero_len.index(find_Hhst)], Main_lst[rw_number]
        zero_len_copy.remove(zero_len_copy[zero_len_copy.index(find_Hhst)])
        zero_len[zero_len.index(find_Hhst)] = 'a'
        
#Achievement 3:- Main_lst now having arranged rows in accordance with number of zeros
print(Main_lst)
