#骗子版本
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
    def challenge(self):
        yes_or_no=random.randint(0,1)
        if yes_or_no==0:
            return 'yes'
        else:
            return 'no'
class Com(Player):
    pass
class Fraud:
    def lie(self):
        Reply=random.randint(1,2)
        if Reply==1:
            return 'lose'
        else:
            return 'tie'
A=Player()
B=Com()
C=Fraud()
def game(player,computer,fraud):
    add_point=1
    fraud_reply=""
    player_res=player.punch()
    computer_res=computer.punch()
    if player_res=='10'and computer_res=='5':
        Challenge=player.challenge()
        if Challenge=='yes':
            add_point+=1
        else:
            fraud_reply=fraud.lie()
            if fraud_reply=='tie':
                print("Tie(Fraud)")
                return 'tie'
            else:
                print("Computer wins the round(Fraud)")
                computer.points+=add_point
                print(computer.points)
                print(player.points)
                return 'com'
        print("Computer wins one round!")
        computer.points+=add_point
        print(computer.points)
        print(player.points)
        return 'com'
    if player_res=='10'and computer_res=='2':
        Challenge=player.challenge()
        if Challenge=='yes':
            add_point+=1
        else:
            fraud_reply=fraud.lie()
            if fraud_reply=='tie':
                print("Tie(Fraud)")
                return 'tie'
            else:
                print("Computer wins the round(Fraud)")
                computer.points+=add_point
                print(computer.points)
                print(player.points)
                return 'com'
        print("Player wins the round!")
        player.points+=add_point
        print(computer.points)
        print(player.points)
        return 'player'
    if player_res=='5'and computer_res=='2':
        Challenge=player.challenge()
        if Challenge=='yes':
            add_point+=1
        else:
            fraud_reply=fraud.lie()
            if fraud_reply=='tie':
                print("Tie(Fraud)")
                return 'tie'
            else:
                print("Computer wins the round(Fraud)")
                computer.points+=add_point
                print(computer.points)
                print(player.points)
                return 'com'
        print("Computer wins the round!")
        computer.points+=add_point
        print(computer.points)
        print(player.points)
        return 'com'
    if player_res=='5'and computer_res=='10':
        Challenge=player.challenge()
        if Challenge=='yes':
            add_point+=1
        else:
            fraud_reply=fraud.lie()
            if fraud_reply=='tie':
                print("Tie(Fraud)")
                return 'tie'
            else:
                print("Computer wins the round(Fraud)")
                computer.points+=add_point
                print(computer.points)
                print(player.points)
                return 'com'
        print("Player wins the round!")
        player.points+=add_point
        print(computer.points)
        print(player.points)
        return 'player'
    if player_res=='2'and computer_res=='5':
        Challenge=player.challenge()
        if Challenge=='yes':
            add_point+=1
        else:
            fraud_reply=fraud.lie()
            if fraud_reply=='tie':
                print("Tie(Fraud)")
                return 'tie'
            else:
                print("Computer wins the round(Fraud)")
                computer.points+=add_point
                print(computer.points)
                print(player.points)
                return 'com'
        print("Player wins the round!")
        player.points+=add_point
        print(computer.points)
        print(player.points)
        return 'player'
    if player_res=='2'and computer_res=='10':
        Challenge=player.challenge()
        if Challenge=='yes':
            add_point+=1
        else:
            fraud_reply=fraud.lie()
            if fraud_reply=='tie':
                print("Tie(Fraud)")
                return 'tie'
            else:
                print("Computer wins the round(Fraud)")
                computer.points+=add_point
                print(computer.points)
                print(player.points)
                return 'com'
        print("Computer wins the round!")
        computer.points+=add_point
        print(computer.points)
        print(player.points)
        return 'com'
    if player_res==computer_res:
        Challenge=player.challenge()
        if Challenge=='yes':
            add_point+=1
        else:
            fraud_reply=fraud.lie()
            if fraud_reply=='tie':
                print("Tie(Fraud)")
                return 'tie'
            else:
                print("Computer wins the round(Fraud)")
                computer.points+=add_point
                print(computer.points)
                print(player.points)
                return 'com'
        print("Tie")
        return 'tie'
game(A,B,C)

