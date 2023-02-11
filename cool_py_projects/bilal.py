import math
p_sq = []
n_p_sq = []
def sch_man(l_st):
    for i in l_st:
        if int(math.sqrt(i)) == float(math.sqrt(i)):
            p_sq.append(i)
        else:
            n_p_sq.append(i)
    print(p_sq, n_p_sq)
sch_man([9,25,4,5,6,7,8,49])
        
        
        
        
