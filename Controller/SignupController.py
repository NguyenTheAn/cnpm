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

    def saveToDb(self, account):
        self.dao.write(account)