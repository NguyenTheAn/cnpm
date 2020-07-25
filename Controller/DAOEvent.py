from Model.Event import Event

class DAO():
    def __init__(self, path):
        self.path = path
        self.event_db = None

    def readEventList(self):
        self.event_db = open(self.path, 'r')
        lines = self.event_db.readlines()
        eventList = []
        for line in lines:
            ele = line.strip().split(" ")
            eventList.append(Event(ele[0], ele[1], ele[2], ele[3]))
        self.event_db.close()
        return eventList

    def write(self, event):
        self.event_db = open(self.path, 'a')
        self.event_db.write(f'{event.name} {event.description} {event.startDate} {event.endDate}\n')
        self.event_db.close()
