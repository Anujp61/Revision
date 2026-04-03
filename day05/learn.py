# ============================================================
# DAY 5 - FILE I/O, MODULES & OBJECT-ORIENTED PROGRAMMING
# The three pillars you need to build real Python applications
# ============================================================


# ============================================================
# PART 1 - FILE I/O
# Reading and writing files is how programs persist data
# ============================================================

# ---- Writing to a file ----

# open(filename, mode)
# Modes: "r" = read, "w" = write, "a" = append, "r+" = read+write
# "w" creates file if it doesn't exist, OVERWRITES if it does

file = open("sample.txt", "w")
file.write("Hello, World!\n")
file.write("Python is awesome.\n")
file.write("This is line 3.\n")
file.close()    # ALWAYS close the file when done

# ---- Reading a file ----

file = open("sample.txt", "r")
content = file.read()       # reads ENTIRE file as one string
print(content)
file.close()

# Read line by line
file = open("sample.txt", "r")
for line in file:
    print(line.strip())     # strip() removes the trailing \n
file.close()

# Read all lines into a list
file = open("sample.txt", "r")
lines = file.readlines()    # ['Hello, World!\n', 'Python is ...']
print(lines)
file.close()

# ---- THE "with" STATEMENT (BEST PRACTICE) ----
# Automatically closes the file even if an error occurs

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
# file is auto-closed here - no need for file.close()

# ---- Appending to a file ----
# "a" mode adds to the END without erasing existing content

with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")
    file.write("And this one too.\n")

# ---- Writing multiple lines at once ----

lines_to_write = ["Line A\n", "Line B\n", "Line C\n"]
with open("output.txt", "w") as file:
    file.writelines(lines_to_write)

# ---- Check if file exists before reading ----

import os

if os.path.exists("sample.txt"):
    with open("sample.txt", "r") as f:
        print(f.read())
else:
    print("File not found!")

# ---- Working with CSV-style data ----

students = [
    ("Ali", 88, "A"),
    ("Sara", 95, "A+"),
    ("Umar", 72, "B"),
]

with open("students.csv", "w") as f:
    f.write("Name,Score,Grade\n")
    for name, score, grade in students:
        f.write(f"{name},{score},{grade}\n")

with open("students.csv", "r") as f:
    header = f.readline().strip()
    print(header)
    for line in f:
        name, score, grade = line.strip().split(",")
        print(f"  {name} scored {score} ({grade})")


# ============================================================
# PART 2 - MODULES & IMPORTS
# Modules let you organize code and use other people's code
# ============================================================

# ---- Importing built-in modules ----

import math
print(math.pi)              # 3.141592653589793
print(math.sqrt(144))       # 12.0
print(math.ceil(4.2))       # 5
print(math.floor(4.9))      # 4
print(math.factorial(5))    # 120

# Import specific things
from math import pi, sqrt
print(pi)                   # no need for math.pi
print(sqrt(81))             # 9.0

# Import with alias
import random as rnd
print(rnd.randint(1, 100))
print(rnd.choice(["apple", "banana", "cherry"]))

# ---- datetime module ----

from datetime import datetime, timedelta

now = datetime.now()
print(now)                           # 2026-04-03 19:30:00.123456
print(now.strftime("%d/%m/%Y"))      # 03/04/2026
print(now.strftime("%I:%M %p"))      # 07:30 PM

tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%A, %d %B %Y')}")

# ---- json module ----

import json

data = {"name": "Ali", "age": 20, "skills": ["Python", "JS"]}

json_string = json.dumps(data, indent=2)
print(json_string)

parsed = json.loads(json_string)
print(parsed["name"])               # Ali

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded)

# ---- Creating your own module ----
# Any .py file is a module. If you have utils.py with:
#     def greet(name):
#         return f"Hello, {name}"
#
# Then in another file:
#     from utils import greet
#     print(greet("Ali"))

# ---- __name__ == "__main__" explained ----
# When you run a file directly: __name__ is "__main__"
# When you import it: __name__ is the module name
# This lets you have code that only runs when file is executed directly

def main():
    print("This runs only when you execute this file directly")

if __name__ == "__main__":
    main()


# ============================================================
# PART 3 - OBJECT-ORIENTED PROGRAMMING (OOP)
# The paradigm used in every large Python project
# ============================================================

# ---- What is OOP? ----
# Instead of functions + data separately, OOP bundles them together
# Class = blueprint,  Object = instance built from that blueprint

# ---- Defining a class ----

class Dog:
    species = "Canine"     # CLASS variable - shared by all dogs

    def __init__(self, name, breed, age):
        # INSTANCE variables - unique to each dog
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"


# Creating objects (instances)
dog1 = Dog("Bruno", "Labrador", 3)
dog2 = Dog("Max", "German Shepherd", 5)

print(dog1.bark())          # Bruno says: Woof!
print(dog2.describe())      # Max is a 5-year-old German Shepherd
print(Dog.species)          # Canine (accessed via class)
print(dog1.species)         # Canine (also works via instance)


# ---- __init__ is the constructor ----
# Runs automatically when you create an object
# "self" refers to the object being created

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.balance += amount
        self.transactions.append(f"+{amount}")
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Balance: {self.balance}")
            return
        self.balance -= amount
        self.transactions.append(f"-{amount}")
        print(f"Withdrew {amount}. Balance: {self.balance}")

    def get_statement(self):
        print(f"\n  Account: {self.owner}")
        print(f"  Balance: {self.balance}")
        print(f"  Transactions: {', '.join(self.transactions)}")


