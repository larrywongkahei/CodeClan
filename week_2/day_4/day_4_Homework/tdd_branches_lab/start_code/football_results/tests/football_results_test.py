import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def setUp(self):
        self.homewin_score = {"home_score": 1,"away_score": 0}
        self.awaywin_score = {"home_score": 0,"away_score": 1}
        self.draw_score = {"home_score": 1,"away_score": 1}
        self.final_scores = [self.homewin_score, self.awaywin_score, self.draw_score]

    # Test we get the right result string for a final score dictionary representing -
    def test_get_the_result_homewin(self):
        expected_outcome = "Home win"
        actual_outcome = get_result(self.homewin_score)
        self.assertEqual(expected_outcome, actual_outcome)
        # Home win
    
    def test_get_the_result_awaywin(self):
        expected_outcome = "Away win"
        actual_outcome = get_result(self.awaywin_score)
        self.assertEqual(expected_outcome, actual_outcome)
        # Away win

    def test_get_the_result_draw(self):
        expected_outcome = "Draw"
        actual_outcome = get_result(self.draw_score)
        self.assertEqual(expected_outcome, actual_outcome)
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 
    def test_get_the_results(self):
        expected_outcome = ["Home win", "Away win", "Draw"]
        actual_outcome = get_results(self.final_scores)
        self.assertEqual(expected_outcome, actual_outcome) 

if __name__ == "__main__":
    unittest.main()
