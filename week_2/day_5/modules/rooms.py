class Rooms:
    def __init__(self):
        #Room number 95-99 == small room
        self.small_room = 5 
        #Room number 100-109 == big room
        self.big_room = 10
        self.guests_list = []

    # def add_guest(self, guest):
    #     guest.guests_list.append(guest)

    def check_availability(self):
        number = 0
        for x,y in self.room_availability.items():
            if y:
                number += 1
        return number


    def guests_check_in(self, guest):
        if guest.number_of_people <= 5:
            for room, availability in self.room_availability.items():
                if str(room).startswith("9") and availability:
                    self.room_availability[room] = False
                    room_number = room
                    room = guest.name
                    return f"Checked in Room {room_number}"
            return "Full, Sorry"
        else:
            for room, availability in self.room_availability.items():
                if str(room).startswith("1") and availability:
                    self.room_availability[room] = False
                    return f"Checked in Room {room}"
            return "Full, Sorry"

    def guests_check_out(self, guest):
        for room in self.room_availability:
            if room == guest.name:
                room = "Cleaning"
                
    def check_all_room_condition(self):
        return self.room_availability



