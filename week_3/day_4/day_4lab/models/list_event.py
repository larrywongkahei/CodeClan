from models.event import Event

event1 = Event("2022-9-19", "Christmas Party", 38, "Rm.308", "Fun Christmas party")
event2 = Event("2022-11-24", "Thanksgiving", 20, "Rm.206", "Various of Foods and Drinks")
event3 = Event("2000-9-30", "Larry's Birthday", 300, "Rm.930", "Happiest party ever")

events = [event1, event2, event3]

def add(event):
    events.append(event)

def remove(event):
    events.remove(event)