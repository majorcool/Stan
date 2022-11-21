#基础版
import random
class Player:
    def __init__(self):
        self.points=0
    def punch(self):
        Get=random.randint(1,3)
        if Get==1:
            return '10'
        elif Get==2:
            return '5'
        else:
            return '2'
class Com(Player):
    pass
A=Player()
B=Com()
def game(player,computer):
    player_res=player.punch()
    computer_res=computer.punch()
    if player_res=='10'and computer_res=='5':
        print("Computer wins one round!")
        computer.points+=1
        return 'com'
    if player_res=='10'and computer_res=='2':
        print("Player wins the round!")
        player.points+=1
        return 'player'
    if player_res=='5'and computer_res=='2':
        print("Computer wins the round!")
        computer.points+=1
        return 'com'
    if player_res=='5'and computer_res=='10':
        print("Player wins the round!")
        player.points+=1
        return 'player'
    if player_res=='2'and computer_res=='5':
        print("Player wins the round!")
        player.points+=1
        return 'player'
    if player_res=='2'and computer_res=='10':
        print("Computer wins the round!")
        computer.points+=1
        return 'com'
    if player_res==computer_res:
        print("Tie")
        return 'tie'
game(A,B)