acc = BankAccount("Ali", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.get_statement()


# ============================================================
# DUNDER (MAGIC) METHODS
# Special methods that Python calls behind the scenes
# ============================================================

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        """Called by print() and str()"""
        return f"{self.name}: Rs.{self.price}"

    def __repr__(self):
        """Called in the console / debugging"""
        return f"Product('{self.name}', {self.price})"

    def __eq__(self, other):
        """Called by == operator"""
        return self.name == other.name and self.price == other.price

    def __lt__(self, other):
        """Called by < operator (enables sorting)"""
        return self.price < other.price

    def __add__(self, other):
        """Called by + operator"""
        return self.price + other.price


p1 = Product("Laptop", 150000)
p2 = Product("Phone", 80000)
p3 = Product("Laptop", 150000)

print(p1)              # Laptop: Rs.150000  (uses __str__)
print(repr(p2))        # Product('Phone', 80000)  (uses __repr__)
print(p1 == p3)        # True   (uses __eq__)
print(p1 + p2)         # 230000 (uses __add__)

products = [p1, p2, Product("Mouse", 2000)]
products.sort()        # uses __lt__
for p in products:
    print(f"  {p}")


# ============================================================
# INHERITANCE
# Create new classes based on existing ones
# ============================================================

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return f"Animal({self.name})"


class Cat(Animal):     # Cat INHERITS from Animal
    def __init__(self, name, color):
        super().__init__(name, "Meow")   # call parent's __init__
        self.color = color

    def purr(self):
        return f"{self.name} purrs..."


class DogPet(Animal):
    def __init__(self, name, tricks=None):
        super().__init__(name, "Woof")
        self.tricks = tricks or []

    def learn_trick(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        if self.tricks:
            return f"{self.name} knows: {', '.join(self.tricks)}"
        return f"{self.name} doesn't know any tricks yet"


cat = Cat("Whiskers", "orange")
dog = DogPet("Buddy")

print(cat.speak())          # Whiskers says Meow!  (inherited method)
print(cat.purr())           # Whiskers purrs...    (own method)
print(cat.color)            # orange               (own attribute)

dog.learn_trick("sit")
dog.learn_trick("shake")
print(dog.show_tricks())    # Buddy knows: sit, shake

# isinstance() checks if object is of a certain class
print(isinstance(cat, Cat))      # True
print(isinstance(cat, Animal))   # True (Cat IS an Animal)
print(isinstance(cat, DogPet))   # False


# ============================================================
# POLYMORPHISM
# Same method name, different behavior in different classes
# ============================================================

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

    def __str__(self):
        return f"{self.__class__.__name__}: area = {self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print(shape)    # each calls its OWN area() method


# ============================================================
# ENCAPSULATION
# Controlling access to data inside a class
# ============================================================

class Employee:
    def __init__(self, name, salary):
        self.name = name            # public
        self._department = ""       # "protected" (convention: don't touch from outside)
        self.__salary = salary      # "private" (name mangling: can't access directly)

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary < 0:
            print("Salary cannot be negative")
            return
        self.__salary = new_salary

    @property
    def salary(self):
        """Property lets you access like an attribute but with control"""
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value


emp = Employee("Ali", 50000)
print(emp.name)                # Ali (public - OK)
print(emp.salary)              # 50000 (using @property)
emp.salary = 60000             # using @salary.setter
print(emp.salary)              # 60000

# emp.__salary                 # AttributeError! can't access directly
# emp._Employee__salary        # technically works (name mangling) but DON'T


# ============================================================
# CLASS METHODS & STATIC METHODS
# ============================================================

class Student:
    school = "Python Academy"    # class variable
    count = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.count += 1

    def describe(self):
        """Regular method - needs self (instance)"""
        return f"{self.name} (Grade {self.grade}) at {self.school}"

    @classmethod
    def change_school(cls, new_school):
        """Class method - gets class (cls) instead of instance"""
        cls.school = new_school

    @classmethod
    def from_string(cls, data_string):
        """Alternative constructor - creates Student from a string"""
        name, grade = data_string.split(",")
        return cls(name.strip(), grade.strip())

    @staticmethod
    def is_passing(grade):
        """Static method - no self or cls, just a utility function"""
        return grade in ("A+", "A", "B", "C")


s1 = Student("Ali", "A")
s2 = Student.from_string("Sara, A+")     # using classmethod as constructor

print(s1.describe())
print(s2.describe())
print(f"Total students: {Student.count}")

Student.change_school("Code Academy")
print(s1.describe())        # school changed for ALL students

print(Student.is_passing("A"))    # True
print(Student.is_passing("F"))    # False


# ============================================================
# COMPOSITION - CLASSES USING OTHER CLASSES
# (Often better than inheritance: "has-a" vs "is-a")
# ============================================================

class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def __str__(self):
        return f"{self.horsepower}HP {self.fuel_type}"

class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine       # Car HAS-A Engine (composition)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.engine})"


engine = Engine(200, "Petrol")
car = Car("Toyota", "Corolla", engine)
print(car)     # Toyota Corolla (200HP Petrol)


# ============================================================
# QUICK SUMMARY
# ============================================================

# | Concept         | What it does                                   |
# |-----------------|------------------------------------------------|
# | File I/O        | Read/write data to files on disk               |
# | with statement  | Auto-closes files, prevents resource leaks     |
# | Modules         | Organize & reuse code across files              |
# | Class           | Blueprint for creating objects                  |
# | __init__        | Constructor - runs when object is created       |
# | self            | Reference to the current instance               |
# | Inheritance     | Child class gets parent's attributes & methods  |
# | super()         | Call parent's methods from child                |
# | Polymorphism    | Same method name, different behavior            |
# | Encapsulation   | Hide internal data, expose through methods      |
# | @property       | Access methods like attributes                  |
# | @classmethod    | Method that works on the class, not instance    |
# | @staticmethod   | Utility function that lives in a class          |
# | Composition     | Classes containing other classes (has-a)        |
