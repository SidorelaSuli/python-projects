number1 = input("enter first number: ")
number2 = input("enter second number: ") # by default will be converted to string
#therefore we have to convert the strings into numbers with int() funtion
result = int(number1) + int(number2)
print(result)
# for decimal numbers we can use float()

result1 = float(number1) + float(number2)
print(result1)