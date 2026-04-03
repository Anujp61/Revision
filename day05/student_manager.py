# ============================================================
# DAY 5 PROJECT - Student Management System
# Uses: OOP (classes, inheritance, dunder methods, @property,
#       @classmethod), File I/O (JSON), modules, composition
# ============================================================

import json
import os
from datetime import datetime


# ============================================================
# MODEL CLASSES
# ============================================================

class Student:
    """Represents a single student."""

    def __init__(self, name, roll_no, marks=None):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks or {}

    @property
    def average(self):
        if not self.marks:
            return 0
        return round(sum(self.marks.values()) / len(self.marks), 2)

    @property
    def grade(self):
        avg = self.average
        if avg >= 90: return "A+"
        if avg >= 80: return "A"
        if avg >= 70: return "B"
        if avg >= 60: return "C"
        if avg >= 50: return "D"
        return "F"

    @property
    def passed(self):
        return self.average >= 50

    def add_marks(self, subject, score):
        if not 0 <= score <= 100:
            print("  Score must be between 0 and 100")
            return False
        self.marks[subject] = score
        return True

    def to_dict(self):
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "marks": self.marks,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["roll_no"], data.get("marks", {}))

    def __str__(self):
        status = "PASS" if self.passed else "FAIL"
        return f"{self.roll_no} | {self.name:<20} | Avg: {self.average:6.2f} | {self.grade} | {status}"

    def __repr__(self):
        return f"Student('{self.name}', '{self.roll_no}')"

    def __eq__(self, other):
        return self.roll_no == other.roll_no

    def __lt__(self, other):
        return self.average > other.average     # sort by highest avg first


# ============================================================
# DATABASE CLASS (File I/O + dict of Student objects)
# ============================================================

class StudentDatabase:
    """Manages loading, saving, and querying students."""

    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}
        self.load()

    def load(self):
        if not os.path.exists(self.filename):
            self.students = {}
            return
        with open(self.filename, "r") as f:
            raw = json.load(f)
        self.students = {
            roll: Student.from_dict(data) for roll, data in raw.items()
        }
        print(f"  Loaded {len(self.students)} student(s) from {self.filename}")

    def save(self):
        data = {roll: s.to_dict() for roll, s in self.students.items()}
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def add_student(self, student):
        if student.roll_no in self.students:
            print(f"  Roll #{student.roll_no} already exists!")
            return False
        self.students[student.roll_no] = student
        self.save()
        print(f"  Added: {student.name} (#{student.roll_no})")
        return True

    def remove_student(self, roll_no):
        if roll_no not in self.students:
            print(f"  Roll #{roll_no} not found.")
            return False
        name = self.students.pop(roll_no).name
        self.save()
        print(f"  Removed: {name} (#{roll_no})")
        return True

    def get_student(self, roll_no):
        return self.students.get(roll_no)

    def search(self, query):
        query = query.lower()
        return [
            s for s in self.students.values()
            if query in s.name.lower() or query in s.roll_no.lower()
        ]

    def get_rankings(self):
        return sorted(self.students.values())   # uses __lt__

    def get_stats(self):
        if not self.students:
            return None
        all_students = list(self.students.values())
        averages = [s.average for s in all_students]
        passed = sum(1 for s in all_students if s.passed)
        return {
            "total": len(all_students),
            "passed": passed,
            "failed": len(all_students) - passed,
            "pass_rate": round(passed / len(all_students) * 100, 1),
            "highest_avg": max(averages),
            "lowest_avg": min(averages),
            "class_avg": round(sum(averages) / len(averages), 2),
            "topper": max(all_students, key=lambda s: s.average).name,
        }


# ============================================================
# UI / MENU SYSTEM
# ============================================================

def get_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("  This field is required.")


