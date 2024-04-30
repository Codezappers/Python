def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def subtract(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def multiply(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def divide(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

while True:
    print("Options: ")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        add(num1, num2)
    elif user_input == "subtract":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        subtract(num1, num2)
    elif user_input == "multiply":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        multiply(num1, num2)
    elif user_input == "divide":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        divide(num1, num2)
    elif user_input == "quit":
        break