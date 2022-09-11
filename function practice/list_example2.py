
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


