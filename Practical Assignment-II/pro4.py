# 4. Function with Default Argument (Simple Interest)

def simple_interest(p, t, r=5):
    return (p * t * r) / 100

p = float(input("Enter Principal amount: "))
t = float(input("Enter Time (years): "))
r = input("Enter Rate (Press Enter for default 5%): ")

if r == "":
    print("Simple Interest:", simple_interest(p, t))
else:
    print("Simple Interest:", simple_interest(p, t, float(r)))
