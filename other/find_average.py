
def average(num):
    total_sum = 0
    for n in range(num):
        numbers = float(input("Enter any numbers"))
        total_sum += numbers

    avg = total_sum / num
    print("Average is :",avg)



num = int(input("How many numbers ? "))
average(num)