class Guests:
    def __init__(self, name, number_of_people, favourite_song):
        self.name = name
        self.Have_a_booking = False
        self.number_of_people = number_of_people
        self.favourite_song = favourite_song
        self.current_songs = ""
        self.ordered_list = []

    
    def check_in(self, room_list):
        room_list.append(self)

    def check_out(self, room_list):
        room_list.remove(self)

    def book_a_room(self):
        self.Have_a_booking = True

    def order_songs(self, song_name, song):
        if song_name in song.song_list:
            self.ordered_list.append(song_name)
            self.current_songs = song_name

