def countElement(a,list1):
    count=0
    for i in range(len(list1)):
        if a==list1[i]:
            count+=1
    return count
            

def read():
    
    f = open("And_Or.txt", 'r')
    f=f.read()
    splitFile = f.split(" ")
    countAnd=0
    for word in splitFile:
        if word.lower()=='alan' or word.lower()=='alan,' or word.lower()==',alan' :
            countAnd+=1
            
    #print(countAnd)
    #print(splitFile)
    dict1=dict()
    print(dict1)
    for word in splitFile:
        #print(word)
        countWord=countElement(word,splitFile)
        dict1[word]=countWord
    maxCount=0
    wordMax=list()
    wordMax.append(" ")
    for item in dict1:
        if dict1[item]>maxCount:
            maxCount=dict1[item]
            wordMax[0]=item
            #wordMax.append(item)
    #print(dict1)
    print("The heigh ferquent word is:  "+wordMax[0])
    print("Count this owrd is:   "+str(maxCount))
        
    
          
