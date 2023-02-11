'''Consequtive nums - perfect square'''
import math


def Cons_num_sq(ninja_b):
    
    ck_num = 1
    it_ials = [0]
    jy_jy = []


    while ck_num < (int(ninja_b+1)):
       pt_var = ck_num + it_ials[0]
       
       if (math.sqrt(pt_var)//1 == math.sqrt(pt_var)):
           jy_jy.append(str(ck_num)+' , ')
           
           
           if ck_num != 0:
               it_ials[0] = ck_num
       ck_num+=1


    for pnt in jy_jy:
        if pnt != jy_jy[-1]:
            print(pnt, end= '')
            continue
        print(str(pnt.replace(',','')))
        
Cons_num_sq(int(input('Enter a num in Domain{Z+}!: ')))
        
   
    
    
    
    
    
    
    
