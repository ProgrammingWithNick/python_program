# 4. Armstrong Number Finder
print("="*50)
print("PROGRAM 4: ARMSTRONG NUMBERS")
print("="*50)
numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

print("\nArmstrong numbers from the list:")
for num in numbers:
    temp = num
    sum_digits = 0
    digits = len(str(abs(num)))
    
    while temp > 0:
        digit = temp % 10
        sum_digits += digit ** digits
        temp //= 10
    
    if sum_digits == num:
        print(num)
print()
