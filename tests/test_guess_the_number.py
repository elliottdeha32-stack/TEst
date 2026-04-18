"""Tests for guess_the_number module."""

from unittest.mock import patch

import pytest

import guess_the_number

# ---------------------------------------------------------------------------
# choose_difficulty
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("1", (10, 6)),
        ("2", (40, 7)),
        ("3", (100, 10)),
        ("4", (1000, 15)),
        ("", (40, 7)),  # default = "2"
    ],
)
def test_choose_difficulty_valid_choices(user_input: str, expected: tuple[int, int]) -> None:
    """Valid inputs (including empty for default) return the correct (max_num, max_guesses)."""
    with patch("builtins.input", return_value=user_input):
        result = guess_the_number.choose_difficulty()
    assert result == expected


def test_choose_difficulty_invalid_then_valid() -> None:
    """An invalid choice re-prompts until a valid one is entered."""
    inputs = iter(["5", "abc", "3"])
    with patch("builtins.input", side_effect=inputs):
        result = guess_the_number.choose_difficulty()
    assert result == (100, 10)


# ---------------------------------------------------------------------------
# play_round – win path
# ---------------------------------------------------------------------------


def test_play_round_win_first_guess() -> None:
    """Player wins on the first guess; returns (True, 1)."""
    with (
        patch("builtins.input", side_effect=["1", "7"]),  # difficulty=Easy, guess=7
        patch("random.randint", return_value=7),
    ):
        won, guesses = guess_the_number.play_round()

    assert won is True
    assert guesses == 1


def test_play_round_win_after_hints() -> None:
    """Player wins after receiving 'too low' / 'too high' hints."""
    # Easy difficulty (1-10), secret=5, guesses: 3 (low), 7 (high), 5 (correct)
    with (
        patch("builtins.input", side_effect=["1", "3", "7", "5"]),
        patch("random.randint", return_value=5),
    ):
        won, guesses = guess_the_number.play_round()

    assert won is True
    assert guesses == 3


# ---------------------------------------------------------------------------
# play_round – lose path
# ---------------------------------------------------------------------------


def test_play_round_loss_exhausts_guesses() -> None:
    """Player loses when all guesses are wrong; returns (False, None)."""
    # Easy: max_num=10, max_guesses=6, secret=5
    # Provide 6 wrong guesses (all too low)
    wrong_guesses = ["1"] * 6  # all guess "1"
    with (
        patch("builtins.input", side_effect=["1"] + wrong_guesses),  # "1" for difficulty
        patch("random.randint", return_value=10),
    ):
        won, guesses = guess_the_number.play_round()

    assert won is False
    assert guesses is None


def test_play_round_invalid_input_not_counted() -> None:
    """Non-integer input is rejected without consuming a guess attempt."""
    # Easy: max_guesses=6, secret=5
    # "abc" is invalid (not counted), then "5" wins
    with (
        patch("builtins.input", side_effect=["1", "abc", "5"]),
        patch("random.randint", return_value=5),
    ):
        won, guesses = guess_the_number.play_round()

    assert won is True
    assert guesses == 1


# ---------------------------------------------------------------------------
# main – play again loop
# ---------------------------------------------------------------------------


def test_main_play_once_then_quit(capsys: pytest.CaptureFixture[str]) -> None:
    """main() runs one round and exits cleanly when player answers 'n'."""
    # Difficulty=Easy, guess=7 (wins), then "n" to quit
    with (
        patch("builtins.input", side_effect=["1", "7", "n"]),
        patch("random.randint", return_value=7),
        patch("guess_the_number.startup_animation"),  # skip animation in tests
    ):
        guess_the_number.main()

    captured = capsys.readouterr()
    assert "Thanks for playing!" in captured.out


def test_main_best_score_updates(capsys: pytest.CaptureFixture[str]) -> None:
    """Best score is updated when a faster win is achieved."""
    # Round 1: Easy, win in 2 guesses (3 too low, then 7 correct)
    # Round 2: Easy, win in 1 guess (7 correct), then quit
    inputs = iter(
        [
            "1",
            "3",
            "7",  # round 1: difficulty, wrong guess, correct
            "y",  # play again
            "1",
            "7",  # round 2: difficulty, correct on first try
            "n",  # quit
        ]
    )
    with (
        patch("builtins.input", side_effect=inputs),
        patch("random.randint", side_effect=[7, 7]),
        patch("guess_the_number.startup_animation"),
    ):
        guess_the_number.main()

    captured = capsys.readouterr()
    assert "New best: 1 guesses!" in captured.out
