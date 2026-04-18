"""Guess the Number - simple terminal game

Run: python3 guess_the_number.py
"""
import random


def choose_difficulty():
    """Prompt the player to select a difficulty level.

    Each level is a tuple of (max_number, max_guesses).
    Returns the chosen (max_number, max_guesses) pair.
    """
    # Map option key -> (upper bound of secret number, allowed guesses)
    choices = {
        "1": (10, 6),    # Easy:    small range, few guesses
        "2": (40, 7),    # Medium:  moderate range and guesses (default)
        "3": (100, 10),  # Hard:    wider range, more guesses needed
        "4": (1000, 15), # Extreme: very wide range, maximum challenge
    }
    print("Choose difficulty:")
    print("  1) Easy    (1-10,   6 guesses)")
    print("  2) Medium  (1-50,   7 guesses)")
    print("  3) Hard    (1-100, 10 guesses)")
    print("  4) Extreme (1-1000, 15 guesses)")
    while True:
        choice = input("Select 1, 2, 3 or 4 (default 2): ").strip() or "2"
        if choice in choices:
            return choices[choice]
        print("Please enter 1, 2, 3 or 4.")


def play_round():
    """Run a single round of the game.

    Returns:
        (won, guesses): won is True if the player guessed correctly,
                        guesses is the number of attempts used (or None on loss).
    """
    max_num, max_guesses = choose_difficulty()

    # Pick a random secret number within the difficulty range
    secret = random.randint(1, max_num)
    print(f"I'm thinking of a number between 1 and {max_num}.")
    guesses = 0

    while guesses < max_guesses:
        remaining = max_guesses - guesses
        try:
            guess = int(input(f"Guess ({remaining} left): "))
        except ValueError:
            # Re-prompt without counting the invalid attempt
            print("Please enter a whole number.")
            continue
        guesses += 1

        if guess == secret:
            print(f"Correct! You found it in {guesses} guess{'es' if guesses!=1 else ''}.")
            return True, guesses
        # Give a directional hint so the player can narrow down the range
        if guess < secret:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Out of guesses! The number was {secret}.")
    return False, None


def main():
    """Entry point: loop through rounds and track the player's best score."""
    print("--- Guess the Number ---")
    best = None  # Fewest guesses used to win across all rounds
    while True:
        won, guesses = play_round()
        if won:
            # Update best score if this round was faster
            if best is None or guesses < best:
                best = guesses
                print(f"New best: {best} guesses!")
        again = input("Play again? (y/n): ").strip().lower()
        if not again or again[0] != 'y':
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()
