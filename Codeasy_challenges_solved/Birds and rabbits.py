r_l, B_L = 2, 2 #initialize the legs of both animal into defaults
m = 1              #where bird leg(B_L) is constant and known, Rabbit leg(r_l) is changeable cos it not known.

lap_ctrl = True
while lap_ctrl:
    j, b, r = 38, 0, 0
    loop_ctrl = True
    while loop_ctrl:
        for i in range(m):
            if j >= B_L:
                j -= 2
                b += 1
            if j < B_L:
                break

        if j > r_l:
            j -= r_l
            r += 1

        if j < B_L:
            loop_ctrl = False
    if (b+r) == 16 and j == 0: #display the bird num(b) and rabbit leg(r_l) that satisfy the question condition.
        print(b)
        print(r_l)
        lap_ctrl = False
    else:
        m += 1
        if m == 19:
            m = 1
            r_l += 1
                
    
        
        
        
    
    
    
    
