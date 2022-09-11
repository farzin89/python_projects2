
list1 = ["mehdi","ali","reza","ahmad","mohammad"]
list2 = []

for item in list1:
    if('m' in item):
        list2.append(item)
print(list2)

#..................................................

#method 2 (comperehence)

list3 = ["mehdi","ali","reza","ahmad","mohammad"]
list4 = [i for i in list3 if "m" in i ]
print(list4)

#..................................................

# print only name that start with "m"

list5 = ["mehdi","ali","reza","ahmad","mohammad"]
list6 = [j for j in list5 if "m"==j[0]]
print("people name with m ",list6)

#.................................................

# print only name that end with "d"

list5 = ["mehdi","ali","reza","ahmad","mohammad"]
list6 = [k for k in list5 if "d"==k[-1]]
print("people name that end with m ",list6)

#...............................................

# reverse

def myRevers(list9):
    tempList = []
    for i in range(len(list9)-1,-1,-1):
        tempList.append(list9[i])
    return tempList

list9 =[12,34,56,7,78,88,90,642]
print("revers :",myRevers(list9))

#...................................................

# sublist

def subList(List10):
    list11 =[]
    for i in range(0,len(list10)+1):
        for j in range(0,i):
            list11.append(list10[j:i])
    return list11


list10 = [1,2,3]
list11 = subList(list10)
print(list11)


#..................................................
#list7 = []
#for l in range(1,6):
#    list7.append(int(input("Enter Number : ")))
#print(list7)

#..................................................

list8 =[]
while True:
    num = int(input("Enter Number : "))
    if num < 0 :
        break
    if num not in list8:
        3
        list8.append(num)
print(list8)



