
def calculate_basic_math(num1,Operator,num2):

    if Operator == '+':
        cal = num1 + num2
    elif Operator == "-":
        cal = num1 - num2
    elif Operator == "*":
        cal = num1 * num2
    elif Operator == '/':
        cal = num1 / num2
    else:
        cal = "The operator is not valid ! "
    print(cal)



try:
    num1 = int(input("Please Enter Number1: "))
    Operator =input("please Enter the operator (+ - * /):")
    num2 = int(input("please Enter Number2: "))
except:
    print("Something went wrong !")
else:
    calculate_basic_math(num1,Operator,num2)

