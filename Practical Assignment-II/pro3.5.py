# Recursive function to calculate factorial
# 3. Factorial Program

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# User Input
num = int(input("Enter a number: "))
print("Factorial (Recursive):", factorial(num))
