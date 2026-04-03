# ============================================================
# DAY 2 - Conditionals, Loops, Strings, Lists
# ============================================================


# ============================================================
# COMPARISON OPERATORS
# ============================================================

# These return True or False
a = 10
b = 20

print(a == b)   # False - equal to
print(a != b)   # True  - not equal to
print(a > b)    # False - greater than
print(a < b)    # True  - less than
print(a >= 10)  # True  - greater than or equal
print(a <= 5)   # False - less than or equal


# ============================================================
# LOGICAL OPERATORS
# ============================================================

# and -> both must be True
print(a < b and a == 10)   # True

# or -> at least one must be True
print(a > b or a == 10)    # True

# not -> flips True to False and vice versa
print(not a == b)           # True


# ============================================================
# IF / ELIF / ELSE
# ============================================================

age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age == 18:
    print("Just turned adult!")
else:
    print("Adult")

# Nested if
score = 85

if score >= 50:
    if score >= 90:
        print("Grade: A+")
    elif score >= 80:
        print("Grade: A")
    else:
        print("Grade: B")
else:
    print("Failed")

# One-liner if (ternary expression)
status = "Pass" if score >= 50 else "Fail"
print(status)   # Pass


# ============================================================
# FOR LOOP
# ============================================================

# Loop over a range of numbers
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step = 2)
    print(i)

# Loop over a string
for char in "Python":
    print(char)

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index using enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# ============================================================
# WHILE LOOP
# ============================================================

count = 1
while count <= 5:
    print(f"count = {count}")
    count += 1   # IMPORTANT: without this it loops forever!

# while with user input (example - commented out to avoid blocking)
# while True:
#     ans = input("Type 'quit' to stop: ")
#     if ans == "quit":
#         break


# ============================================================
# BREAK, CONTINUE, PASS
# ============================================================

# break - exit the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)   # prints 0 1 2 3 4

# continue - skip current iteration, move to next
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)   # prints 1 3 5 7 9 (odd numbers only)

# pass - do nothing (placeholder)
for i in range(3):
    pass   # loop runs but does nothing (useful while writing code)


# ============================================================
# STRINGS - DEEP DIVE
# ============================================================

s = "  Hello, Python World!  "

# Length
print(len(s))              # total characters including spaces

# Case methods
print(s.upper())           # "  HELLO, PYTHON WORLD!  "
print(s.lower())           # "  hello, python world!  "
print(s.title())           # "  Hello, Python World!  "

# Strip whitespace
print(s.strip())           # "Hello, Python World!"
print(s.lstrip())          # remove left spaces only
print(s.rstrip())          # remove right spaces only

# Replace
print(s.replace("Python", "World"))

# Split - breaks string into a list
sentence = "one two three four"
words = sentence.split(" ")    # split by space
print(words)                   # ['one', 'two', 'three', 'four']

# Join - opposite of split
joined = "-".join(words)
print(joined)                  # one-two-three-four

# Check contents
print("Hello" in s)            # True
print(s.startswith("  Hello")) # True
print(s.endswith("  "))        # True

# String slicing  [start : stop : step]
text = "Python"
print(text[0])       # P       (first char)
print(text[-1])      # n       (last char)
print(text[0:3])     # Pyt     (index 0,1,2)
print(text[::2])     # Pto     (every 2nd char)
print(text[::-1])    # nohtyP  (reversed)

# Find & Count
print(text.find("th"))    # 2  (index where "th" starts, -1 if not found)
print(text.count("t"))    # 1  (how many times "t" appears)

# f-strings with formatting
pi = 3.14159
print(f"{pi:.2f}")         # 3.14  (2 decimal places)
print(f"{1000000:,}")      # 1,000,000  (comma separator)
print(f"{'hi':>10}")       # right-align in 10 chars
print(f"{'hi':<10}|")      # left-align in 10 chars


# ============================================================
# LISTS
# ============================================================

# Creating a list
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True]   # lists can hold any type

# Indexing
print(numbers[0])    # 10  (first)
print(numbers[-1])   # 50  (last)

# Slicing
print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])   # [10, 20, 30]
print(numbers[::2])  # [10, 30, 50]

# Modifying
numbers[0] = 99
print(numbers)       # [99, 20, 30, 40, 50]

# Adding items
numbers.append(60)         # add to end
numbers.insert(1, 15)      # insert at index 1
print(numbers)

# Removing items
numbers.remove(99)         # remove by value (first occurrence)
popped = numbers.pop()     # remove & return last item
popped_idx = numbers.pop(0)  # remove & return item at index 0
print(numbers)

# Useful list methods
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(nums))           # 8
print(sum(nums))           # 31
print(max(nums))           # 9
print(min(nums))           # 1
print(sorted(nums))        # [1, 1, 2, 3, 4, 5, 6, 9] (new sorted list)
nums.sort()                # sorts in place
nums.reverse()             # reverses in place
print(nums.count(1))       # 2 (how many times 1 appears)
print(nums.index(4))       # finds index of value 4

# Check membership
print(5 in nums)           # True
print(99 not in nums)      # True

# List comprehension (short way to build lists)
squares = [x**2 for x in range(1, 6)]
print(squares)             # [1, 4, 9, 16, 25]

evens = [x for x in range(20) if x % 2 == 0]
print(evens)               # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# ============================================================
# TRY / EXCEPT (Error Handling)
# ============================================================

# Without try/except, bad input crashes the program
# With try/except, you handle the error gracefully

try:
    num = int(input("Enter a number: "))
    print(f"10 divided by {num} = {10 / num:.2f}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print(f"Something went wrong: {e}")
else:
    print("No errors occurred!")
finally:
    print("Done.")  # always runs
