
def square(n):
    print(n * '* ')
    for i in range(n-2):
        print('* ' + (n-2) * '  ' + '* ')
    print(n * '* ')




length = int(input("Enter square side lenght : "))
if length < 2:
    print('invalid input !')
else:
    square(n=length)
