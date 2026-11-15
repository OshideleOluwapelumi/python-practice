print("MINI CALCULATOR!!!")
sign = input("OPERATOR YOU WANT TO USE: ")
number1 = int(input("INPUT FIRST NUMBER: "))
number2 = int(input("INPUT SECOND NUMBER: " ))
if sign == "+":
    print(number1 + number2)
elif sign == "-":
    print(number1-number2)
elif sign == "/":
    print(number1/number2)
elif sign == "*":
    print(number1*number2)
