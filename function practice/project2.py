
def printList(list1):
    for item in list1:
        print(item,end="\t")


def addItemToList(list1,a,index):

    list2 = list1[:index]
    list2.append(a)
    list2 += list1[index:]
    printList(list2)



list1 = [23,45,67,54,89,76,34,778,990,345]
num = int(input("enter number : "))
index = int(input("enter index : "))
addItemToList(list1,num,index)