def load_highscores(filepath="highscores.txt"):
    try:
        with open(filepath, "r") as file:
            lines = file.read().split(",")
            player_wins = int(lines[0])
            dealer_wins = int(lines[1])
            return player_wins, dealer_wins
    except FileNotFoundError:
        # If file does not exist, start with 0–0
        return 0, 0

def save_highscores(player_wins, dealer_wins, filepath="highscores.txt"):
    with open(filepath, "w") as file:
        file.write(f"{player_wins},{dealer_wins}")
