from Controller.DAOAttendanceList import DAOAttendanceList

class AtendanceController():
    def __init__(self):
        self.dao = DAOAttendanceList()
    def verifyInfo(self, infor, event):
        name = event.name
        list = self.dao.get(name)
        nameAttendance = infor.split("_")[0]
        for i in list:
            ele = i.split(" ")
            if ele[1] == nameAttendance:
                return True

        return False
