
# factorial calculation function
def fact(num):                            # 4=> 24
    f=1
    for i in range(1,num+1):
        f*= i
    return f

n = int(input('Enter Number : '))        #5
sum = 0

for i in range(0,n):                     # 0 1 2 3 4
    sorat = 2**i
    makhraj = fact(2*(i+1)-1)
    sum+= sorat/makhraj
print(sum)
