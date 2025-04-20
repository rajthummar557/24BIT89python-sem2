

# 1. A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. Write a 
# program to find out number of boys and girls in the list.
def count_boys_girls():
    people = [("Rahul",), "Anjali", ("Aman",), "Priya", "Neha", ("Rohan",)]
    boys = 0
    girls = 0
    for i in people:
        if isinstance(i, tuple):
            boys += 1
        else:
            girls += 1
    print("Number of boys:", boys)
    print("Number of girls:", girls)
# count_boys_girls()

# 2. A list contains tuples containing roll no., name and age of student. Write a python program to create 
# three lists separately for roll no., name and age
def split_student_info():
    data = [(1, "Ankit", 18), (2, "Sneha", 19), (3, "Amit", 20)]
    roll = []
    name = []
    age = []
    for i in data:
        roll.append(i[0])
        name.append(i[1])
        age.append(i[2])
    print("Roll numbers:", roll)
    print("Names:", name)
    print("Ages:", age)
# split_student_info()

# 3. Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of 
# days between the two dates.
from datetime import date
def days_between_dates():
    date1 = (15, 4, 2023)
    date2 = (20, 4, 2025)
    d1 = date(date1[2], date1[1], date1[0])
    d2 = date(date2[2], date2[1], date2[0])
    diff = abs((d2 - d1).days)
    print("Number of days between the two dates:", diff)
# days_between_dates()

# 4. Create a list of tuples containing a food item and its price. Sort the tuples in descending order by 
# price.
def sort_food_prices():
    food = [("Pizza", 250), ("Burger", 100), ("Fries", 80), ("Pasta", 150)]
    sorted_food = sorted(food, key=lambda i: i[1], reverse=True)
    print("Sorted food items by price (descending):", sorted_food)
# sort_food_prices()

# 5. Remove empty tuple(s) from the list of tuples.
def remove_empty_tuples():
    tuples = [(), ("Python",), (), (1, 2), ()]
    cleaned = [i for i in tuples if i]
    print("List after removing empty tuples:", cleaned)
# remove_empty_tuples()

# 6. Modify an element of a tuple.
def modify_tuple_element():
    tup = (1, 2, 3, 4)
    new_tup = tup[:2] + (99,) + tup[3:]
    print("Modified tuple:", new_tup)
# modify_tuple_element()

# 7. Delete an element of a tuple.
def delete_tuple_element():
    tup = (10, 20, 30, 40)
    new_tup = tup[:1] + tup[2:]
    print("Tuple after deleting element at index 1:", new_tup)
# delete_tuple_element()
