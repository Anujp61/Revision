# ============================================================
# DAY 1 - Variables, Data Types, Input/Output
# ============================================================

# --- VARIABLES ---
# A variable stores a value. No need to declare type.
name = "Aakas"
age = 20
height = 5.9
is_student = True

print(type(name))
print(age)
print(height)
print(is_student)

# Python figures out the type automatically
# This is called "dynamic typing"

# --- NAMING RULES ---
# good names (snake_case is Python standard)
first_name = "Ali"
total_marks = 95
is_logged_in = False

# bad names (avoid these)
# 2name = "bad"       <- can't start with a number
# my-name = "bad"     <- no hyphens allowed
# class = "bad"       <- 'class' is a reserved keyword


# ============================================================
# DATA TYPES
# ============================================================

# 1. INTEGER - whole numbers
score = 100
temperature = -5
year = 2026

# 2. FLOAT - decimal numbers
pi = 3.14159
price = 19.99
gpa = 3.75

# 3. STRING - text, wrapped in quotes
greeting = "Hello, World!"
language = 'Python'          # single or double quotes, both work
multiline = """This is
a multiline
string"""

# 4. BOOLEAN - True or False (capital T and F)
is_raining = False
has_passed = True

# 5. None - represents "nothing" / empty value
result = None


# ============================================================
# type() - CHECK WHAT TYPE A VARIABLE IS
# ============================================================

print(type(score))        # <class 'int'>
print(type(price))        # <class 'float'>
print(type(greeting))     # <class 'str'>
print(type(is_raining))   # <class 'bool'>
print(type(result))       # <class 'NoneType'>


# ============================================================
# TYPE CONVERSION - converting between types
# ============================================================

# str -> int
num_str = "42"
num_int = int(num_str)
print(num_int + 8)        # 50

# int -> float
x = float(10)
print(x)                  # 10.0

# int -> str
age_str = str(25)
print("I am " + age_str + " years old")

# float -> int (WARNING: cuts off decimal, does NOT round)
pi_int = int(3.99)
print(pi_int)             # 3  <-- not 4!


# ============================================================
# INPUT / OUTPUT
# ============================================================

# print() - output to screen
print("Hello!")                         # simple string
print("Name:", name, "Age:", age)       # multiple values
print(f"My name is {name} and I am {age} years old")   # f-string (best way)

# f-strings let you embed variables directly inside strings
city = "Karachi"
population = 16_000_000    # underscores make big numbers readable
print(f"{city} has a population of {population:,}")    # comma formatting

# input() - get input from user (ALWAYS returns a string)
# user_name = input("What is your name? ")
# print(f"Hello, {user_name}!")

# To get a number from user you must convert:
# user_age = int(input("How old are you? "))
# print(f"In 10 years you will be {user_age + 10}")


# ============================================================
# ARITHMETIC OPERATORS
# ============================================================

a = 17
b = 5

print(a + b)    # 22  - addition
print(a - b)    # 12  - subtraction
print(a * b)    # 85  - multiplication
print(a / b)    # 3.4 - division (always gives float)
print(a // b)   # 3   - floor division (cuts decimal)
print(a % b)    # 2   - modulus (remainder)
print(a ** b)   # 1419857 - exponent (17 to the power 5)


# ============================================================
# USEFUL BUILT-IN FUNCTIONS
# ============================================================

print(abs(-45))          # 45  - absolute value
print(round(3.7))        # 4   - rounds to nearest int
print(round(3.14159, 2)) # 3.14 - round to 2 decimal places
print(max(4, 7, 2, 9))   # 9   - maximum value
print(min(4, 7, 2, 9))   # 2   - minimum value
