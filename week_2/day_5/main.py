from modules.guests import Guests
from modules.rooms import Rooms
from modules.songs import Songs
from modules.karaoke import Karaoke
import random
import time

Continue = True
songs = Songs()
rooms = Rooms()
karaoke = Karaoke()


Add_customer = input("Have customer?").lower()


def start():
    name = input("Enter customer's name -->")
    number_of_people = int(input("Enter the number of customers -->"))
    # booking = input("Does he/she have a booking? -->")
    favourite = random.choice(songs.song_list)
    guest1 = Guests(name, number_of_people, favourite)

    guest1.check_in(karaoke.room_list) 
    rooms.guests_check_in(guest1)
