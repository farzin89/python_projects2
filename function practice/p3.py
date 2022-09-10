
n = int(input("Enter N : "))
k = int(input("Enter K : "))

sum =0

for i in range(1,n+1):
    s2 = 0
    for j in range(1,i+1):
        s2 = s2 * 10 + k
    print(s2,end=' ')
    sum += s2
print( )
print(sum)


