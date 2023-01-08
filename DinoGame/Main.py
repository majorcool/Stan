import pygame
import sys  # sys 是 python 的标准库，提供 Python 运行时环境变量的操控
import random
from Obstacles import *
from Scorboard import *
from dino import *
import keyboard
# settings
FPS = 60
TITLE = 'Chrome Dino'
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (1400, 600)
IMAGE_PATHS = {
    'ground': 'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground.png',
    'cloud': 'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cloud/cloud.png',
    'bird1':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/pterodactyl/pterodactyl-1.png',
    'bird2': 'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/pterodactyl/pterodactyl-2.png',
    'ani_gr_1':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground——an1.png",
    'ani_gr_2':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an2.png",
    'ani_gr_3':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an3.png",
    'ani_gr_4': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an4.png",
    'ani_gr_5': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an5.png",
    'ani_gr_6': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an6.png",
    'ani_gr_7': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an7.png",
    'ani_gr_8': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an8.png",
    'ani_gr_9': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an9.png",
    'ani_gr_10': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an10.png",
    'ani_gr_11': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an11.png",
    'Start_Hint':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/StartHint.png"
}
Start_Hint=pygame.image.load(IMAGE_PATHS['Start_Hint'])
an1=pygame.image.load(IMAGE_PATHS['ani_gr_1'])
an2=pygame.image.load(IMAGE_PATHS['ani_gr_2'])
an3=pygame.image.load(IMAGE_PATHS['ani_gr_3'])
an4=pygame.image.load(IMAGE_PATHS['ani_gr_4'])
an5=pygame.image.load(IMAGE_PATHS['ani_gr_5'])
an6=pygame.image.load(IMAGE_PATHS['ani_gr_6'])
an7=pygame.image.load(IMAGE_PATHS['ani_gr_7'])
an8=pygame.image.load(IMAGE_PATHS['ani_gr_8'])
an9=pygame.image.load(IMAGE_PATHS['ani_gr_9'])
an10=pygame.image.load(IMAGE_PATHS['ani_gr_10'])
an11=pygame.image.load(IMAGE_PATHS['ani_gr_11'])
ground_image=pygame.image.load(IMAGE_PATHS['ground'])
cloud_image=pygame.image.load(IMAGE_PATHS['cloud'])
bird1=pygame.image.load(IMAGE_PATHS['bird1'])
bird2=pygame.image.load(IMAGE_PATHS['bird2'])
zero=pygame.image.load(SC_IMAGES['0'])
one=pygame.image.load(SC_IMAGES['1'])
two=pygame.image.load(SC_IMAGES['2'])
three=pygame.image.load(SC_IMAGES['3'])
four=pygame.image.load(SC_IMAGES['4'])
five=pygame.image.load(SC_IMAGES['5'])
six=pygame.image.load(SC_IMAGES['6'])
seven=pygame.image.load(SC_IMAGES['7'])
eight=pygame.image.load(SC_IMAGES['8'])
nine=pygame.image.load(SC_IMAGES['9'])
HI=pygame.image.load(SC_IMAGES['HI'])
blank=pygame.image.load(SC_IMAGES['Blank'])
dino_die=pygame.image.load(Image_Paths['DinoDie'])
dino_duck1=pygame.image.load(Image_Paths['DinoDuck1'])
dino_duck2=pygame.image.load(Image_Paths['DinoDuck2'])
dino_jump=pygame.image.load(Image_Paths['DinoJump'])
dino_run1=pygame.image.load(Image_Paths['DinoRun1'])
dino_run2=pygame.image.load(Image_Paths['DinoRun2'])
dino_start=pygame.image.load(Image_Paths['DinoStart'])
class Ground(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)

        # two same pictures
        self.image_0 = image
        self.rect_0 = self.image_0.get_rect()
        self.rect_0.left, self.rect_0.bottom = position
        self.displacement=0
        self.image_1 = image
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.left, self.rect_1.bottom = self.rect_0.right, self.rect_0.bottom

        # pixels move each term
        self.speed = -10

    # calculate position
    def update(self):
        self.displacement+=1
        self.rect_0.left += self.speed
        self.rect_1.left += self.speed
        if self.rect_0.right < 0:
            self.rect_0.left = self.rect_1.right
            self.rect_0, self.rect_1 = self.rect_1, self.rect_0
    # draw to screen
    def draw(self, screen):
        screen.blit(self.image_0, self.rect_0)
        screen.blit(self.image_1, self.rect_1)
