
# removing duplicate numbers

#list1 = [10,20,30,20,40,50,10,15,45,20,40]
#templist =[]

#for item in list1:
#    if item not in templist:
#        templist.append(item)
#print(templist)

#........................................................

# checking two list

#list1 =[1,2,3,4,5,6,7]
#list2 =[8,9,10,11,4,12]
#flag = False

#for item1 in list1:
#    for item2 in list2:
#        if item1 == item2:
#            flag = True
#            break
#print('Yes') if flag == True else print("No")

#........................................................

# another method

#list1 =[1,2,3,4,5,6,7]
#list2 =[8,9,10,11,4,12]
#flag = False

#for item1 in list1:
#    if item1 in list2:
#        flag = True
#        break
#print('Yes') if flag == True else print("No")

#........................................................

list1 =[1,2,3,4,5,6]
list2= []

for item in list1 :
    list2.append(item*item)
print(list2)
#.........................................................
# another method

list3= [1,2,3,4,5,6]
list4 =[x*x for x in list3]
print("method2",list4)
#..........................................................
list5 =[1,2,3,4]
list6 =[10,20,30]
list7 =[x * y for x in list5 for y in list6]
print(list7)
#.........................................................

list8 =['ali','amir','mohammad']
list9 =['reza','hosseyn']
list10 = [x+y for x in list8 for y in list9 ]
print(list10)
#........................................................

list11 = [2,23,35,68,12,24,53,18]
list12 =[x for x in list11 if x%2==0]
print(list12)

#.......................................................

list13 = [2,23,35,68,12,24,53,18]
list14 = [x+1 if x > 30 else x+10 for x in list13]
print(list14)