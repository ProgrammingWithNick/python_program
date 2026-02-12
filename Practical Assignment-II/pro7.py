# 7. Menu Driven Program: Student Result System

def enter_marks():
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        marks.append(float(input("Enter marks: ")))
    return marks

def calculate_percentage(marks):
    return sum(marks) / len(marks)

def assign_grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 50:
        return "C"
    else:
        return "Fail"

marks = []

while True:
    print("\n1. Enter Marks")
    print("2. Show Percentage")
    print("3. Show Grade")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        marks = enter_marks()

    elif choice == 2:
        if marks:
            per = calculate_percentage(marks)
            print("Percentage:", per)
        else:
            print("Enter marks first!")

    elif choice == 3:
        if marks:
            per = calculate_percentage(marks)
            print("Grade:", assign_grade(per))
        else:
            print("Enter marks first!")

    elif choice == 4:
        break

    else:
        print("Invalid choice")

