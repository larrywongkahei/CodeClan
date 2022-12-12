import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 7)
        self.card2 = Card("Clubs", 5)
        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        expected_outcome = False
        actual_outcome = CardGame.check_for_ace(self, self.card1)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_highest_card(self):
        expected_outcome = self.card1
        actual_outcome = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_cards_total(self):
        expected_outcome = "You have a total of {}".format(12)
        actual_outcome = CardGame.cards_total(self, self.cards)
        self.assertEqual(expected_outcome, actual_outcome)
