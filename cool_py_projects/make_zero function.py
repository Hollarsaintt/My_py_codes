
def Make_zero(jun_arg,i,j):
    if jun_arg[i][j] != 0:         #will make jun_arg[i][j] zero
        if jun_arg[i+1][j] != 0:
            rw_multiplier = (jun_arg[i][j]) / (jun_arg[i+1][j])
            for zindi1 in jun_arg[i+1]:
                y1 = 0
                jun_arg[i+1][y1] = (zindi1 * rw_multiplier)
                y1 += 1    #@ d end of the loop row i+1 has been multiplied with the multiplier

            for zindi2 in jun_arg[i]:
                y2 = 0
                jun_arg[i][y2] = zindi2 - jun_arg[i+1][y2]
                y2 += 1   #@ d end of the loop row i element j is sucessfully changed to zero.
                
