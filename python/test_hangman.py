from wordguess import Wordguess


def test_wordguess_creation():
    game = Wordguess("PYTHON")
    assert game.word == "PYTHON"
    assert game.guessed_letters == set()
    assert game.max_attempts == 6
    assert game.wrong_guesses == 0


def test_make_guess_correct():
    game = Wordguess("PYTHON")
    result = game.make_guess("P")
    assert "Good guess" in result
    assert "P" in game.guessed_letters


def test_make_guess_wrong():
    game = Wordguess("PYTHON")
    result = game.make_guess("Z")
    assert "Sorry" in result
    assert game.wrong_guesses == 1


def test_is_won():
    game = Wordguess("HI")
    game.make_guess("H")
    game.make_guess("I")
    assert game.is_won()


def test_is_lost():
    game = Wordguess("HI")
    for letter in "ABCDEFG":
        game.make_guess(letter)
    assert game.is_lost()


class TestHangman:
    """Test class for Hangman - ready for test implementation."""
    pass