def show_menu():
    print("\n" + "=" * 50)
    print("         STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("  1. Add student")
    print("  2. View student")
    print("  3. Add marks")
    print("  4. Search students")
    print("  5. Rankings")
    print("  6. Class statistics")
    print("  7. List all students")
    print("  8. Remove student")
    print("  0. Exit")
    print("-" * 50)


def handle_add(db):
    name = get_input("  Name: ")
    roll_no = get_input("  Roll No: ")
    student = Student(name, roll_no)

    print("  Enter marks (leave subject blank to stop):")
    while True:
        subject = input("    Subject: ").strip()
        if not subject:
            break
        try:
            score = float(input(f"    {subject} score: "))
            student.add_marks(subject, score)
        except ValueError:
            print("    Invalid score, skipping.")

    db.add_student(student)


def handle_view(db):
    roll = get_input("  Roll No: ")
    student = db.get_student(roll)
    if not student:
        print(f"  Student #{roll} not found.")
        return

    print(f"\n  {'='*40}")
    print(f"  Name:    {student.name}")
    print(f"  Roll:    {student.roll_no}")
    print(f"  Average: {student.average}")
    print(f"  Grade:   {student.grade}")
    print(f"  Status:  {'PASS' if student.passed else 'FAIL'}")
    if student.marks:
        print(f"  {'-'*40}")
        print(f"  {'Subject':<15} {'Score':>6}")
        print(f"  {'-'*40}")
        for subject, score in student.marks.items():
            print(f"  {subject:<15} {score:>6.1f}")
    print(f"  {'='*40}")


def handle_add_marks(db):
    roll = get_input("  Roll No: ")
    student = db.get_student(roll)
    if not student:
        print(f"  Student #{roll} not found.")
        return

    print(f"  Adding marks for {student.name}:")
    while True:
        subject = input("    Subject (blank to stop): ").strip()
        if not subject:
            break
        try:
            score = float(input(f"    {subject} score: "))
            student.add_marks(subject, score)
        except ValueError:
            print("    Invalid score.")

    db.save()
    print(f"  Marks updated. New average: {student.average} ({student.grade})")


def handle_search(db):
    query = get_input("  Search (name or roll): ")
    results = db.search(query)
    if not results:
        print("  No students found.")
        return
    print(f"\n  Found {len(results)} student(s):")
    for s in results:
        print(f"  {s}")


def handle_rankings(db):
    ranked = db.get_rankings()
    if not ranked:
        print("  No students yet.")
        return
    print(f"\n  {'Rank':<6} {'Roll':<8} {'Name':<20} {'Avg':>6}  Grade")
    print("  " + "-" * 50)
    for i, s in enumerate(ranked, 1):
        print(f"  {i:<6} {s.roll_no:<8} {s.name:<20} {s.average:>6.2f}  {s.grade}")


def handle_stats(db):
    stats = db.get_stats()
    if not stats:
        print("  No students yet.")
        return
    print(f"\n  {'='*35}")
    print(f"  Total Students:  {stats['total']}")
    print(f"  Passed:          {stats['passed']}")
    print(f"  Failed:          {stats['failed']}")
    print(f"  Pass Rate:       {stats['pass_rate']}%")
    print(f"  Class Average:   {stats['class_avg']}")
    print(f"  Highest Average: {stats['highest_avg']}")
    print(f"  Lowest Average:  {stats['lowest_avg']}")
    print(f"  Topper:          {stats['topper']}")
    print(f"  {'='*35}")


def handle_list_all(db):
    if not db.students:
        print("  No students yet.")
        return
    print(f"\n  {'Roll':<8} {'Name':<20} {'Avg':>6}  Grade  Status")
    print("  " + "-" * 55)
    for s in sorted(db.students.values(), key=lambda x: x.name):
        status = "PASS" if s.passed else "FAIL"
        print(f"  {s.roll_no:<8} {s.name:<20} {s.average:>6.2f}  {s.grade:<6} {status}")


def seed_demo_data(db):
    """Load demo data so you can test right away."""
    demos = [
        Student("Ali Khan",    "R001", {"Math": 88, "Physics": 92, "English": 78}),
        Student("Sara Ahmed",  "R002", {"Math": 95, "Physics": 90, "English": 94}),
        Student("Umar Farooq", "R003", {"Math": 55, "Physics": 48, "English": 62}),
        Student("Zara Malik",  "R004", {"Math": 72, "Physics": 68, "English": 75}),
        Student("John Smith",  "R005", {"Math": 40, "Physics": 35, "English": 45}),
    ]
    for s in demos:
        if s.roll_no not in db.students:
            db.students[s.roll_no] = s
    db.save()
    print("  Demo data loaded.\n")


# ============================================================
# MAIN
# ============================================================

def main():
    print("\n  Welcome to the Student Management System!")
    print(f"  Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}\n")

    db = StudentDatabase()

    if not db.students:
        seed_demo_data(db)

    while True:
        show_menu()
        choice = input("  Choose: ").strip()

        if choice == "0":
            print("\n  Goodbye! Data saved automatically.")
            break
        elif choice == "1":
            handle_add(db)
        elif choice == "2":
            handle_view(db)
        elif choice == "3":
            handle_add_marks(db)
        elif choice == "4":
            handle_search(db)
        elif choice == "5":
            handle_rankings(db)
        elif choice == "6":
            handle_stats(db)
        elif choice == "7":
            handle_list_all(db)
        elif choice == "8":
            roll = get_input("  Roll No to remove: ")
            db.remove_student(roll)
        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    main()
