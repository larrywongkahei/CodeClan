from datetime import datetime

class Event:
    def __init__(self, date, name, number_guest, location, description):
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.name = name
        self.number_guest = number_guest
        self.location = location
        self.description = description