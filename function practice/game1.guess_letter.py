
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
    print(newName)


names = filNameList()
selectName = getRandomName(names)
print(selectName)
hideCharForName(selectName)




