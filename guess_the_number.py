"""Guess the Number - simple terminal game

Run: python3 guess_the_number.py
"""
import random


def choose_difficulty():
    choices = {
        "1": (10, 6),   # (max_number, max_guesses)
        "2": (50, 7),
        "3": (100, 10),
    }
    print("Choose difficulty:")
    print("  1) Easy   (1-10, 6 guesses)")
    print("  2) Medium (1-50, 7 guesses)")
    print("  3) Hard   (1-100, 10 guesses)")
    while True:
        choice = input("Select 1, 2 or 3 (default 2): ").strip() or "2"
        if choice in choices:
            return choices[choice]
        print("Please enter 1, 2 or 3.")


def play_round():
    max_num, max_guesses = choose_difficulty()
    secret = random.randint(1, max_num)
    print(f"I'm thinking of a number between 1 and {max_num}.")
    guesses = 0

    while guesses < max_guesses:
        remaining = max_guesses - guesses
        try:
            guess = int(input(f"Guess ({remaining} left): "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        guesses += 1

        if guess == secret:
            print(f"Correct! You found it in {guesses} guess{'es' if guesses!=1 else ''}.")
            return True, guesses
        if guess < secret:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Out of guesses! The number was {secret}.")
    return False, None


def main():
    print("--- Guess the Number ---")
    best = None
    while True:
        won, guesses = play_round()
        if won:
            if best is None or guesses < best:
                best = guesses
                print(f"New best: {best} guesses!")
        again = input("Play again? (y/n): ").strip().lower()
        if not again or again[0] != 'y':
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()
