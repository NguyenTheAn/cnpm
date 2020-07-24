from Controller.DAO import DAO

class LoginController():
    def __init__(self):
        self.dao = DAO("./Data/account.txt")

    def verify(self, verify_account):
        accountList = self.dao.readAccountList()
        for account in accountList:
            if account == verify_account:
                return True

        return False