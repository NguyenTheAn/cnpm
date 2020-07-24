from Model.Account import Account

class DAO():
    def __init__(self, path):
        self.account_db = open(path, 'r')

    def readAccountList(self):
        lines = self.account_db.readlines()
        accountList = []
        for line in lines:
            ele = line.strip().split(" ")
            account = Account()
            account.set(ele[0], ele[1], ele[2])
            accountList.append((account))
        return accountList
