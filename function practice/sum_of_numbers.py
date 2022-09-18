def is_numeric(x):
    try :
        float(x)
        return True
    except:
        return False

num1 = input("Enter your input : ").split()

numeric_string = list(filter(is_numeric,num1))
if numeric_string:
    numbers = map(float,numeric_string)
    print("Sum of numbers: ",sum(numbers))
else:
    print("There is no number!")
