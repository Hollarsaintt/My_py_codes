#input = (x, y), target - willl be given
#moves - (x+y, y) or (x, x+y)
#output = 'Yes' or 'No'

#initial(x1, y1)  targe(x2, y2)

#code doesn't work write it again.
def canReach(x1, y1, x2, y2):
    for m in range(0, (y2//x1)+1):
        if y1+ (m*x1) == y2:
            for n in range(0, (x2//y1)+1):
                if x1 + (n*y1) == x2:
                    return 'YES'
                   
            else:
                return 'NO'
        elif m == (y2//x1):
            return 'NO'

print(canReach(2,2,6,7))
    