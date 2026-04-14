
import random
from person_interface import PersonInterface
from person import Person

# Module-level word list used by the game loop below
WORD_LIST = ["JUNGLE", "GOOGLE", "BOUNTY", "TRIANGLE", "ZIPCODE", "PYTHON"]




def welcome():
    print("Welcome to WordGuess!")

        

class Wordguess:
    WORD_LIST = ["JUNGLE", "GOOGLE", "BOUNTY", "TRIANGLE", "ZIPCODE", "PYTHON"]

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
    
    def make_guess(self, letter):
        """Process a single letter guess"""
        letter = letter.upper()

        if len(letter) != 1 or not letter.isalpha():
            return "Please guess a single letter"
        if letter in self.guessed_letters:
            return "You already guessed that letter"
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            return f"Good guess! {letter} is in the word"
        else:
            self.wrong_guesses += 1
            return f"Sorry, {letter} is not in the word"
    def is_won(self):
            """Check if all letters have been guessed"""
            return all(letter in self.guessed_letters for letter in self.word)
    def is_lost(self):
            """Check if player is out of attempts"""
            return self.wrong_guesses >= self.max_attempts
    def is_game_over(self):
            """Check if game should end"""
            return self.is_won() or self.is_lost()
    def get_game_status(self):
            """Return a formatted status string"""
            status = f"Word: {self.display_word()}\n"
            status += f"Guessed: {', '.join(sorted(self.guessed_letters))}\n"
            status += f"Attempts remaining: {self.max_attempts - self.wrong_guesses}\n"
            return status
if __name__ == "__main__":
    welcome()
    while True:
        word = random.choice(WORD_LIST)
        player_name = input("Enter your name: ")
        # instantiate Person with name for a simpler API
        player = Person(player_name)

        wordguess = Wordguess(word)

        while not wordguess.is_game_over():
            print(wordguess.get_game_status())
            guess = input("Guess a letter: ")
            result = wordguess.make_guess(guess)
            print(result)

        again = input("Play again? [y/N]: ").strip().lower()
        if again != "y":
            break
         
