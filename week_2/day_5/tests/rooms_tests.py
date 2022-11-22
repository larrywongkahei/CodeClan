import unittest
from modules.rooms import Rooms
from modules.guests import Guests
from modules.songs import Songs

class Test_Rooms(unittest.TestCase):
    def setUp(self):
        self.songs = Songs()

        self.room = Rooms()

        self.guest1 = Guests("Larry", 4, "Nothing gonna change my love for you")
        self.guest1.check_in(self.room.guests_list)

        guest2 = Guests("Tim", 4, "Heal the world")
        guest2.check_in(self.room.guests_list)

        self.guest3 = Guests("Mary", 6, "My apple pie")
        self.guest3.check_in(self.room.guests_list)

        guest4 = Guests("Cindy", 6, "My love")
        guest4.check_in(self.room.guests_list)

    # def test_check_add_guest(self):
    #     new_room = Rooms()
    #     first_outcome = 0
    #     first_actual_outcome = len(new_room.guests_list)
    #     self.assertEqual(first_outcome, first_actual_outcome)

    #     new_room.add_guest(self.guest1)
    #     expected_outcome = 1
    #     actual_outcome = len(new_room.guests_list)
    #     self.assertEqual(expected_outcome, actual_outcome)

    # def test_check_number_of_guests(self):
    #     expected_outcome = 4
    #     actual_outcome =len(self.room.guests_list)

    #     self.assertEqual(expected_outcome, actual_outcome)

    def test_Rooms_number_of_small_rooms(self):
        expected_outcome = 5
        actual_outcome = self.room.small_room

        self.assertEqual(expected_outcome, actual_outcome)

    def test_Rooms_number_of_big_rooms(self):
        expected_outcome = 10
        actual_outcome = self.room.big_room

        self.assertEqual(expected_outcome, actual_outcome)

    def test_Rooms_number_of_availability(self):
        expected_outcome = 15
        actual_outcome = self.room.check_availability()

        self.assertEqual(expected_outcome, actual_outcome)
    
    def test_guest_check_in_smallroom_OK(self):
        expected_outcome = "Checked in Room 95"
        actual_outcome = self.room.guests_check_in(self.guest1)
        check = self.room.check_availability()

        self.assertEqual(14, check)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_guest_check_in_smallroom_Failed(self):
        new_room = Rooms()
        new_room.room_availability = {num : False for num in range(95, 110)}
        expected_outcome = "Full, Sorry"
        actual_outcome = new_room.guests_check_in(self.guest1)
        check = new_room.check_availability()

        self.assertEqual(0, check)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_guest_check_in_bigroom_OK(self):
        expected_outcome = "Checked in Room 100"
        actual_outcome = self.room.guests_check_in(self.guest3)
        check = self.room.check_availability()

        self.assertEqual(14, check)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_guest_check_in_bigroom_Failed(self):
        new_room = Rooms()
        new_room.room_availability = {num : False for num in range(95, 110)}
        expected_outcome = "Full, Sorry"
        actual_outcome = new_room.guests_check_in(self.guest3)
        check = new_room.check_availability()

        self.assertEqual(0, check)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_guest_check_in_another_smallroom_OK(self):
        new_room = Rooms()
        new_room.room_availability[95] = False
        expected_outcome = "Checked in Room 96"
        actual_outcome = new_room.guests_check_in(self.guest1)
        check = new_room.check_availability()

        self.assertEqual(13, check)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_guest_check_in_another_bigroom_OK(self):
        new_room = Rooms()
        new_room.room_availability[100] = False
        expected_outcome = "Checked in Room 101"
        actual_outcome = new_room.guests_check_in(self.guest3)
        check = new_room.check_availability()

        self.assertEqual(13, check)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_guest_check_out(self):
        self.room.guests_check_in(self.guest1)
        self.room.guests_check_out(self.guest1)
        expected_outcome = 14
        actual_outcome = self.room.check_availability()

        self.assertEqual(expected_outcome, actual_outcome)

    def test_guest_check_out_big_room(self):
        self.room.guests_check_in(self.guest1)
        self.room.guests_check_out(self.guest1)
        expected_outcome = 14
        actual_outcome = self.room.check_availability()

        self.assertEqual(expected_outcome, actual_outcome)

    def test_check_all_room_condition(self):
        expected_outcome = True
        dict = self.room.check_all_room_condition()
        actual_outcome = dict[95]
        self.assertEqual(expected_outcome, actual_outcome)



    