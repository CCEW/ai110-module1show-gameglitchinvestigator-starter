import sys
from pathlib import Path

# Ensure project root is on sys.path so logic_utils can be imported
sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess, parse_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_guess_with_secret_as_string():
    # Reproduce the bug: when the secret is stored as a string, comparisons should still work
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"

    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"

    outcome, message = check_guess(50, "50")
    assert outcome == "Win"


def test_negative_guess_is_too_low():
    outcome, message = check_guess(-10, 50)
    assert outcome == "Too Low"


def test_decimal_guess_parses_to_int():
    ok, guess_int, err = parse_guess("20.7")
    assert ok is True
    assert guess_int == 20
    assert err is None


def test_extremely_large_guess_is_too_high():
    outcome, message = check_guess(10**9, 50)
    assert outcome == "Too High"
