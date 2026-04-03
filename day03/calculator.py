# ============================================================
# DAY 3 PROJECT - Scientific Calculator
# Uses: functions, default params, *args, input validation,
#       functions calling functions, lambda
# ============================================================


# ============================================================
# CORE MATH FUNCTIONS
# ============================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(base, exp=2):
    return base ** exp

def modulus(a, b):
    if b == 0:
        return "Error: Cannot mod by zero"
    return a % b

def square_root(n):
    if n < 0:
        return "Error: Cannot square root a negative number"
    return n ** 0.5


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a number.")

def format_result(result):
    """Format result: show int if whole number, else 6 decimal places."""
    if isinstance(result, str):    # it's an error message
        return result
    if result == int(result):
        return int(result)
    return round(result, 6)

def show_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 40)
    print("       SCIENTIFIC CALCULATOR")
    print("=" * 40)
    print("  1. Add           (+)")
    print("  2. Subtract       (-)")
    print("  3. Multiply       (*)")
    print("  4. Divide         (/)")
    print("  5. Power          (^)")
    print("  6. Modulus        (%)")
    print("  7. Square Root    (√)")
    print("  8. History")
    print("  0. Exit")
    print("-" * 40)


# ============================================================
# HISTORY TRACKER
# ============================================================

history = []   # list to store past calculations

def add_to_history(expression, result):
    history.append(f"{expression} = {result}")
    if len(history) > 10:      # keep only last 10
        history.pop(0)

def show_history():
    if not history:
        print("  No calculations yet.")
        return
    print("\n  --- Last Calculations ---")
    for i, entry in enumerate(history, 1):
        print(f"  {i}. {entry}")


# ============================================================
# OPERATIONS DISPATCHER
# ============================================================

# Map choice to function using a dictionary of lambdas
operations = {
    "1": lambda a, b: (f"{a} + {b}", add(a, b)),
    "2": lambda a, b: (f"{a} - {b}", subtract(a, b)),
    "3": lambda a, b: (f"{a} * {b}", multiply(a, b)),
    "4": lambda a, b: (f"{a} / {b}", divide(a, b)),
    "5": lambda a, b: (f"{a} ^ {b}", power(a, b)),
    "6": lambda a, b: (f"{a} % {b}", modulus(a, b)),
}

def run_two_operand(choice):
    """Handle operations that need two numbers."""
    a = get_number("  Enter first number:  ")
    b = get_number("  Enter second number: ")
    expression, result = operations[choice](a, b)
    formatted = format_result(result)
    print(f"\n  Result: {expression} = {formatted}")
    add_to_history(expression, formatted)

def run_square_root():
    """Handle square root (only needs one number)."""
    n = get_number("  Enter number: ")
    result = square_root(n)
    formatted = format_result(result)
    expression = f"√{n}"
    print(f"\n  Result: {expression} = {formatted}")
    add_to_history(expression, formatted)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    print("\nWelcome to the Scientific Calculator!")

    while True:
        show_menu()
        choice = input("  Choose an option: ").strip()

        if choice == "0":
            print("\nGoodbye! Thanks for using the calculator.")
            break
        elif choice in ("1", "2", "3", "4", "5", "6"):
            run_two_operand(choice)
        elif choice == "7":
            run_square_root()
        elif choice == "8":
            show_history()
        else:
            print("  Invalid choice. Please enter 0-8.")

# This is the standard Python entry point pattern
# Code inside only runs when this file is run directly
# (not when imported as a module - you'll learn this on Day 5)
if __name__ == "__main__":
    main()
