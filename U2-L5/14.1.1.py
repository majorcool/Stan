class People:
    def talk(self):
        print('Ahhhh')
class infant(People):
    def talk(self):
        print("无法调用")
XM=infant()
XM.talk()