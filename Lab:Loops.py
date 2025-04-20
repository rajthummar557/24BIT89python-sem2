import math

# 1) Print all alphabets in upper case and in lower case.
def print_alphabets():
    upper = [chr(i) for i in range(65, 91)]
    lower = [chr(i) for i in range(97, 123)]
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)
# print_alphabets()

# 2) Print a multiplication table of a given number.
def multiplication_table():
    n = int(input("Enter number for multiplication table: "))
    for i in range(1, 11):
        print(n, "*", i, "=", n * i)
# multiplication_table()

# 3) Count no. of alphabets and no. of digits in any given string.
def count_alpha_digit():
    s = input("Enter a string: ")
    a = 0
    d=0
    for i in s:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            d += 1
    print("Alphabets:", a)
    print("Digits:", d)
# count_alpha_digit()

# 4) Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.
def number_checks():
    n = int(input("Enter a number: "))
    prime = all(n%i!=0 for i in range(2, int(n**0.5)+1)) and n > 1
    perfect = sum(i for i in range(1, n) if n%i==0) == n
    armstrong = sum(int(i)**len(str(n)) for i in str(n)) == n
    palindrome = str(n) == str(n)[::-1]
    square = n*n
    automorphic = str(square).endswith(str(n))
    print("Prime:", prime)
    print("Perfect:", perfect)
    print("Armstrong:", armstrong)
    print("Palindrome:", palindrome)
    print("Automorphic:", automorphic)
# number_checks()

# 5) Generate all Pythagorean Triplets with side length <= 30.
def pythagorean_triplets():
    for i in range(1, 31):
        for j in range(i, 31):
            k = int((i**2 + j**2)**0.5)
            if k <= 30 and i**2 + j**2 == k**2:
                print(i, j, k)
# pythagorean_triplets()

# 6) Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
def print_24_hours():
    for i in range(24):
        if i == 0:
            print("12 Midnight")
        elif i == 12:
            print("12 Noon")
        elif i < 12:
            print(i, "AM")
        else:
            print(i-12, "PM")
# print_24_hours()

# 7) Print nCr and nPr.
def ncr_npr():
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    f = math.factorial
    ncr = f(n) // (f(r) * f(n - r))
    npr = f(n) // f(n - r)
    print("nCr:", ncr)
    print("nPr:", npr)
# ncr_npr()

# 8) Print factorial of a given number.
def factorial():
    n = int(input("Enter number: "))
    print("Factorial:", math.factorial(n))
# factorial()

# 9) Print N natural nos. in reverse.
def reverse_natural():
    n = int(input("Enter N: "))
    for i in range(n, 0, -1):
        print(i, end=" ")
    print()
# reverse_natural()

# 10) Generate N numbers of Fibonacci series.
def fibonacci(i,first=0,second=1,cnt=0):
    if count < i:
        print(first)
        fibonacci(i,second,first+second,cnt+1)
# n = int(input("Enter a number:"))
# fibonacci(n)

# 11) Calculate sin(x); x is a radian value.
def sin_x():
    deg = float(input("Enter angle in degrees: "))
    x = deg * 3.14159 / 180
    term = x
    sinx = 0
    sign = 1
    for i in range(1, 10, 2):
        sinx += sign * term
        sign *= -1
        term *= x * x / ((i + 1) * (i + 2))
    print("sin(x) approx:", sinx)
# sin_x()
