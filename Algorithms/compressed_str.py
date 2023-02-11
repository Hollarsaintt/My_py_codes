input_str = 'Thank you so much lord jesus we thank you bbbbaba ooo eseeeeeeee eeesessithhskkskk'

com_str = ''
count = 0
temp_str = ''
for char in input_str:
    if count == 0:
        temp_str += char
        count += 1
    elif count > 0:
        if temp_str[0] == char:
            temp_str = temp_str  + char
            count += 1
        else:
            if len(temp_str) > 1:
                com_str = com_str + (temp_str[0]+str(count))
                temp_str  = char
                count = 1
            else:
                com_str += temp_str
                temp_str  = char
                count = 1
else:
    if len(temp_str) > 1:
        com_str = com_str + (temp_str[0]+str(count))
                
    else:
        com_str += temp_str
                
    
print(com_str)
    