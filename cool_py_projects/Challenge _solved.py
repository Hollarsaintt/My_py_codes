main_dic = {}
j = 1

#loop 1: Assign Alpha-num into main_dic 
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    while j < 27:
        main_dic.setdefault(i,j)
        break
    j += 1
import itertools, enchant
Alpha_lst = list(main_dic.keys())

#loop 2: Extract 4 letter words upward and check their int version if add up to 100; displays the words if meaningful
for jj in range(4,27):
    st_Alpha = ''.join(Alpha_lst)
    tupl_lst = list(itertools.combinations(st_Alpha,jj))
    ##sltn_lst = []
    ##for kk in tupl_lst: #change tupl_lst to list of list
        ##sltn_lst.append(list(kk))
    for jk in tupl_lst:
        nt_value = 0
        for jw in jk: #checks if jk items certify the sum 100 condition
            nt_value = nt_value + main_dic[jw]
        if nt_value == 100:
            fnl_wrd = ''.join(jk)
            pm_tupl_lst_fnl_wrd = list(itertools.permutations(fnl_wrd,len(fnl_wrd)))
            for r_st in pm_tupl_lst_fnl_wrd:
                chck_wrd = ''.join(r_st)
                us_ditn = enchant.Dict('en_US')
                if us_ditn.check(chck_wrd) == True: #check if string chck_wrd exist in Real dictionary and prints it if it does
                    print(chck_wrd.title(), end=' ')
        
    


    
