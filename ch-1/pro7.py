# 7. List Operations Menu
print("="*50)
print("PROGRAM 7: LIST OPERATIONS")
print("="*50)
my_list = []

while True:
    print("\n--- LIST MENU ---")
    print("1. Add element")
    print("2. Remove element")
    print("3. Display list")
    print("4. Sort list")
    print("5. Search element")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        element = input("Enter element to add: ")
        my_list.append(element)
        print("Element added!")
    elif choice == '2':
        element = input("Enter element to remove: ")
        if element in my_list:
            my_list.remove(element)
            print("Element removed!")
        else:
            print("Element not found!")
    elif choice == '3':
        print(f"List: {my_list}")
    elif choice == '4':
        my_list.sort()
        print("List sorted!")
    elif choice == '5':
        element = input("Enter element to search: ")
        if element in my_list:
            print(f"Element found at index {my_list.index(element)}")
        else:
            print("Element not found!")
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
print()
