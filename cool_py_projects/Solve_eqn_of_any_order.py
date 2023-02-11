#Fun Project: Solve linear simultaneous equations involving several unknowns
#Programmer: Demokun Boluwatife Olayiwola
#Date: oct 2020 to Nov 2020


main_lp_ctrl = True
while main_lp_ctrl:
    def exit(): #A function that ask the user if to exit or not.
            global main_lp_ctrl
            exit_ctrl = True
            while exit_ctrl:
                ctrl_main = input('\nHave more to solve?(Y) or (N): ')
                if ctrl_main.lower() == 'n':
                    exit_ctrl = False
                    main_lp_ctrl = False #exit the program successfully
                elif ctrl_main.lower() == 'y':
                    exit_ctrl = False
                    
    try:
        print('Welcome!')
        Unknown_Num = int(input('What the number of unknown?: '))
        Main_lst = []
        Eql_lst = []
        C_Num = (Unknown_Num**2) + Unknown_Num
        C_lst = []
        for i in range(1,(C_Num+1)):
            C_lst.append('c'+str(i)) #Makes C_lst contains total number of coefficient to be inserted into main list from user input
        keep_trck = []

        k = 0
        def insert_C(R_arg, typ): #Inserts the coefficient appropriately when call
            R_arg.append(typ(input('Insert {c1}: '.format(c1=C_lst[0]))))
            C_lst.remove(C_lst[0])
            if R_arg == Main_lst[k]:
                keep_trck.append('a')



        for i in range(0,Unknown_Num): ##Creates the required number of list into the Main list
            Main_lst.append(list())


        #A loop that insert coefficient of unknowns in order based on user input
        print('Type in the coefficients in order.')
        for k in range(0,Unknown_Num): ##Creates the required number of list into the Main list
            insert_C(Main_lst[k],int)
            w = True

        #len(Main_lst) now == Unknown_Num
        #Loop that separates coefficient into main list and eql list
        k = 0
        for j in range(0,len(C_lst)):
            if (int(len(keep_trck)/Unknown_Num) == float(len(keep_trck)/Unknown_Num)) and (w == True):
                insert_C(Eql_lst,int)
                w = False
            else:
                w = True
                insert_C(Main_lst[k],int)
                k += 1
                if k == (Unknown_Num):
                    k = 0


        ##Achievement 1:- Main_lst and Eql_lst in correct order of coefficient and having all elements as integers 
                                      
        Unmanip_Mains = Main_lst.copy()   #unmanip_Mains stores the initial user input 
                                            #will be used for solving other determinants of unknown

        
        #program that calculate determinant of any order
        def basket_weave_solver(butterfly_mat): #2*2 Det solver
            butterfly_solved = ((butterfly_mat[0][0] * butterfly_mat[1][1]) - (butterfly_mat[0][1] * butterfly_mat[1][0]))
            return butterfly_solved

        # n*n det_reducer; n - is the order
        c = 1
        end_multiplier = 1
        def det_reducer(mat_ag): # reduced the arg passed to (n-1)if n > 2
            global c
            global end_multiplier
            n = len(mat_ag)
            #solve for n > 2
            lap_ctrl = True 
            j1 = 1
            #end_multiplier = 1 #used to control effect of row exchange in determinants
            while lap_ctrl:   #loop that checks for first row first item that are zero and do some row exchange if any
                if mat_ag[0][0] != 0:
                    c =  (c * (1/((mat_ag[0][0])** (n-2)))) #c - chio's multiplier
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
                
             
            jina = True
            while jina:
                      #A loop that forms 2 * 2 from the n * n mat_ag
                ini_lst[0][0] = mat_ag[CTRL3][CTRL3]
                ini_lst[1][0] = mat_ag[ctrl4][CTRL3] #CTRL3 is constant
                ini_lst[0][1] = mat_ag[CTRL3][ctrl2] #ctrl4 controls rows and ctrl2 controls column
                ini_lst[1][1] = mat_ag[ctrl4][ctrl2] #ctrl2 changes by 1 always
                ctrl2 += 1
                red_mat[ctrl1].append((basket_weave_solver(ini_lst)))
                if len(red_mat[ctrl1]) != (n-1):
                    continue
                else:
                    ctrl4 += 1
                    ctrl1 += 1 #ctrl1 controls distribution to red_mat
                    ctrl2 = 1
                if len(red_mat[-1]) == (n-1):
                    jina = False

            return red_mat #The passed matrix has been reduced and c(chio's multiplier) is kept, the end_multiplier is also important

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
                    lp2_ctrl = False #Read below comment for usage of the det_solver function to evaluate to Real det
        ##Mission1 accomplished
        #usage:- det_solver() #passed a argument
        #Real_det = (c * end_multiplier * pseudo_det_holder)

        #Next-Mission :- A loop that slices main_list and passed it to det_solver and returns the solution as variables(B)


        #Solution loop
        soln_lst = []
        
        Solved_det_lst = []


        det_solver(Main_lst)
        Real1_det = (c * end_multiplier * pseudo_det_holder) #The Main_lst first det
        if Real1_det == 0:
            1/0 #Causes an Error
        c, end_multiplier = 1, 1 #change back to initials for new determinant calculation
        Main_lst = Unmanip_Mains.copy() #Returns back to original if at all there has been row exchange.


        for ctrl8 in range(len(Main_lst)):
            Main_lst = Unmanip_Mains.copy() #Returns back to original if at all there has been row exchange.
            Main_lst[ctrl8] = Eql_lst
            det_solver(Main_lst)
            Real2_det = (c * end_multiplier * pseudo_det_holder)
            Solved_det_lst.append(Real2_det)
            c, end_multiplier = 1, 1

        for ctrl9 in Solved_det_lst:
            soln_lst.append((ctrl9 / Real1_det)) #At the end of the loop the solutions to the equations are complete in the solution list

        a11 = 1
        print('\n')
        for sol in soln_lst:
            print('B{} = {}'.format(a11, sol))
            a11 += 1
        exit()
        
                    
                
                

    except: #This brings out error for equations that doesn't have a unique solutions
        print('\nMATH ERROR!')
        exit()

        
        



            
            
    



    













