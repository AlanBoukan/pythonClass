def rew_number():
    a=(input('pleas enter the number'))
    rev_a=0
    for i in range(len(a)-1,-1,-1):
        
        x=int(a[i])*(10**i)
        rev_a=rev_a+x
    return rev_a
