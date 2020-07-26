from Controller.DAOEvent import DAO

class SeachController():
    def __init__(self):
        self.dao = DAO("./Data/Event.txt")
    def seach(self, name):
        eventList = self.dao.readEventList()
        resultList = []
        for event in eventList:
            if event.name == name:
                resultList.append(event)

        return resultList