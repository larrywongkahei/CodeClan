import unittest
from modules.songs import Songs

class Test_Songs(unittest.TestCase):
    def setUp(self):
        self.songs = Songs()

    def test_has_songs(self):
        expected_outcome = 12
        actual_outcome = self.songs.songs_total()
        self.assertEqual(expected_outcome, actual_outcome)

        