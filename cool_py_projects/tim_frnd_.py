n = 1
loop_ctrl = True

while loop_ctrl:
    if (n % 8 == 1) and (n % 15 == 1) and (n % 20 == 1) and (n % 9 == 4) and (n % 13 == 4):
        print(n)
        loop_ctrl = False
    
    
    n += 1

