import unittest
from modules.karaoke import Karaoke
from modules.guests import Guests

class KaraokeTest(unittest.TestCase):
    def setUp(self):
        self.karaoke = Karaoke()

        # self.guest1 = Guests("Larry", 4, "Nothing gonna change my love for you")

    # def test_check_in(self):
    #     self.karaoke.check_in(self.guest1)
    #     expected_outcome = 1
    #     actual_outcome = len(self.karaoke.room_list)
    #     self.assertEqual(expected_outcome, actual_outcome)

    # def test_check_in_fail(self):
    #     for i in range(11):
    #         self.karaoke.check_in(i)
    #     expected_outcome = "Full,sorry"
    #     actual_outcome = self.karaoke.check_in("larry")
    #     self.assertEqual(expected_outcome, actual_outcome)
        
        