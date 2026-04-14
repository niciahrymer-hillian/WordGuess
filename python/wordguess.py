
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
    def make_guess(self, letter):
        """Process a single letter guess"""
        letter = letter.upper()

        if len(letter) != 1 or not letter.isalpha():
            return "Please guess a single letter"
        if letter in self.guessed_letters:
            return "You already guessed that letter"
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            return f"Good gurss! {letter} is in the word"
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
            return self.is_won() or self.Is_lost()
        def get_game_status(self):
            """Return a formatted status string"""
            status = f"WOrd: {self.display_word()}\n"
            status += f"Guessed: {', '.join(sorted(self.guessed_letters))}\n"
            status += f"Attempts remaining: {self.max_attempts - self.wrong_guesses}\n"
            return status
class Person:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.games_played = 0
        self.games_won = 0
    def update_score(self, points):
        """Add points to player's score"""
        self.score += points
    def record_game(self, won):
        """Track game statistics"""
        self.games_played += 1
        if won:
            self.games_won += 1
            
    def get_win_rate(self):
        """Calculate winning percentage"""
        if self.games_played == 0:
            return 0.0
        return (self.games_won / self.games_plaed) * 100
         
