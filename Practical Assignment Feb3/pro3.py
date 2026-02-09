# 3. WAP for print sum of series 1^2 + 2^2 + 3^2 + ... + n^2

n = int(input("Enter value of n: "))
sum = 0

for i in range(1, n + 1):
    sum += i * i

print("Sum of series:", sum)
