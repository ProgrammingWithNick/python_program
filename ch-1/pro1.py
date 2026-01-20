# 1. Simple Interest Calculator
print("="*50)
print("PROGRAM 1: SIMPLE INTEREST CALCULATOR")
print("="*50)
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
n = float(input("Enter Time period (years): "))
interest = (p * r * n) / 100
print(f"Simple Interest = {interest}")
print()
