# ============================================================
# DAY 6 - Professional Python: errors, paths, data tools, types
# What was left after Days 1–5 (the "real project" layer)
# ============================================================


# ============================================================
# PART 1 - EXCEPTIONS (beyond try/except)
# ============================================================

# raise - you signal an error yourself
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b


# Custom exception - subclass Exception (or a built-in one)
class InsufficientBalanceError(Exception):
    """Raised when a withdrawal would go below zero."""

    pass


# Re-raising after logging / cleanup (preserve traceback with "raise" alone)
def risky():
    try:
        return 1 / 0
    except ZeroDivisionError:
        # log here in real code
        raise  # re-raise the same exception


# assert - for programmer checks (can be disabled with python -O)
# Use for invariants, not for user input validation
assert 2 + 2 == 4, "math broke"


# ============================================================
# PART 2 - pathlib — modern file paths (prefer over os.path)
# ============================================================

from pathlib import Path

# Current directory and home
here = Path.cwd()
home = Path.home()

# Build paths with / (works on Windows too)
data_dir = here / "data"
file_path = data_dir / "notes.txt"

# Create parents, write, read
data_dir.mkdir(parents=True, exist_ok=True)
file_path.write_text("hello from pathlib\n", encoding="utf-8")
text = file_path.read_text(encoding="utf-8")
print(text.strip())

print(file_path.suffix)   # .txt
print(file_path.stem)     # notes
print(file_path.exists())

# Iterate files in a folder
for p in sorted(data_dir.glob("*.txt")):
    print("  ", p.name)


# ============================================================
# PART 3 - csv module (proper CSV; not just split(","))
# ============================================================

import csv

csv_path = data_dir / "people.csv"
rows = [
    {"name": "Ali", "score": "88"},
    {"name": "Sara", "score": "95"},
]

with csv_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)

with csv_path.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['name']}: {row['score']}")


# ============================================================
# PART 4 - Regular expressions (re) — pattern matching in text
# ============================================================

import re

log_line = "2026-04-11 10:05:22 ERROR connection timeout"
# Groups in parentheses
m = re.search(r"(\d{4}-\d{2}-\d{2}).*(ERROR|WARN) (.+)", log_line)
if m:
    date, level, msg = m.groups()
    print(date, level, msg)

# findall - all emails in a blob
blob = "Contact a@x.com or b@y.org"
print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", blob))

# sub - replace
redacted = re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}", "****-****-****-****", "card 4111-1111-1111-1111")
print(redacted)


# ============================================================
# PART 5 - Type hints (annotations) — documentation + tooling
# ============================================================

from typing import Optional, List, Dict, Tuple


def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}\n") * times


def first_or_none(items: List[int]) -> Optional[int]:
    return items[0] if items else None


def scores_by_name(pairs: List[Tuple[str, int]]) -> Dict[str, int]:
    return {name: score for name, score in pairs}


print(greet("Python", 2))
print(first_or_none([1, 2, 3]))
print(scores_by_name([("Ali", 90), ("Sara", 95)]))


# ============================================================
# PART 6 - dataclasses — less boilerplate than manual __init__
# ============================================================

from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    done: bool = False
    tags: List[str] = field(default_factory=list)


t = Task("Review Day 6", tags=["python", "revision"])
t.done = True
print(t)


# ============================================================
# PART 7 - Generators (yield) — lazy sequences, memory-friendly
# ============================================================

def countdown(n: int):
    while n > 0:
        yield n
        n -= 1


print(list(countdown(3)))  # [3, 2, 1]

# Generator expression (like list comp but lazy)
squares_gen = (x * x for x in range(5))
print(next(squares_gen), next(squares_gen))  # 0, 1


# ============================================================
# PART 8 - Decorators — wrap functions to add behavior
# ============================================================

from functools import wraps
import time


def timed(fn):
    @wraps(fn)  # keeps original function name/docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{fn.__name__} took {elapsed:.4f}s")
        return result

    return wrapper


@timed
def slow_sum(n: int) -> int:
    time.sleep(0.05)
    return sum(range(n))


print(slow_sum(1000))


# ============================================================
# PART 9 - logging — production apps don't use print() everywhere
# ============================================================

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("day06")

log.debug("quiet detail")
log.info("something happened")
log.warning("this might be a problem")


# ============================================================
# PART 10 - collections — batteries for real data
# ============================================================

from collections import Counter, defaultdict, deque

# Counter - count hashable items
words = "to be or not to be".split()
print(Counter(words))  # Counter({'to': 2, 'be': 2, ...})

# defaultdict - missing keys get a default (e.g. empty list)
dd: Dict[str, List[str]] = defaultdict(list)
dd["fruits"].append("apple")
print(dict(dd))

# deque - fast append/pop from both ends (FIFO queues)
q: deque[int] = deque([1, 2, 3])
q.appendleft(0)
q.pop()
print(list(q))


# ============================================================
# QUICK SUMMARY — what Day 6 adds to your toolbox
# ============================================================

# | Topic        | Why it matters                                      |
# |--------------|-----------------------------------------------------|
# | raise/custom | Clear errors; APIs that fail predictably           |
# | pathlib      | Safe, readable paths on any OS                      |
# | csv          | Correct escaping for spreadsheets / exports         |
# | re           | Parse logs, validate formats, extract fields        |
# | type hints   | IDE help, fewer bugs, easier teamwork               |
# | dataclass    | Quick structured records without OOP ceremony       |
# | yield        | Large files/streams without loading all into RAM    |
# | decorators   | Cross-cutting concerns (timing, auth, caching)      |
# | logging      | Levels, filters, log files in real apps             |
# | collections  | Counter/defaultdict/deque for everyday algorithms   |
