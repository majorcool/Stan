class User:
    def __init__(self):
        self.id='sd2'
        self.nickname='lbw'
        self.credits=100
    def get_info(self):
        print('id:%s\nname:%s\ncredits:%d'%(self.id,self.nickname,self.credits))
    def upgrade_to_vip(self):
        self=Vip()
class Vip(User):
    def __init__(self):
        self.vip_level=1
        print("您已成为VIP")
a=User()
a.upgrade_to_vip()
