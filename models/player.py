import random

class Player:
    def __init__(self):
        self.score = 0
        self.current_roll = 0
        self.wins = 0

    def __str__(self):
        return f"Player {self.score}"

    def roll_dice(self):
        self.current_roll = random.randint(1, 6)
        self.score += self.current_roll

    def get_score(self):
        return self.score
