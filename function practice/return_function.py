
def printList(list1):
    for item in list1:
        if (type(item)==list):
            printList(item)
        else:
            print(item,end=' ')

list1 = [1,2,[3,4,[10,20,30],6],7,8,[1,2,[2,3,[2,[23,45,[10,20,30]],4]],5]]
printList(list1)