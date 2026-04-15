class Person:
    """Simple Person class for the game."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.score = 0
    
    def add_score(self, points: int):
        self.score += points
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, score={self.score})"