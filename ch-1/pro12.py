# 12. Local, Global, and Nonlocal Variables
print("="*50)
print("PROGRAM 12: LOCAL, GLOBAL, NONLOCAL")
print("="*50)

global_var = 100

def outer_function():
    nonlocal_var = 50
    
    def inner_function():
        nonlocal nonlocal_var
        local_var = 10
        
        print(f"Local variable: {local_var}")
        print(f"Nonlocal variable (before): {nonlocal_var}")
        nonlocal_var = 75
        print(f"Nonlocal variable (after): {nonlocal_var}")
        print(f"Global variable: {global_var}")
    
    inner_function()
    print(f"Nonlocal variable in outer function: {nonlocal_var}")

outer_function()
print(f"Global variable outside function: {global_var}")
print()