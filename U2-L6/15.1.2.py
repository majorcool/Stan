import random
#鱼塘大小10*10
#-1,0,1
class Fish:
    def __init__(self):
        self.x=random.randint(0,10)
        self.y=random.randint(0,10)
        self.speed=1
    def move(self):
        self.straight_move=random.randint(-1,1)
        self.horizontal_move=random.randint(-1,1)
class SmallFish(Fish):
    def __init__(self):
        super().__init__()
    def move(self):
        self.straight_move=0
        self.horizontal_move=0
        self.choosemove=random.randint(1,2)
        if self.choosemove==1:
            self.straight_move=random.randint(-1,1)
        else:
            self.horizontal_move=random.randint(-1,1)
        if self.straight_move==1:
            self.y+=1
        if self.straight_move==-1:
            self.y-=1
        if self.horizontal_move==1:
            self.x+=1
        if self.horizontal_move==-1:
            self.x-=1
        if self.x-10>0:
            self.x=10-(self.x-10)
        if self.y-10>0:
            self.y=10-(self.y-10)
class BigFish(Fish):
    def __init__(self):
        super().__init__()
        self.hp=100
    def move(self):
        super().move()
        big_fish.hp-=1
        if self.straight_move==1:
            self.y+=1
        if self.straight_move==-1:
            self.y-=1
        if self.horizontal_move==1:
            self.x+=1
        if self.horizontal_move==-1:
            self.x-=1
        if self.x-10>0:
            self.x=10-(self.x-10)
        if self.y-10>0:
            self.y=10-(self.y-10)
    def eat(self):
        self.hp+=20
        if self.hp>100:
            self.hp=100
big_fish=BigFish()
small_fishes=list()
for i in range(10):
    small_fishes.append(SmallFish())
while big_fish.hp>0 and small_fishes != []:
    big_fish.move()
    eaten_fishes=[]
    for i,small_fish in enumerate(small_fishes):
        small_fish.move()
        if (big_fish.x,big_fish.y) == (small_fish.x,small_fish.y):
            big_fish.eat()
            eaten_fishes.append(i)
    for i in eaten_fishes:
        del small_fishes[i]
        print(len(small_fishes))
    if len(small_fishes)==0:
        print("大🐟获胜")
        break
    if big_fish.hp<=0:
        print("小🐟获胜")
        break