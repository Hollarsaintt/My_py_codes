total_squares = 0
chess_board = []
t_counter = 0
for i in range(8):
    chess_board.append(list('aaaaaaaa'))

m = 1
ctrl = True
while ctrl:
    for counter in range(0, len(chess_board[0]), m):
        t_counter += 1
    total_square += (t_counter * t_counter)
    m += 1

    if m == 9:
        ctrl = False
        
print(total_squares)
    
