# Function to calculate factorial using loop
# 3. Factorial Program

def factorial(n):
    if n<0:
        return
    fact = 1
    for i in range(1, n + 1):
        fact=fact * i
    return fact

# User Input
num = int(input("Enter a number: "))
print("Factorial (Normal Function):", factorial(num))
