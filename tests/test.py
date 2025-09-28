import unittest
from models import Player, Dealer

class Test(unittest.TestCase):

    #Test Player initialization
    def test_player_initialization(self):
        player = Player()
        self.assertEqual(player.score, 0, "Initial player score should be 0")
        self.assertEqual(player.current_roll, 0, "Initial player current roll should be 0")
        self.assertEqual(player.wins, 0, "Initial player wins should be 0")

    # Test Player roll_dice method, ensuring the roll is between 1 and 6
    def test_player_roll_dice(self):
        for i in range(1000):
            player = Player()
            player.roll_dice()
            self.assertTrue(1 <= player.current_roll <= 6, "Player roll should be between 1 and 6")

    """
    @patch("models.player.random.randint", return_value=6)
    def test_roll_dice_max_value(self, mock_randint):
        player = Player()
        roll = player.roll_dice()
        self.assertEqual(roll, 6)
        self.assertEqual(p.get_score(), 6)
    """

    # Test Dealer roll_dice method, ensuring the total is greater than 17
    def test_dealer_roll_dice(self):
        dealer = Dealer()
        dealer.roll_dice()
        self.assertTrue(dealer.get_total() >= 17, "Dealer total should be greater than 17")

