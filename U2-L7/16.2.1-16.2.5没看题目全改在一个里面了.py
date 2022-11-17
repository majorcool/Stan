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
    def award(self,rounds,player):
        player.points=10-rounds
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
    def judge(self,rounds,player):
        player.points+=10-rounds
p1=Player()
host=Dealer()
rule=Rule()
def game(host,player):
    player.guess_number()
    low=0
    high=100
    while player.points>=-10:
        host.set_number()
        host.hint(player.guess_num)
        if player.guess_num==host.win_number:
            rule.judge(rule.rounds,player)
            break
        if host.hint(player.guess_num)==-1:
            low=player.guess_num
            player.guess_number(player.guess_num,high)
        else:
            high=player.guess_num
            player.guess_number(low,player.guess_num)
        rule.rounds+=1
    print(p1.points)
while p1.points>=-10:
    game(host,p1)
