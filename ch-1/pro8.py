# 8. String Operations
print("="*50)
print("PROGRAM 8: STRING OPERATIONS")
print("="*50)
text = input("Enter a string: ")

# a) Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"a) Number of vowels: {vowel_count}")

# b) Count length without len()
length = 0
for char in text:
    length += 1
print(f"b) Length of string: {length}")

# c) Reverse string
reversed_text = text[::-1]
print(f"c) Reversed string: {reversed_text}")

# d) Find and replace
find_str = input("d) Enter string to find: ")
replace_str = input("   Enter string to replace with: ")
new_text = text.replace(find_str, replace_str)
print(f"   Result: {new_text}")

# e) Palindrome check
if text.lower() == text.lower()[::-1]:
    print("e) String is a palindrome!")
else:
    print("e) String is NOT a palindrome!")
print()