import unittest
from modules.guests import Guests
from modules.rooms import Rooms
from modules.songs import Songs
from modules.karaoke import Karaoke

class Test_Guests(unittest.TestCase):
    def setUp(self):
        self.songs = Songs()

        self.karaoke = Karaoke()

        self.room = Rooms()
        self.guest1 = Guests("Larry", 4, "Nothing gonna change my love for you")
        self.guest1.check_in(self.karaoke.room_list)

        guest2 = Guests("Tim", 4, "Heal the world")
        guest2.check_in(self.karaoke.room_list)

        self.guest3 = Guests("Mary", 6, "My apple pie")
        self.guest3.check_in(self.karaoke.room_list)

        guest4 = Guests("Cindy", 6, "My love")
        guest4.check_in(self.karaoke.room_list)

    def test_check_in(self):
        expected_outcome = self.guest1
        actual_outcome = self.karaoke.room_list[0]

        self.assertEqual(expected_outcome, actual_outcome)

    def test_check_in2(self):
        expected_outcome = 4
        actual_outcome = len(self.karaoke.room_list)

        self.assertEqual(expected_outcome, actual_outcome)

    def test_check_out(self):
        expected_outcome = 3
        self.guest1.check_out(self.karaoke.room_list)
        actual_outcome = len(self.karaoke.room_list)

        self.assertEqual(expected_outcome, actual_outcome)

    def test_check_out2(self):
        expected_outcome = 2
        self.guest1.check_out(self.karaoke.room_list)
        self.guest3.check_out(self.karaoke.room_list)
        actual_outcome = len(self.karaoke.room_list)

        self.assertEqual(expected_outcome, actual_outcome)

    def test_book_a_room(self):
        expected_outcome = True
        self.guest1.book_a_room()
        actual_outcome = self.guest1.Have_a_booking

        self.assertEqual(expected_outcome, actual_outcome)

    def test_order_song(self):
        expected_outcome = "My apple pie"
        self.guest1.order_songs("My apple pie", self.songs)
        actual_outcome = self.guest1.current_songs
        self.assertEqual(expected_outcome, actual_outcome)

    def test_ordered_song_list(self):
        expected_outcome = "My apple pie"
        self.guest1.order_songs("My apple pie", self.songs)
        actual_outcome = self.guest1.ordered_list[0]
        self.assertEqual(expected_outcome, actual_outcome)





