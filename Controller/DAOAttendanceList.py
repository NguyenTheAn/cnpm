import json
import os

class DAOAttendanceList():
    def __init__(self):
        if not os.path.isfile("./Data/attendanceList.json"):
            self.list = {}
        else:
            with open("./Data/attendanceList.json") as f:
                self.list = json.load(f)

    def get(self, name):
        return self.list[name]

    def write(self, name, line):
        if name in self.list:
            self.list[name].append(line)
        else:
            self.list[name] = [line]
        print(self.list)
        with open("./Data/attendanceList.json", 'w') as json_file:
            json.dump(self.list, json_file)