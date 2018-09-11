
print("Hello welcome to pocket calculator")

def add (number1, number2):
    return number1+ number2

def diff (number1, number2):
    return number1-number2

def mult (number1, number2):
    return number1*number2

def div (number1, number2):
    return number1/number2

number1 = int (input ("Please add the first number "))
number2 = int (input ("Please add the second number "))
operator = input ("Please enter the operator ")

if operator == "+":
    print(number1,'+',number2,'=', add(number1, number2))

if operator == "-":
    print(number1, '-', number2, '=', diff(number1, number2))

if operator == "*":
    print(number1, '*', number2, '=', mult(number1, number2))

if operator == "/":
    print(number1, '/', number2, '=', div(number1, number2))


