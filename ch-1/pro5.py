# 5. Largest Odd Number Finder
print("="*50)
print("PROGRAM 5: LARGEST ODD NUMBER")
print("="*50)
numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

odd_numbers = [num for num in numbers if num % 2 != 0]

if odd_numbers:
    print(f"Largest odd number: {max(odd_numbers)}")
else:
    print("No odd numbers found!")
print()