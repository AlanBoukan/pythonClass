def maghsomAlieh(num):
    list1=list()
    for i in range(1, num+1):
        if num % i==0:
            list1.append(i)
    return list1

def commonMaghsum(num1, num2):
    list1=maghsomAlieh(num1)
    list2=maghsomAlieh(num2)
    #print(set(list1))
    common_elements = list(set(list1) & set(list2))
    return common_elements



def bmm(num1, num2):
    num1=int(num1)
    num2=int(num2)
    common_maghsum=commonMaghsum(num1,num2)
    return max(common_maghsum)
    
def kmm(num1, num2):
    bmm2Digit=bmm(num1,num2)
    kmm1=(num1*num2)/bmm2Digit
    return kmm1

def surat(makh1, makh2, sur):
    kmm1=kmm(makh1,makh2)
    surat1=(kmm1/makh1)*sur
    return surat1
    
def Endnum():
    makh1=int(input('pleas enter the mahraj1 number'))
    makh2=int(input('pleas enter the mahraj2 number'))
    sur1=int(input('pleas enter the surat1 number'))
    sur2=int(input('pleas enter the surat2 number'))
    ghalamat=input('pleas enter the +or-, * or / number')
    #if num5==+:
        #num1+num4
    
    kmm_mahraj=kmm(makh1, makh2)
  
    if ghalamat== '-':
        surat1=surat(makh1, makh2,sur1)
        #print(surat1)
        surat2=surat(makh2, makh1,sur2)
        suratAll=surat1-surat2
        bmmAll=bmm(suratAll,kmm_mahraj)
        suratAll=suratAll/bmmAll
        kmm_mahraj=kmm_mahraj/bmmAll
        print(str(suratAll)+"/"+str(kmm_mahraj))       
    if ghalamat== '+':
        surat1=surat(makh1, makh2,sur1)
        print(surat1)
        surat2=surat(makh2, makh1,sur2)
        suratAll=surat1+surat2
        bmmAll=bmm(suratAll,kmm_mahraj)
        suratAll=suratAll/bmmAll
        kmm_mahraj=kmm_mahraj/bmmAll
        print(str(suratAll)+"/"+str(kmm_mahraj))   

        
    if ghalamat== '*':
        suratAll=sur1*sur2
        makhAll=makh1*makh2
        bmmAll=bmm(suratAll,kmm_mahraj)
        suratAll=suratAll/bmmAll
        makhAll=makhAll/bmmAll
        print(str(suratAll)+"/"+str(makhAll))  
        
    if ghalamat== '/':
        suratAll=sur1*makh2
        makhAll=sur2*makh1
        bmmAll=bmm(suratAll,kmm_mahraj)
        suratAll=suratAll/bmmAll
        makhAll=makhAll/bmmAll
        print(str(suratAll)+"/"+str(makhAll))
