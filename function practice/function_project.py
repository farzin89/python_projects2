
def readList(list1):
    while True:
        num = int(input("Enter Number : "))
        if num < 0:
            break
        if num not in list1:
            list1.append(num)

def mulList(list1):
    for i in range(0,len(list1)):
        list1[i]*=10


list1=[]
readList(list1)
mulList(list1)
print(list1)