# 2. Arithmetic Calculator with Operator Input
print("="*50)
print("PROGRAM 2: ARITHMETIC CALCULATOR")
print("="*50)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print(f"Result: {num1 + num2}")
elif operator == '-':
    print(f"Result: {num1 - num2}")
elif operator == '*':
    print(f"Result: {num1 * num2}")
elif operator == '/':
    print(f"Result: {num1 / num2}")
else:
    print("Invalid operator!")
print()