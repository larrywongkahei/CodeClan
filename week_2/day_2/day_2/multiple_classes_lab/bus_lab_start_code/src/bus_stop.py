class BusStop:
    def __init__(self, station_name):
        self.name = station_name
        self.q_length = []

    def queue_length(self):
        return len(self.q_length)

    def add_to_queue(self, person):
        self.q_length.append(person)

    def clear(self):
        self.q_length.clear()
