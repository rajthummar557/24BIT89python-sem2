# 1. Write a program to create three dictionaries and concatenate them to create fourth dictionary.
def concatenate_dicts():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    d3 = {"e": 5, "f": 6}
    d4 = {**d1, **d2, **d3}
    print("Concatenated dictionary:", d4)
# concatenate_dicts()

# 2. Write a program to check whether a dictionary is empty or not.
def check_empty_dict():
    d = {}
    if not d:
        print("Dictionary is empty")
    else:
        print("Dictionary is not empty")
# check_empty_dict()

# 3. Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and 
# maximum of salary.
def dept_salary_stats():
    data = [
        {"dept": 1, "roll": 101, "salary": 30000},
        {"dept": 1, "roll": 102, "salary": 25000},
        {"dept": 2, "roll": 201, "salary": 40000},
        {"dept": 2, "roll": 202, "salary": 35000},
        {"dept": 3, "roll": 301, "salary": 50000}
    ]
    stats = {}
    for i in data:
        d = i["dept"]
        s = i["salary"]
        if d not in stats:
            stats[d] = {"min": s, "max": s}
        else:
            stats[d]["min"] = min(stats[d]["min"], s)
            stats[d]["max"] = max(stats[d]["max"], s)
    print("Department wise salary stats:", stats)
# dept_salary_stats()

# 4. Write a program that reads a string from the keyboard and creates dictionary containing frequency 
# of each character occurring in the string.
def char_frequency():
    s = input("Enter a string: ")
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1
    print("Character frequencies:", freq)
# char_frequency()

# 5. Create two dictionaries – one containing grocery items and their prices and another containing 
# grocery items and quantity purchased. By using the values from these two dictionaries compute the 
# total bill.
def compute_total_bill():
    price = {"rice": 40, "wheat": 30, "sugar": 50, "milk": 60}
    quantity = {"rice": 2, "wheat": 3, "sugar": 1, "milk": 2}
    total = 0
    for i in price:
        total += price[i] * quantity.get(i, 0)
    print("Total bill:", total)
# compute_total_bill()
