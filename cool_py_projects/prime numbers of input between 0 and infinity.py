print('Type any digit between 0 and infinity')
print('And i will list prime numbers in between the digit')
i = input()
if int(i) > 1 and int(i) != 2:
    print(2, end=' ')
else:
    print('No prime number in between your input')
if int(i) > 2 and int(i) != 3:
    print(3, end=' ')
if int(i) > 3 and int(i) != 4 and int(i) != 5:
   print(5,end=' ') 
for i in range(6, int(i)):
    if i % 2 != 0:
        for k in range(3,int(i),2):
            if i/k == int(i/k):
                break
            elif k == int(i-2):
                print(i, end=' ')

        
    
        
         

