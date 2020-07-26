from Model.Account import Account

class DAO():
    def __init__(self, path):
        self.path = path
        self.account_db = None

    def readAccountList(self):
        self.account_db = open(self.path, 'r+')
        lines = self.account_db.readlines()
        accountList = []
        # if lines[0] == "\n":
        #     return accountList
        for line in lines:
            ele = line.strip().split(" ")
            account = Account()
            account.set(ele[1], ele[2], ele[3])
            accountList.append((account))
        self.account_db.close()
        return accountList

    def write(self, account):
        self.account_db = open(self.path, 'a')
        self.account_db.write(f'{account.ID} {account.username} {account.password} {account.role}\n')
        self.account_db.close()
