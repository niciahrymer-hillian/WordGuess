
def welcome():
    print("Welcome to WordGuess!")
    while True:
        guess = input("Guess a letter: ")
        print(f"You guessed: {guess}")
class Wordguess:
    def __init__(self, word):
        self.word = word.upper()
        self.guessed_letters = set()
        self.max_attempts = 6
        self.wrong_guesses = 0
    def display_word(self):
        """Show the word with blanks for the unguessed letters"""
        display = " "
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()
    