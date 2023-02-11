print ('Hi,enter a name')
name = input()
while name:
    print ('Thanks for entering a name')
    print ('The length of your name is ' + str(len(name)))
    print ('Hi, enter a name')
    name = input()
    
else:
    print ('you did not enter a name')
    print ('kindly enter a name to count its  length')

