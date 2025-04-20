import random

# 1. Write a program that converts words present in a list into uppercase and stores them in a set.
def list_to_upper_set():
    words = ["apple", "banana", "cherry", "date", "elder"]
    upper_set = {i.upper() for i in words}
    print("Set with uppercase words:", upper_set)
# list_to_upper_set()

# 2. Write a program to create a set containing 10 random numbers in the range 15 to 45. Count how 
# many of these numbers are less than 30. Delete all numbers that are greater than 35.
def random_set_operations():
    nums = {random.randint(15, 45) for i in range(20)}
    while len(nums) > 10:
        nums.pop()
    print("Original Set:", nums)
    count = len([i for i in nums if i < 30])
    print("Count of numbers less than 30:", count)
    nums = {i for i in nums if i <= 35}
    print("Set after removing numbers > 35:", nums)
# random_set_operations()

# 3. Create an empty set. Write a program that adds five new names to this set, modifies one existing 
# name and deletes two names from it.
def modify_name_set():
    names = set()
    names.update(["Ankit", "Sneha", "Rahul", "Priya", "Amit"])
    names.remove("Sneha")
    names.remove("Amit")
    names.add("Snehalata")
    print("Modified set:", names)
# modify_name_set()

# 4. A set contains names which begin either with A or with B. Write a program to separate out the 
# names into two sets, one containing names beginning with A and another with B.
def separate_names_by_initial():
    all_names = {"Ankit", "Amit", "Anjali", "Bobby", "Bina", "Bhavesh", "Akash"}
    a_names = {i for i in all_names if i.startswith("A")}
    b_names = {i for i in all_names if i.startswith("B")}
    print("Names starting with A:", a_names)
    print("Names starting with B:", b_names)
# separate_names_by_initial()
