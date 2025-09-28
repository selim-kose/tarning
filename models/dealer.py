import random

class Dealer:
    def __init__(self):
        self.total = 0
        self.wins = 0

    def __str__(self):
        return f"Dealer {self.total}"

    def roll_dice(self):
        while self.total <= 17:
            self.total += random.randint(1, 6)

    def get_total(self):
        return self.total
