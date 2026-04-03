# ============================================================
# DAY 3 - FUNCTIONS
# The most important building block in all of programming
# ============================================================


# ============================================================
# WHY FUNCTIONS?
# ============================================================

# WITHOUT functions - repeated code, hard to fix
# print("Hello, Alice!")
# print("Hello, Bob!")
# print("Hello, Charlie!")

# WITH functions - write once, use everywhere
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")


# ============================================================
# DEFINING A FUNCTION
# ============================================================

# Syntax:
# def function_name(parameters):
#     body
#     return value   <- optional

def say_hello():          # no parameters
    print("Hello!")

say_hello()               # calling the function


# ============================================================
# PARAMETERS vs ARGUMENTS
# ============================================================

# parameter = variable in the function definition
# argument  = actual value you pass when calling

def add(a, b):            # a and b are PARAMETERS
    result = a + b
    return result

total = add(10, 20)       # 10 and 20 are ARGUMENTS
print(total)              # 30


# ============================================================
# RETURN VALUES
# ============================================================

def square(n):
    return n ** 2

print(square(5))          # 25
print(square(12))         # 144

# Functions without return statement return None
def just_print(msg):
    print(msg)

x = just_print("hi")
print(x)                  # None

# Return multiple values (returns a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 2, 7])
print(f"Min: {low}, Max: {high}")   # Min: 1, Max: 9


# ============================================================
# DEFAULT PARAMETERS
# ============================================================

# Default value is used when argument is not provided
def power(base, exponent=2):    # exponent defaults to 2
    return base ** exponent

print(power(3))       # 9  (uses default exponent=2)
print(power(3, 3))    # 27 (overrides default)
print(power(2, 10))   # 1024


# ============================================================
# KEYWORD ARGUMENTS
# ============================================================

# You can pass arguments by name - order doesn't matter
def describe_person(name, age, city):
    print(f"{name} is {age} years old from {city}")

describe_person("Ali", 20, "Karachi")                   # positional
describe_person(age=25, city="Lahore", name="Sara")     # keyword (any order)
describe_person("Umar", city="Islamabad", age=30)       # mixed


# ============================================================
# *args - VARIABLE NUMBER OF ARGUMENTS
# ============================================================

# When you don't know how many arguments will be passed
# *args collects extra positional args into a TUPLE

def add_all(*args):
    print(args)           # it's a tuple
    return sum(args)

print(add_all(1, 2))             # 3
print(add_all(1, 2, 3, 4, 5))   # 15
print(add_all(10, 20, 30))       # 60


# ============================================================
# **kwargs - VARIABLE KEYWORD ARGUMENTS
# ============================================================

# **kwargs collects extra keyword args into a DICTIONARY

def show_info(**kwargs):
    print(kwargs)         # it's a dict
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

show_info(name="Ali", age=20, city="Karachi")


# ============================================================
# SCOPE - WHERE VARIABLES LIVE
# ============================================================

# LOCAL variable - only exists inside the function
def my_func():
    local_var = 100       # only accessible inside my_func
    print(local_var)

my_func()
# print(local_var)        # NameError! local_var doesn't exist here

# GLOBAL variable - exists in the whole file
global_var = "I am global"

def read_global():
    print(global_var)     # can READ global variables

read_global()

# To MODIFY a global variable inside a function:
counter = 0

def increment():
    global counter        # declare you want to modify the global
    counter += 1

increment()
increment()
print(counter)            # 2


# ============================================================
# DOCSTRINGS - documenting your functions
# ============================================================

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms
        height_m: Height in meters

    Returns:
        BMI as a float, rounded to 2 decimal places
    """
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

print(calculate_bmi(70, 1.75))    # 22.86
print(calculate_bmi.__doc__)      # prints the docstring


# ============================================================
# FUNCTIONS CALLING OTHER FUNCTIONS
# ============================================================

def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

def get_status(score):
    if score >= 50:
        return "Pass"
    return "Fail"

def full_report(name, score):
    grade = get_grade(score)      # calling another function
    status = get_status(score)    # calling another function
    print(f"{name} | Score: {score} | Grade: {grade} | Status: {status}")

full_report("Ali",   95)
full_report("Sara",  72)
full_report("Umar",  45)


# ============================================================
# LAMBDA - ONE-LINE ANONYMOUS FUNCTIONS
# ============================================================

# Syntax: lambda parameters: expression

double = lambda x: x * 2
print(double(5))          # 10

add = lambda a, b: a + b
print(add(3, 7))          # 10

# Most useful with map() and filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() - apply a function to every item
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)            # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# filter() - keep only items where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)              # [2, 4, 6, 8, 10]

# sorted() with lambda as key
students = [("Ali", 88), ("Sara", 95), ("Umar", 72)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print(sorted_students)    # sorted by score, highest first


# ============================================================
# COMMON MISTAKES TO AVOID
# ============================================================

# 1. Forgetting to return
def bad_add(a, b):
    result = a + b        # calculated but not returned!

print(bad_add(3, 4))      # None  <- bug!

def good_add(a, b):
    return a + b          # correct

# 2. Mutable default arguments (classic Python trap)
def bad_append(item, my_list=[]):   # NEVER use mutable default!
    my_list.append(item)
    return my_list

print(bad_append(1))      # [1]
print(bad_append(2))      # [1, 2]  <- unexpected! same list reused

def good_append(item, my_list=None):  # correct way
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(good_append(1))     # [1]
print(good_append(2))     # [2]  <- fresh list each time
