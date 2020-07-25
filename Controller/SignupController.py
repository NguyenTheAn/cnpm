from Controller.DAOAccount import DAO
from Model.Account import Account

class SignupController():
    def __init__(self):
        self.dao = DAO("./Data/account.txt")

    def findExistedAccount(self, verify_account):
        accountList = self.dao.readAccountList()
        for account in accountList:
            if account.username == verify_account.username:
                return True
        return False

    def saveToDb(self, username, password, role):
        account = Account()
        account.set(username, password, role)
        self.dao.write(account)