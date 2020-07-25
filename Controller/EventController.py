from Controller.DAOEvent import DAO
from Model.Event import Event

class EventController():
    def __init__(self):
        self.dao = DAO("./Data/Event.txt")

    def saveToDb(self, name, description, startDate, endDate):
        account = Event(name, description, startDate, endDate)
        self.dao.write(account)