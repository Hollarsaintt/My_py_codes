theBoard = {'t.l':' ', 't.m':' ', 't.r':' ',  ##Data structures of tictactoeBoard
            'm.l':' ', 'm.m':' ', 'm.r':' ',
            'b.l':' ', 'b.m':' ', 'b.r':' '}

guideBoard = {'t.l':'t.l', 't.m':'t.m', 't.r':'t.r',  ##Serves as a guide for the players to enter their move
              'm.l':'m.l', 'm.m':'m.m', 'm.r':'m.r',
              'b.l':'b.l', 'b.m':'b.m', 'b.r':'b.r'}
count = {}

def printboard(board):  ##Works with the structure to model the tictactoe board 
    print(board['t.l'] + '|' + board['t.m'] + '|' + board['t.r'])
    if board == theBoard:
        print('-+-+-')
    else:
       print('---+---+---') 
    print(board['m.l'] + '|' + board['m.m'] + '|' + board['m.r'])
    if board == theBoard:
        print('-+-+-')
    else:
       print('---+---+---') 
    print(board['b.l'] + '|' + board['b.m'] + '|' + board['b.r'])
    
def swap():  ##swap turns
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

def printWinsAndCount():
    global turn
    print(turn + ' wins')
    print('')
    count[turn] = count[turn] + 1
    swap()
def exit():
    H = True
    while H:
        ex_it = input('\nwould you like to exit the Game(Y/N): ')
        print()
        if (ex_it == ('Y')) or (ex_it == ('y')):
            global play
            play = False
            print('Exiting...\n\nGame Ended')
            H = False
            
        elif (ex_it == ('N')) or (ex_it == ('n')):
            break
        else:
            print('\n\nEnter the correct option!')
    
                
                

##Allows players to enter their moves
turn = 'X'
play = True
while play:
    theBoard = {'t.l':' ', 't.m':' ', 't.r':' ',  
                'm.l':' ', 'm.m':' ', 'm.r':' ',
                'b.l':' ', 'b.m':' ', 'b.r':' '}
    try:
        i = 0
        san_count = {}
        k = True
        while (i < 9):  ## one Round
            printboard(theBoard)
            print('')
            print('it is the turn of {t}\n\n'.format(t=turn))
            G = True
            while G:
                guide = input('\nDo you want a Guideboard?(Y/N): ')
                if (guide == ('y')) or (guide == ('Y')):
                    printboard(guideBoard)
                    print('\nuse the above chart as a guide\
just type the characters in the desired space\n')
                    G = False
                elif (guide == ('n')) or (guide == ('N')):
                    break
                else:
                    print('\nEnter the correct option!\n')    
            move = input('Type your move: ')
            print()
            cheese = theBoard[move] ##only check for Key Error
            
            if theBoard[move] != 'X' and theBoard[move] != 'O':
                theBoard[move] = turn
                count.setdefault(turn, 0)
            
                
            else:  ##Handles a player who tries to write on Non empty space
                print('\nSpace Not vacant!, try locating empty spaces!\n')
                san_count.setdefault(turn, 0)
                san_count[turn] += 1
                if san_count[turn] == 3:
                    swap()
                    printWinsAndCount()
                    break
                else:
                    continue
                
            i += 1
            
                                    
              ##winning conditions
            if (theBoard['t.l'] == turn and theBoard['t.m'] == turn and theBoard['t.r'] == turn):
                printWinsAndCount()
                break
            elif (theBoard['m.l'] == turn and theBoard['m.m'] == turn and theBoard['m.r'] == turn):
                printWinsAndCount()
                break
            elif (theBoard['b.l'] == turn and theBoard['b.m'] == turn and theBoard['b.r'] == turn):
                printWinsAndCount()
                break
            elif (theBoard['t.l'] == turn and theBoard['m.l'] == turn and theBoard['b.l'] == turn):
                printWinsAndCount()
                break
            elif (theBoard['t.m'] == turn and theBoard['m.m'] == turn and theBoard['b.m'] == turn):
                printWinsAndCount()
                break
            elif (theBoard['t.r'] == turn and theBoard['m.r'] == turn and theBoard['b.r'] == turn):
                printWinsAndCount()
                break
            elif (theBoard['t.l'] == turn and theBoard['m.m'] == turn and theBoard['b.r'] == turn):
                printWinsAndCount()
                break
            elif (theBoard['t.r'] == turn and theBoard['m.m'] == turn and theBoard['b.l'] == turn):
                printWinsAndCount()
                break
            else:
                if i == 9:
                    print('\nNo winner!\n')
                    
            swap() 
        printboard(theBoard)
        print('')
        print(count)
        print('')
        exit()

        ##Handles Error: Intentional and Non intentional
    except KeyError:
        print("Error!, You Entered an invalid space character.")
        print('\nRequest for a guide to know the correct moves command!\n')
        if i >= 3:    ##conditions for intentionally making an Error so that the opponent won't win 
            swap()
            print(turn + ' wins')
            print('')
            count[turn] = count[turn] + 1
            print(count)
            print('')
            exit()
        


    

