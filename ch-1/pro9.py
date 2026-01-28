# 9. Function with Arithmetic Operations
print("="*50)
print("PROGRAM 9: FUNCTION WITH OPERATORS")
print("="*50)

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
result = calculate(a, b, op)
print(f"Result: {result}")
print()