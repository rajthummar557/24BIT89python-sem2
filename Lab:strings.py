# 1) Count how many vowels there are in a string. Accept the string from the user.
def count_vowels():
    s = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    print("Vowels count:", count)
# count_vowels()

# 2) Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.
def to_lowercase(s):
    result = ""
    for i in s:
        if 'A' <= i <= 'Z':
            result += chr(ord(i) + 32)
        else:
            result += i
    return result

def to_uppercase(s):
    result = ""
    for i in s:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i
    return result

def toggle_case(s):
    result = ""
    for i in s:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        elif 'A' <= i <= 'Z':
            result += chr(ord(i) + 32)
        else:
            result += i
    return result

# Test the functions
s = "Hello World"
print("Lowercase:", to_lowercase(s))
print("Uppercase:", to_uppercase(s))
print("Toggle case:", toggle_case(s))

# 3) Accept two strings. Check whether one string is there in another string.
def check_substring():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    if s2 in s1:
        print("Yes, second string is present in the first string.")
    else:
        print("No, second string is not present in the first string.")
# check_substring()

# 4) Write a function that removes one string from another string, if present.
def remove_string():
    s1 = input("Enter first string: ")
    s2 = input("Enter string to remove: ")
    result = s1.replace(s2, "")
    print("Final string:", result)
# remove_string()
