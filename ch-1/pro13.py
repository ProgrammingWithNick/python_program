# 13. Map, Filter, and Reduce with Lambda
print("="*50)
print("PROGRAM 13: MAP, FILTER, REDUCE")
print("="*50)
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map: Square each number
squared = list(map(lambda x: x**2, numbers))
print(f"Original numbers: {numbers}")
print(f"Squared (map): {squared}")

# Filter: Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (filter): {evens}")

# Reduce: Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum of all numbers (reduce): {total}")

# Reduce: Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of all numbers (reduce): {product}")
print()