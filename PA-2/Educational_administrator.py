class E_A:
    def __init__(self,Username,Password):
        self.UserName=Username
        self.PassWord=Password
        self.UserType='EA'
    def Login_(self):
        return self.UserName, self.PassWord