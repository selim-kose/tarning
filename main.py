from models import Player, Dealer
from game import Game

def main():
    player = Player()
    dealer = Dealer()

    game = Game(player, dealer)
    game.play()

    print("-------------------------")
    choice = input("Would you like to play again? (y/n): ")
    if choice.strip().lower() == 'y':
       main()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()