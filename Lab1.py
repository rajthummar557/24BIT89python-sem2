# 1. Add two numbers.
def add_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)
add_numbers()

# 2. Subtract two numbers.
def subtract_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Difference:", a - b)
subtract_numbers()

# 3. Multiply two numbers.
def multiply_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Product:", a * b)
multiply_numbers()

# 4. Divide two numbers.
def divide_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b != 0:
        print("Division:", a / b)
    else:
        print("Error: Division by zero")
divide_numbers()

# 5. Add, multiply, subtract and divide two numbers.
def operations():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Error: Division by zero")
operations()

# 6. Convert hours into minutes.
def hours_to_minutes():
    hours = int(input("Enter hours: "))
    print("Minutes:", hours * 60)
hours_to_minutes()

# 7. Convert minutes into hours.
def minutes_to_hours():
    minutes = int(input("Enter minutes: "))
    print("Hours:", minutes / 60)
minutes_to_hours()

# 8. Convert dollars into Rs. Where 1 $ = 48 Rs.
def dollars_to_rs():
    dollars = int(input("Enter dollars: "))
    print("Rs:", dollars * 48)
dollars_to_rs()

# 9. Convert Rs. into dollars where 1 $ = 48 Rs.
def rs_to_dollars():
    rs = int(input("Enter Rs: "))
    print("Dollars:", rs / 48)
rs_to_dollars()

# 10. Convert dollars into pound where 1 $ = 48 Rs. And 1 pound = 70 Rs.
def dollars_to_pound():
    dollars = int(input("Enter dollars: "))
    rs = dollars * 48
    pounds = rs / 70
    print("Pounds:", pounds)
dollars_to_pound()

# 11. Convert grams into kg.
def grams_to_kg():
    grams = int(input("Enter grams: "))
    print("Kilograms:", grams / 1000)
grams_to_kg()

# 12. Convert kgs into grams.
def kgs_to_grams():
    kgs = int(input("Enter kilograms: "))
    print("Grams:", kgs * 1000)
kgs_to_grams()

# 13. Convert bytes into KB, MB and GB.
def bytes_to_units():
    bytes = int(input("Enter bytes: "))
    kb = bytes / 1024
    mb = kb / 1024
    gb = mb / 1024
    print("KB:", kb)
    print("MB:", mb)
    print("GB:", gb)
bytes_to_units()

# 14. Convert celcius into Fahrenheit. F = (9/5 * C) + 32
def celsius_to_fahrenheit():
    celsius = int(input("Enter Celsius: "))
    fahrenheit = (9/5 * celsius) + 32
    print("Fahrenheit:", fahrenheit)
celsius_to_fahrenheit()

# 15. Convert Fahrenheit into celcius. C = 5/9 * (F – 32)
def fahrenheit_to_celsius():
    fahrenheit = int(input("Enter Fahrenheit: "))
    celsius = 5/9 * (fahrenheit - 32)
    print("Celsius:", celsius)
fahrenheit_to_celsius()

# 16. Calculate interest where I = PRN/100.
def calculate_interest():
    p = int(input("Enter principal: "))
    r = int(input("Enter rate: "))
    n = int(input("Enter time in years: "))
    interest = (p * r * n) / 100
    print("Interest:", interest)
calculate_interest()

# 17. Calculate area & perimeter of a square. A = L^2, P = 4L
def square_area_perimeter():
    side = int(input("Enter side of square: "))
    area = side ** 2
    perimeter = 4 * side
    print("Area:", area)
    print("Perimeter:", perimeter)
square_area_perimeter()

# 18. Calculate area & perimeter of a rectangle. A = L*B, P = 2(L+B)
def rectangle_area_perimeter():
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    area = length * breadth
    perimeter = 2 * (length + breadth)
    print("Area:", area)
    print("Perimeter:", perimeter)
rectangle_area_perimeter()

# 19. Calculate area of a circle. A = 22/7 * R * R
def circle_area():
    radius = int(input("Enter radius: "))
    area = (22/7) * radius * radius
    print("Area:", area)
circle_area()

# 20. Calculate area of a triangle. A = H*L/2
def triangle_area():
    height = int(input("Enter height: "))
    length = int(input("Enter length: "))
    area = (height * length) / 2
    print("Area:", area)
triangle_area()

# 21. Calculate net salary where net salary = gross salary + allowance – deduction.
# Allowances are 10% while deductions are 3% of gross salary.
def net_salary():
    gross_salary = int(input("Enter gross salary: "))
    allowance = 0.10 * gross_salary
    deduction = 0.03 * gross_salary
    net_salary = gross_salary + allowance - deduction
    print("Net salary:", net_salary)
net_salary()

# 22. Calculate net sales where net sales = gross sales – 10% discount of gross sales.
def net_sales():
    gross_sales = int(input("Enter gross sales: "))
    discount = 0.10 * gross_sales
    net_sales = gross_sales - discount
    print("Net sales:", net_sales)
net_sales()

# 23. Calculate average of three subjects along with their total.
def average_and_total():
    sub1 = int(input("Enter marks for subject 1: "))
    sub2 = int(input("Enter marks for subject 2: "))
    sub3 = int(input("Enter marks for subject 3: "))
    total = sub1 + sub2 + sub3
    average = total / 3
    print("Total marks:", total)
    print("Average marks:", average)
average_and_total()

# 24. Swap two values.
def swap_values():
    a = input("Enter first value: ")
    b = input("Enter second value: ")
    a, b = b, a
    print("Swapped values:", a, b)
swap_values()
