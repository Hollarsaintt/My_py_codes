##Takes the list of lists items and transpose \
##changes all horizontal items to vertical 
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for y in range(len(grid[0])): ## Variable y locate items in the inner list 
   for x in range(len(grid)): ##Variable x locate items in the list of list 
      print(grid[x][y], end='')
   if x == (len(grid)-1):
      print('')##condition for a new line printing 
       
               
               
        
