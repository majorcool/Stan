class Easymath:
    def __init__(self,user,id):
        self.user=user
        self.id=id
    def easy_add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return num1+num2
    def easy_minus(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return num1-num2
User=Easymath('II',2)
print(User.easy_add(8,7))