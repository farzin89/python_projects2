

def addItemTolist(list1,a,index):
    list2 = list1[:index]
    list2.append(a)
    list2+=list1[index:]

    return list2






list1 = [23, 45, 67, 89, 124,156]
print(addItemTolist(list1,2000,3))