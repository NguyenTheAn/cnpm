import random


class Event():
    def __init__(self, name, description, startDate, endDate):
        self.ID = random.randint(100000, 1000000)
        self.name = name
        self.description = description
        self.startDate = startDate
        self.endDate = endDate
