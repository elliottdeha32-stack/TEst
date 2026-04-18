"""Guess the Number - simple terminal game

Run: python3 guess_the_number.py
"""
import random
import time


def startup_animation():
    banner = r"""
  ____                       _   _            _   _                 _
 / ___|_   _  ___  ___ ___  | |_| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __
| |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |
 \____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|
"""
    separators = ["★  ★  ★  ★  ★  ★  ★  ★  ★  ★  ★  ★", "~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~"]
    title = "       🎯  GUESS THE NUMBER  🎯"
    subtitle = "   Can YOU find the secret number in time?"

    # Print banner letter by letter
    print()
    for char in banner:
        print(char, end='', flush=True)
        time.sleep(0.01)

    time.sleep(0.3)

    # Animated separator
    for char in separators[0]:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

    # Animated title — slower for dramatic effect
    print()
    for char in title:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

    # Animated subtitle — slower for dramatic effect
    for char in subtitle:
        print(char, end='', flush=True)
        time.sleep(0.08)
    print()

    time.sleep(0.3)
    for char in separators[1]:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\n")

    # Suspenseful countdown
    for i in range(3, 0, -1):
        print(f"  ⏳  Starting in {i}...", end='\r', flush=True)
        time.sleep(1.0)
    print("  🚀  Get ready!             ")
    time.sleep(0.6)
    print()


def choose_difficulty():
    choices = {
        "1": (10, 6),   # (max_number, max_guesses)
        "2": (40, 7),
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
    startup_animation()
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
