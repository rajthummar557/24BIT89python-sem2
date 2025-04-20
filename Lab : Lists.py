import random

# 1. Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using 
# random nos. Replace the third element of odd integers with a list of 4 even integers. Flatten, sort 
# and print the list. Provide appropriate message at each stage.
def odd_even_list_replace():
    odd_list = [random.randrange(1, 50, 2) for i in range(5)]
    even_list = [random.randrange(2, 50, 2) for i in range(4)]
    print("list of 5 odd integers:", odd_list)
    print("list of 4 even integers:", even_list)
    odd_list[2] = even_list
    print("List after replacing 3rd element with even list:", odd_list)
    flat_list = []
    for i in odd_list:
        if isinstance(i, list):
            flat_list.extend(i)
        else:
            flat_list.append(i)
    print("Flattened list:", flat_list)
    flat_list.sort()
    print("Sorted list:", flat_list)
# odd_even_list_replace()

# 2. Generate 20 random integers and store them in a list. Accept a number from the user and print 
# position of all occurrences of that number in the list.
def find_occurance():
    num = [random.randint(1, 50) for i in range(20)]
    print("list of 20 random numbers:", num)
    n = int(input("Enter number to find occurrences: "))
    ans = []
    for i in range(20):
        if num[i] == n:
            ans.append(i)
    print("The number occurs at:", ans)
# find_occurance()

# 3. Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.
def remove_duplicates():
    nums = [random.randint(1, 30) for i in range(50)]
    print("Original list with duplicates:", nums)
    unique_nums = list(set(nums))
    print("List after removing duplicates:", unique_nums)
# remove_duplicates()

# 4. Generate 30 random numbers and put them in a list. Create two more lists – one containing only 
# +ve numbers and another with –ve nos.
def split_pos_neg():
    nums = [random.randint(-50, 50) for i in range(30)]
    print("Original list of 30 numbers:", nums)
    positives = [i for i in nums if i > 0]
    negatives = [i for i in nums if i < 0]
    print("Positive numbers:", positives)
    print("Negative numbers:", negatives)
# split_pos_neg()

# 5. A list contains 5 strings. Convert all these strings to uppercase.
def convert_uppercase():
    words = ["hello", "world", "python", "list", "string"]
    print("Original list of strings:", words)
    upper_words = [i.upper() for i in words]
    print("List with uppercase strings:", upper_words)
# convert_uppercase()

# 6. Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
def convert_temp():
    fahrenheit = [32, 68, 100, 212, 50]
    print("Fahrenheit temperatures:", fahrenheit)
    celsius = [round((i - 32) * 5 / 9, 2) for i in fahrenheit]
    print("Celsius temperatures:", celsius)
# convert_temp()

# 7. Write a menu-driven program to implement the stack data structure.
def stack_menu():
    stack = []
    while True:
        print("\nMenu:\n1. Push\n2. Pop\n3. Display\n4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            val = input("Enter value to push: ")
            stack.append(val)
            print("Stack after push:", stack)
        elif choice == 2:
            if stack:
                print("Popped element:", stack.pop())
            else:
                print("Stack is empty")
        elif choice == 3:
            print("Current Stack:", stack)
        elif choice == 4:
            break
        else:
            print("Invalid choice")
# stack_menu()

# 8. Write a menu-driven program to implement the Queue data structure.
def queue_menu():
    queue = []
    while True:
        print("\nMenu:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            val = input("Enter value to enqueue: ")
            queue.append(val)
            print("Queue after enqueue:", queue)
        elif choice == 2:
            if queue:
                print("Dequeued element:", queue.pop(0))
            else:
                print("Queue is empty")
        elif choice == 3:
            print("Current Queue:", queue)
        elif choice == 4:
            break
        else:
            print("Invalid choice")
# queue_menu()

# 9. Take two lists of numbers. Create third list of numbers for only those numbers from first list which 
# are not there in 2nd list (use list comprehension).
def list_diff():
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [2, 4, 6, 8]
    result = [i for i in list1 if i not in list2]
    print("List1:", list1)
    print("List2:", list2)
    print("Elements in List1 but not in List2:", result)
# list_diff()
