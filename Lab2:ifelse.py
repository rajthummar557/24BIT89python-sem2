# 1) Print largest and smallest values out of two.
def largest_smallest_two():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Largest:", max(a, b))
    print("Smallest:", min(a, b))
# largest_smallest_two()

# 2) Print largest and smallest values out of three.
def largest_smallest_three():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    print("Largest:", max(a, b, c))
    print("Smallest:", min(a, b, c))
# largest_smallest_three()

# 3) Check whether a given number is odd or even.
def check_odd_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
# check_odd_even()

# 4) Check whether a given number is divisible by 10 or not.
def check_divisible_by_10():
    num = int(input("Enter a number: "))
    if num % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")
# check_divisible_by_10()

# 5) Accept age of a person. If age is less than 18, print minor otherwise Major.
def check_minor_major():
    age = int(input("Enter age: "))
    if age < 18:
        print("Minor")
    else:
        print("Major")
# check_minor_major()

# 6) Accept a number from the user. And print number of digits in it.
def count_digits():
    num = input("Enter a number: ")
    print("Number of digits:", len(num))
# count_digits()

# 7) Accept a year value from the user. Check whether it is a leap year or not.
def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
# check_leap_year()

# 8) Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard.
def check_triangle_validity():
    a = float(input("Enter first angle: "))
    b = float(input("Enter second angle: "))
    c = float(input("Enter third angle: "))
    if a + b + c == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")
# check_triangle_validity()

# 9) Print absolute value of a given number.
def absolute_value():
    num = float(input("Enter a number: "))
    print("Absolute value:", abs(num))
# absolute_value()

# 10) Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter.
def compare_area_perimeter():
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    perimeter = 2 * (length + breadth)
    if area > perimeter:
        print("Area is greater than Perimeter")
    else:
        print("Area is not greater than Perimeter")
# compare_area_perimeter()

# 11) Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.
def check_straight_line():
    x1, y1 = map(int, input("Enter coordinates of point 1 (x1, y1): ").split())
    x2, y2 = map(int, input("Enter coordinates of point 2 (x2, y2): ").split())
    x3, y3 = map(int, input("Enter coordinates of point 3 (x3, y3): ").split())
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        print("The points lie on a straight line")
    else:
        print("The points do not lie on a straight line")
# check_straight_line()

# 12) Given the coordinates (x, y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle.
from math import sqrt, pow
def check_point_in_circle():
    x, y = map(int, input("Enter coordinates of point (x, y): ").split())
    h, k = map(int, input("Enter coordinates of center of circle (h, k): ").split())
    r = float(input("Enter radius of the circle: "))
    distance = sqrt(pow(x - h, 2) + pow(y - k, 2))
    if distance < r:
        print("Point lies inside the circle")
    elif distance == r:
        print("Point lies on the circle")
    else:
        print("Point lies outside the circle")
# check_point_in_circle()

# 13) Convert number 0 to 19 to its equivalent words. E.g. 0 -> zero, 19 -> nineteen.
def number_to_words():
    num = int(input("Enter a number between 0 and 19: "))
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
             "eighteen", "nineteen"]
    if 0 <= num <= 19:
        print("Word:", words[num])
    else:
        print("Invalid number. Please enter a number between 0 and 19.")
# number_to_words()

# 14) Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. 
# If student secures <= 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the table.

def student_result():
    sub1 = int(input("Enter marks for subject 1: "))
    sub2 = int(input("Enter marks for subject 2: "))
    sub3 = int(input("Enter marks for subject 3: "))
    
    total = sub1 + sub2 + sub3
    average = total / 3
    
    grades = []
    passed = True
    
    # Function to assign grade based on marks
    def assign_grade(marks):
        if marks == 0:
            return "NA" 
        elif marks <= 39:
            return "F" 
        elif 40 <= marks <= 44:
            return "P"  
        elif 45 <= marks <= 49:
            return "C"  
        elif 50 <= marks <= 54:
            return "B"  
        elif 55 <= marks <= 59:
            return "B+"  
        elif 60 <= marks <= 69:
            return "A" 
        elif 70 <= marks <= 79:
            return "A+" 
        else:
            return "O" 
    
    # Assign grades for each subject
    grades.append(assign_grade(sub1))
    grades.append(assign_grade(sub2))
    grades.append(assign_grade(sub3))
    
    # Check if the student has failed in any subject
    if sub1 <= 39 or sub2 <= 39 or sub3 <= 39:
        passed = False
    
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Grades:", grades)
    
    if passed:
        print("Result: Passed")
    else:
        print("Result: Failed")

# student_result()