class Cloud(pygame.sprite.Sprite):#pygame.sprite.Sprite is the base for any visible elements
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)

        # two same pictures
        self.image = image
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.right=700
        # pixels move each term
        self.speed = -5
    def draw(self,pos):
        screen.blit(self.image, self.rect)
    def update(self):
        self.rect.right += self.speed
        if self.rect.right < 0:
            self.rect.right=1400
            self.rect.y=random.randint(200,350)
            self.speed=random.randint(-8,-5)
class Ani_Ground(pygame.sprite.Sprite):#pygame.sprite.Sprite is the base for any visible elements
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.images=images
        self.image=self.images[0]
        self.rect=self.image.get_rect()
        self.rect.bottom=600
        self.rect.left=0
        self.counter=0
        self.finished=False
    def draw(self,screen):
        screen.blit(self.image, self.rect)
    def update(self):
        if self.finished==False:
            self.counter+=1
            if self.counter!=0 and self.counter%20==0:
                self.image=self.images[self.counter//40]
            if self.counter==220:
                self.finished=True
                dino.status='started'


# 内部各功能模块进行初始化创建及变量设置，默认调用
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)
music_played=False
clock = pygame.time.Clock()
ground=Ground(ground_image,(0,SCREENSIZE[1]))
cloud=Cloud(cloud_image)
ptera=Ptera([bird1,bird2])
ani_gr=Ani_Ground([an1,an2,an3,an4,an5,an6,an7,an8,an9,an10,an11,ground_image])
scoreboard=ScoreBoard([zero,one,two,three,four,five,six,seven,eight,nine,HI,blank])
dino=Dino([dino_start,dino_run1,dino_run2,dino_jump,dino_duck1,dino_duck2,dino_die])
screen.fill(BACKGROUND_COLOR)
f = pygame.font.Font(None,50)
text = f.render("Press Space To Start",True,(154, 160, 166),(235,235,235))
screen.blit(text,(100,100))
dino.draw(screen)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if dino.status=="unstarted" or dino.status=="Start_Animation":
        screen.fill(BACKGROUND_COLOR)
        dino.start()
        dino.draw(screen)
        pygame.display.update()
    elif dino.status=='half_started':
        dino.dino_stat='run'
        screen.fill(BACKGROUND_COLOR)
        dino.update()
        dino.draw(screen)
        ani_gr.update()
        ani_gr.draw(screen)
        pygame.display.update()
    elif dino.status=="started":
        screen.fill(BACKGROUND_COLOR)
        cloud.draw(screen)
        dino.jump_spd=10
        dino.c_limit=15
        dino.d_limit=30
        cloud.update()
        dino.update()
        dino.draw(screen)
        ground.draw(screen)
        ground.update()
        if scoreboard.score>=300:
            ptera.spawn()
        if ptera.exist==True:
            ptera.update()
            ptera.draw(screen)
        if scoreboard.score and not scoreboard.score % 100:
            scoreboard.calculate()
            if music_played==False:
                pygame.mixer.Sound('C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/audios/score.mp3').play()  # sound
                music_played=True
            scoreboard.flicker(screen)
        else:
            music_played=False
            scoreboard.calculate()
            scoreboard.draw(screen)
        #if game_status == 'end':
            #scoreboard.high_score = max(scoreboard.score, scoreboard.high_score)
        pygame.display.update()
        clock.tick(FPS)
