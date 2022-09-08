
def stringToList(str1):
    list1 = list(str1)
    return list1

def showStar():
    print("\n**********************")

def printList(list1):
    for item in list1:
        print(item,end="\t")
    showStar()


def wordLen(str1):
    list1 = list(str1)
    wl = 1
    for i in range(0,len(list1)):
        if(list1[i] == ' ' and list1[i+1] != ' '):
           wl += 1
    return wl

#def wordLen(str1):
#    list1 = list(str1)
#     wl = 1
#     for item in list1:
#       if item ==' ':
#
#           wl+=1
#  return wl


str1 = input("Enter Text : ")
#printList(stringToList(str1))
print(wordLen(str1))