
x = int(input("Enter Number : "))
for num in range(1,x):

    temp = num
    sum = 0
    while num > 0:
        sum+= num % 10
        num//= 10
    if temp % sum == 0:
        print(temp, end='\t')




#num = int(input("Enter Number : "))
#temp = num

#sum = 0
#while num > 0 :
    #sum += num % 10
    #num//=10


# this if code is for two condition
#print("Yes") if temp % sum == 0 else print('No')

