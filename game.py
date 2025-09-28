from models import Player, Dealer
import highscore

class Game:

    def __init__(self, player: Player, dealer: Dealer):
        self.player = player
        self.dealer = dealer

    def play(self):
        self.player.wins, self.dealer.wins = highscore.load_highscores()

        print("Welcome to the Dice Game!")
        print("-------------------------")
        print("### High Scores ###")
        print(f"Player wins: {self.player.wins}\nDealer wins: {self.dealer.wins}")
        print("-------------------------")

        while True:
            choice = input("Do you want to roll the dice? (y/n): ").strip().lower()
            if choice == 'y':
                self.player.roll_dice()
                print("-------------------------")
                print(f"You rolled the dice.\nYou hit a {self.player.current_roll}!\nYour total is: {self.player.get_score()}")
                print("-------------------------")
                if self.player.get_score() > 21:
                    print("You busted! Dealer wins.")
                    highscore.save_highscores(self.player.wins,self.dealer.wins +1,"highscores.txt")
                    return
            elif choice == 'n':
                print("You chose to hold.")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        self.dealer.roll_dice()
        print(f"Dealer's final total is: {self.dealer.get_total()}")

        if self.dealer.get_total() > 21 or self.player.get_score() > self.dealer.get_total():
            print("You win!")
            highscore.save_highscores(self.player.wins + 1,self.dealer.wins,"highscores.txt")
        elif self.player.get_score() < self.dealer.get_total():
            print("Dealer wins!")
            highscore.save_highscores(self.player.wins,self.dealer.wins +1,"highscores.txt")
        else:
            print("It's a tie!")