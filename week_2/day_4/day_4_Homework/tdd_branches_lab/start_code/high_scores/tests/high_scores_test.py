import unittest

from src.high_scores import latest, personal_best, personal_top_three, personal_highest_to_lowest

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    def setUp(self):
        self.scores = [60, 70, 40, 50 ,30, 3, 50 ,85, 85, 90]
        self.two_scores = [30, 50]
        self.one_scores = [5]

    # Test latest score (the last thing in the list)
    def test_lastest_score(self):
        expected_outcome = 90
        user_outcome = latest(self.scores)
        self.assertEqual(expected_outcome, user_outcome)


    # Test personal best (the highest score in the list)
    def test_highest_score(self):
        expected_outcome = 90
        user_outcome = personal_best(self.scores)
        self.assertEqual(expected_outcome, user_outcome)

    # Test top three from list of scores
    def test_personal_top_three(self):
        expect_outcome = [85, 85, 90]
        user_outcome = personal_top_three(self.scores)
        self.assertEqual(expect_outcome, user_outcome)

    # Test ordered from highest tp lowest
    def test_highest_to_lowest(self):
        expect_outcome = [90, 85, 85, 70, 60, 50, 50, 40, 30, 3]
        user_outcome = personal_highest_to_lowest(self.scores)
        self.assertEqual(expect_outcome, user_outcome)


    # Test top three when there is a tie
    def test_top_three_when_theres_tie(self):
        expect_outcome = [85, 85, 90]
        user_outcome = personal_top_three(self.scores)
        self.assertEqual(expect_outcome, user_outcome)


    # Test top three when there are less than three
    def test_top_three_when_theres_less_than_three(self):
        expect_outcome = [30, 50]
        user_outcome = personal_top_three(self.two_scores)
        self.assertEqual(expect_outcome, user_outcome)


    # Test top three when there is only one
    def test_top_three_when_theres_only_one(self):
        expect_outcome = [5]
        user_outcome = personal_top_three(self.one_scores)
        self.assertEqual(expect_outcome, user_outcome)
    
