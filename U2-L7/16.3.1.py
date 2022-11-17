import random
class Citizen:
    def vote(self):
        pass
class Mafia:
    def kill(self):
        return random.randint(0,9)
    def vote(self):
        pass
class Judge:
    def vote(self):
        pass
citizens=[]
mafias=[]
select=[]
for i in range(6):
    citizens.append(Citizen())
for i in range(3):
    mafias.append(Mafia())
judge=Judge()
def game(citizens,mafias,judge):
    for mafia in mafias:
        select.append(mafia.kill())
    if len(set(select))==len(select):
        print("Mafia kills %d" % (max(select)))

