# match_case_calculator.py
# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Ask the user to choose the operation
operation = input("Choose the operation (+, -, *, /): ")
#perform the calculation using match case
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
        print(f"The result is {result}.")
        else:
            print("Cannot be divided by zero.")
    case _:
        print("Invalid operation")                        