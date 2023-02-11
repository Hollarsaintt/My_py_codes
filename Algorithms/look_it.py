#input = (x, y), target - willl be given
#moves - (x+y, y) or (x, x+y)
#output = 'Yes' or 'No'

#initial(x1, y1)  targe(x2, y2)
def canReach(x1, y1, x2, y2):
    y = True
    for m in range(1, (y2//x1)+1):
        if y1+ (m*x1) == y2:
            for n in range(1, (x2//y1)+1):
                if x1 + (n*y1) == x2:
                    return 'YES'
                   
            if m == (y2//x1) and y == True:
                y = False
                return 'NO'
        elif m == (y2//x1) and y == True:
            y = False
            return 'NO'

print(canReach(1,4,5,9))
    