#program that calculate determinant of any order
def basket_weave_solver(butterfly_mat): #2*2 Det solver
    butterfly_solved = ((butterfly_mat[0][0] * butterfly_mat[1][1]) - (butterfly_mat[0][1] * butterfly_mat[1][0]))
    return butterfly_solved

# n*n det_reducer; n - is the order
k = 1
end_multiplier = 1
def det_reducer(mat_ag): # reduced the arg passed to (n-1)if n > 2
    global k
    global end_multiplier
    n = len(mat_ag)
    #solve for n > 2
    lap_ctrl = True 
    j1 = 1
    #end_multiplier = 1 #used to control effect of row exchange in determinants
    while lap_ctrl:   #loop that checks for first row first item that are zero and do some row exchange if any
        if mat_ag[0][0] != 0:
            k =  (k * (1/((mat_ag[0][0])** (n-2)))) #k - chio's multiplier
            lap_ctrl = False
        else:
            mat_ag[0], mat_ag[j1] = mat_ag[j1], mat_ag[0]
            j1 += 1
            end_multiplier = (end_multiplier * (-1)) #counterbalance effect of row exchange
            
    
    
    ctrl1,ctrl2, CTRL3, ctrl4 = 0, 1, 0, 1 #used to control the distribution into ini_lst
    ini_lst = [[0,0], #initial basket_weave list
               [0,0]]
    red_mat = []     #the new reduced matrix at start
    for xin in range(n-1):
        red_mat.append(list()) #creates a (n-1) empty list of list 
        
     
    j = True
    while j:
              #A loop that forms 2 * 2 from the n * n mat_ag
        ini_lst[0][0] = mat_ag[CTRL3][CTRL3]
        ini_lst[1][0] = mat_ag[ctrl4][CTRL3] #CTRL3 is constant
        ini_lst[0][1] = mat_ag[CTRL3][ctrl2] #ctrl1 controls rows and ctrl2 controls column
        ini_lst[1][1] = mat_ag[ctrl4][ctrl2] #ctrl4 changes by 1 always
        ctrl2 += 1
        red_mat[ctrl1].append((basket_weave_solver(ini_lst)))
        if len(red_mat[ctrl1]) != (n-1):
            continue
        else:
            ctrl4 += 1
            ctrl1 += 1
            ctrl2 = 1
        if len(red_mat[-1]) == (n-1):
            j = False

    return red_mat #The passed matrix has been reduced and k(chio's multiplier) is kept, the end_multiplier is also important

# n*n det_solver; n - is the order
#return a single value determinant

pseudo_det_holder = 0 #holds the determinant solved.
def det_solver(mat_det): #n2 is the order of mat_det
    global pseudo_det_holder
    lp2_ctrl = True
    while lp2_ctrl:
        n2 = len(mat_det)
        if (n2 > 2):
           mat_det = det_reducer(mat_det)
        else:
            pseudo_det_holder = basket_weave_solver(mat_det)
            lp2_ctrl = False

##Mission accomplished
det_solver() #passed a argument
solved_det = (k * end_multiplier * pseudo_det_holder)


        
        
