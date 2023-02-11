##To return the string concatenation \
##of items of list passed into dummy function
spam = ['apples', 'bananas', 'tofu', 'cats']
def dummy(mumu):
    d = ''
    for i in range(len(mumu)):
        if i != (len(mumu)-1):
            s = mumu[i] + ', '
        else:
            s = mumu[i]
        d = d + s
    return d


dummy(spam)
        
            
                
           
