import random
class Dealer:
    def __init__(self):
        self.win_number=random.randint(0,100)
    def set_number(self):
        self.win_number=random.randint(0,100)
        return self.win_number
    def hint(self,n):
        if n>self.win_number:
            print("猜大了")
            return 1
        elif n<self.win_number:
            print("猜小了")
            return -1
        else:
            print("猜对了")
            return 0
    def award(self,rounds):
        self.Awards=10-rounds
        return self.Awards
class Player(Dealer):
    def __init__(self):
        super().__init__()
        self.points=0
    def guess_number(self,n1=0,n2=100):
        self.n1=n1
        self.n2=n2
        self.guess_num=random.randint(n1,n2)
class Rule(Player,Dealer):
    def __init__(self):
        super().__init__()
        self.rounds=0
    def judge(self,user):
        self.points=user
        self.points+=super().award(self.rounds)

p1=Player()
host=Dealer()
rule=Rule()
def game():
    p1.guess_number()
    low=0
    high=100
    while p1.points>=-10:
        host.set_number()
        host.hint(p1.guess_num)
        if p1.guess_num==host.win_number:
            #rule.judge(p1.points)
            p1.points+=host.award(rule.rounds)
            break
        if host.hint(p1.guess_num)==-1:
            low=p1.guess_num
            p1.guess_number(p1.guess_num,high)
        else:
            high=p1.guess_num
            p1.guess_number(low,p1.guess_num)
        rule.rounds+=1
    print(p1.points)
while p1.points>=-10:
    game()
