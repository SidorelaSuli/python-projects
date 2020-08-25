num1 = float(input("Enter number one: "))
operator = input("Enter the operator: ")
num2 = float(input("Enter number two: "))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "/":
    print(num1/num2)
elif operator == "*":
    print(num1*num2)
else:
    print("Invalid operator")
