# 10. Lambda Functions with Operators
print("="*50)
print("PROGRAM 10: LAMBDA FUNCTIONS")
print("="*50)

add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print(f"Result: {add(num1, num2)}")
elif operator == '-':
    print(f"Result: {subtract(num1, num2)}")
elif operator == '*':
    print(f"Result: {multiply(num1, num2)}")
elif operator == '/':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid operator!")
print()
