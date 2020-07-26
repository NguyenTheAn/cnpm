import random


class Account():
    def __init__(self):
        self.ID = random.randint(100000, 1000000)
        self.username = ''
        self.password = ''
        self.role = ''

    def set(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
    def get(self):
        return self.username, self.password, self.role

    def __eq__(self, other):
        name, p, r = other.get()
        if name == self.username and p == self.password and r == self.role:
            return True
        return False