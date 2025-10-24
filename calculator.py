# Basic calculator with error handling
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    else:
        raise ValueError("Invalid operator.")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    print(f"Result: {calculator(a, b, op)}")
except Exception as e:
    print(e)
