# 11. Variable Arguments Function
print("="*50)
print("PROGRAM 11: VARIABLE ARGUMENTS")
print("="*50)

def total_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

result = total_sum(10, 20, 30, 40, 50)
print(f"Total of (10, 20, 30, 40, 50): {result}")

result2 = total_sum(5, 15, 25)
print(f"Total of (5, 15, 25): {result2}")
print()