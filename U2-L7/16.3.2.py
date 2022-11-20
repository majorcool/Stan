import random
class Citizen:
    def __init__(self):
        self.id='citizen'
    def vote(self):
        return random.randint(0,len(players)-1)
    def select(self):
        return 'citizen'
class Mafia:
    def __init__(self):
        self.id='mafia'
    def kill(self):
        return random.randint(0,len(players)-1)
    def vote(self):
        return random.randint(0,len(players)-1)
    def select(self):
        return 'mafia'
class Judge:
    def __init__(self):
        self.id='judge'
    def vote(self):
        return random.randint(0,len(players)-1)
    def select(self):
        return 'judge'
class Cop(Citizen):
    def __init__(self):
        self.id='cop'
    def ask(self,player):
        return player.id
    def select(self):
        return 'cop'
players=[]
for i in range(6):
    players.append(Citizen())
for i in range(3):
    players.append(Mafia())
players.append(Judge())
players.append(Cop())
def game(players):
    while 1:
        select=[]
        vote=[]
        for player in players:
            if player.select()=='mafia':
                select.append(player.kill())
                print(select)
        if len(set(select))==len(select):
            print("Mafia kills %s" % (players[max(select)].select()))
            players.pop(max(select))
        else:
            killed=False
            for items in range(1,len(select)):
                i1=select[0]
                i2=select[items]
                if i1==i2:
                    print("Mafia kills %s" % (players[select[0]].select()))
                    players.pop(select[0])
                    killed=True
            if killed==False:
                print("Mafia kills %s" % (players[select[1]].select()))
                players.pop(select[1])
        mafia_live=False
        good_live=False
        for player in players:
            if player.select()=='citizen':
                good_live=True
            if player.select()=='mafia':
                mafia_live=True
            if player.select()=='judge':
                good_live=True
        if good_live==False:
            print("Mafia Wins")
            break
        elif mafia_live==False:
            print("Good Wins")
            break
        cop_is_alive=False
        judge_is_alive=False
        for player in players:
            if player.select()=='cop':
                cop_is_alive=True
            if player.select()=='judge':
                judge_is_alive=True
        if cop_is_alive==True and judge_is_alive==True:
            for player in players:
                if player.select() == 'cop':
                    player_id=random.randint(0,len(players)-1)
                    Identity=player.ask(players[player_id])
                    print("警官询问了Judge并得知了 %s 的身份是 %s" % (player_id,Identity))
                    if Identity=='mafia':
                        print("Cop killed mafia")
                        players.pop()

        print("开始讨论")
        for player in players:
            vote.append(player.vote())
        print("投票结果",vote)
        if len(set(vote))==len(vote):
            print("Players vote to kill %s" % (players[max(vote)].select()))
            players.pop(max(vote))

        else:
            num=0
            c1=-10
            for x,y in enumerate(vote):
                if c1<=vote.count(num):
                    c1=vote.count(num)
                    c2=x
                num+=1
            print("Players vote to kill %s" % (players[c2].select()))
            players.pop(c2)
        mafia_live=False
        good_live=False
        for player in players:
            if player.select()=='citizen':
                good_live=True
            if player.select()=='mafia':
                mafia_live=True
            if player.select()=='judge':
                good_live=True
        if good_live==False:
            print("Mafia Wins")
            break
        elif mafia_live==False:
            print("Good Wins")
            break
        else:
            continue





game(players)

