# ============================================================
# DAY 4 - TUPLES, DICTIONARIES & SETS
# The data structures that power real Python applications
# ============================================================


# ============================================================
# PART 1 - TUPLES
# Like a list, but IMMUTABLE (cannot be changed after creation)
# ============================================================

# Creating tuples
coordinates = (10, 20)
rgb = (255, 128, 0)
single = (42,)          # IMPORTANT: comma needed for single item
empty = ()

print(type(coordinates))   # <class 'tuple'>

# Accessing - same as lists
point = (4, 7, 9)
print(point[0])     # 4
print(point[-1])    # 9
print(point[1:])    # (7, 9)

# Cannot modify - this would crash:
# point[0] = 10     # TypeError: tuple does not support item assignment

# Unpacking - assigning tuple values to variables
x, y = (10, 20)
print(x, y)         # 10  20

name, age, city = ("Ali", 20, "Karachi")
print(name, age, city)

# Swap variables using tuple unpacking (Python trick)
a, b = 5, 10
a, b = b, a         # no temp variable needed!
print(a, b)         # 10  5

# Functions returning multiple values return tuples
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

low, high, total = get_stats([3, 1, 9, 4, 7])
print(f"Min={low}, Max={high}, Sum={total}")

# Tuple methods
nums = (1, 2, 3, 2, 4, 2)
print(nums.count(2))   # 3  (how many times 2 appears)
print(nums.index(4))   # 4  (index of value 4)

# When to use tuple vs list?
# Tuple  → data that should NOT change (coordinates, RGB, DB records)
# List   → data that WILL change (shopping cart, student names)


# ============================================================
# PART 2 - DICTIONARIES
# Key-value pairs. The most important data structure in Python.
# ============================================================

# Creating a dictionary
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A",
    "city": "Karachi"
}

print(student)
print(type(student))   # <class 'dict'>

# Accessing values
print(student["name"])         # Ali
print(student.get("age"))      # 20
print(student.get("email"))    # None  (no error if key missing)
print(student.get("email", "Not provided"))  # default value

# Adding & updating
student["email"] = "ali@gmail.com"    # add new key
student["age"] = 21                   # update existing key
print(student)

# Deleting
del student["city"]                   # delete by key
removed = student.pop("grade")        # delete and return value
print(removed)                        # A
print(student)

# Checking if key exists
print("name" in student)              # True
print("phone" in student)             # False

# ---- Dictionary Methods ----

person = {"name": "Sara", "age": 25, "job": "Engineer"}

print(person.keys())      # dict_keys(['name', 'age', 'job'])
print(person.values())    # dict_values(['Sara', 25, 'Engineer'])
print(person.items())     # dict_items([('name', 'Sara'), ...])

# Looping over a dictionary
for key in person:
    print(key, "->", person[key])

# Better way - loop over items
for key, value in person.items():
    print(f"  {key}: {value}")

# Loop only values
for value in person.values():
    print(value)

# ---- Merging Dictionaries ----

defaults = {"color": "blue", "size": "M", "qty": 1}
order = {"color": "red", "qty": 3}

# update() - merges, order values override defaults
merged = {**defaults, **order}    # spread operator (Python 3.9+ also: defaults | order)
print(merged)   # {'color': 'red', 'size': 'M', 'qty': 3}

# ---- Nested Dictionaries ----

students = {
    "s001": {"name": "Ali",  "score": 88, "grade": "A"},
    "s002": {"name": "Sara", "score": 95, "grade": "A+"},
    "s003": {"name": "Umar", "score": 72, "grade": "B"},
}

# Access nested value
print(students["s002"]["name"])    # Sara
print(students["s001"]["score"])   # 88

# Loop nested dict
for student_id, info in students.items():
    print(f"{student_id}: {info['name']} scored {info['score']}")

# ---- Dictionary Comprehension ----

# Create dict from a list
names = ["Ali", "Sara", "Umar"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)    # {'Ali': 3, 'Sara': 4, 'Umar': 4}

# Filter a dict
scores = {"Ali": 88, "Sara": 45, "Umar": 72, "Zara": 39}
passed = {name: score for name, score in scores.items() if score >= 50}
print(passed)          # {'Ali': 88, 'Umar': 72}


# ============================================================
# PART 3 - SETS
# Unordered collection of UNIQUE items. No duplicates allowed.
# ============================================================

# Creating sets
fruits = {"apple", "banana", "cherry", "apple", "banana"}
print(fruits)          # {'apple', 'banana', 'cherry'} - duplicates removed!

numbers = {1, 2, 3, 4, 5}
empty_set = set()      # IMPORTANT: {} creates empty dict, not set!

# Adding & removing
fruits.add("mango")
fruits.remove("banana")     # raises KeyError if not found
fruits.discard("grape")     # safe - no error if not found
print(fruits)

# Checking membership (VERY fast compared to list)
print("apple" in fruits)    # True
print("grape" in fruits)    # False

# ---- Set Operations (most powerful feature) ----

python_devs = {"Ali", "Sara", "Umar", "Zara"}
java_devs   = {"Sara", "Umar", "John", "Mike"}

# Union - everyone in either set
print(python_devs | java_devs)
print(python_devs.union(java_devs))

# Intersection - only those in BOTH sets
print(python_devs & java_devs)            # {'Sara', 'Umar'}
print(python_devs.intersection(java_devs))

# Difference - in first set but NOT in second
print(python_devs - java_devs)            # {'Ali', 'Zara'}
print(python_devs.difference(java_devs))

# Symmetric difference - in either but NOT in both
print(python_devs ^ java_devs)            # {'Ali', 'Zara', 'John', 'Mike'}

# ---- Common Use Case: Remove duplicates from a list ----
raw = [1, 2, 3, 2, 4, 3, 5, 1, 6]
unique = list(set(raw))
print(unique)           # [1, 2, 3, 4, 5, 6] - order may vary

# ---- Subset & Superset ----
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))    # True  - all of a is in b
print(b.issuperset(a))  # True  - b contains all of a


# ============================================================
# COMPARISON TABLE
# ============================================================

# | Feature       | List      | Tuple     | Dict          | Set       |
# |---------------|-----------|-----------|---------------|-----------|
# | Ordered       | Yes       | Yes       | Yes (3.7+)    | No        |
# | Mutable       | Yes       | No        | Yes           | Yes       |
# | Duplicates    | Yes       | Yes       | Keys: No      | No        |
# | Access by     | Index     | Index     | Key           | -         |
# | Use for       | Collection| Fixed data| Key-value     | Unique    |
# | Syntax        | [1,2,3]   | (1,2,3)   | {"k":"v"}     | {1,2,3}   |
