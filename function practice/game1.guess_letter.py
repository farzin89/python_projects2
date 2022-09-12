
import random

def filNameList():
    list1=["ali","reza","mehdi","ahmad","sara","mohammad"]
    return list1

def getRandomName(list1):
    return random.choice(list1)

def hideCharForName(selectName):                          #mehdi
    len1 = len(selectName)                                # l=5
    index = random.randint(0,len1-1)                      #index =3
    newName=selectName[:index]+'_'+selectName[index+1:]
    hideChar = selectName[index]
    print(newName)
    return hideChar

def playing(selectName,hideChar):
    count = 0
    for i in range(0,len(selectName)):
        ch =input("Enter char : ")
        count+=1
        if(ch==hideChar):
            break
    return count

def printResult(count,len1):
    if count < len1:
        print("win")
    else:
        print('lose')
names = filNameList()
selectName = getRandomName(names)
hideChar= hideCharForName(selectName)
count = playing(selectName,hideChar)
printResult(count,len(selectName))



