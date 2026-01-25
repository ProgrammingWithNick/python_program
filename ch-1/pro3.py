# 3. Student Result Calculator
print("="*50)
print("PROGRAM 3: STUDENT RESULT")
print("="*50)
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))

total = sub1 + sub2 + sub3 + sub4
percentage = total / 4

if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'F'

print(f"Total Marks: {total}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
print()