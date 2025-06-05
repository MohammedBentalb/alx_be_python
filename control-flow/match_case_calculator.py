num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Choose the operation (+, -, *, /): ")

if operation == '/' and num1 == 0:
    print('Cannot divide by zero')
    exit()

match operation:
    case "+":
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        result = num1 / num2
