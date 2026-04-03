# ============================================================
# DAY 1 PROJECT - Number Guessing Game
# Uses: variables, data types, input, type conversion, operators
# ============================================================

import random   # built-in module to generate random numbers

# --- Game Setup ---
secret_number = random.randint(1, 100)   # random int between 1 and 100
max_attempts = 7
attempts_used = 0
has_won = False

# --- Game Info ---
print("=" * 40)
print("   WELCOME TO THE NUMBER GUESSING GAME")
print("=" * 40)
print(f"I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts. Good luck!\n")

# --- Game Loop ---
while attempts_used < max_attempts:
    attempts_left = max_attempts - attempts_used

    # Get guess from user and convert to integer
    guess_str = input(f"Attempt {attempts_used + 1}/{max_attempts} - Enter your guess: ")
    guess = int(guess_str)
    attempts_used = attempts_used + 1

    # Check the guess
    if guess == secret_number:
        has_won = True
        break
    elif guess < secret_number:
        diff = secret_number - guess
        if diff > 20:
            print("Too low! Way off.\n")
        else:
            print("Too low! Getting warmer.\n")
    else:
        diff = guess - secret_number
        if diff > 20:
            print("Too high! Way off.\n")
        else:
            print("Too high! Getting warmer.\n")

# --- Result ---
print("-" * 40)
if has_won:
    print(f"CORRECT! The number was {secret_number}!")
    print(f"You got it in {attempts_used} attempt(s).")

    # Score calculation
    score = round((attempts_left / max_attempts) * 100)
    print(f"Your score: {score}/100")

    if attempts_used == 1:
        print("UNBELIEVABLE! First try!")
    elif attempts_used <= 3:
        print("Excellent guessing!")
    else:
        print("Well done!")
else:
    print(f"GAME OVER! The number was {secret_number}.")
    print("Better luck next time!")

print("=" * 40)
