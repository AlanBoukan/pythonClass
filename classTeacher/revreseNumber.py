# Revrese big number
def revNumber():
    #the below structure will save the number in list
    a=(input("please insert a big number to find the revrese"))
    #The below variable is for saving number
    rev_a=0
    for i in range(len(a)-1,-1, -1):
        x=int(a[i])*(10**i)
        rev_a=rev_a+x
    return rev_a
    
    
