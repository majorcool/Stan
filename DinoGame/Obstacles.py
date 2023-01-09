import random
import pygame
Paths={
    'cac1':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-1.png",
    'cac2':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-2.png",
    'cac3':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-3.png",
    'cac4':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-4.png",
    'cac5':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-5.png",
    'cac6':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-6.png"
}
cac1=pygame.image.load(Paths['cac1'])
cac2=pygame.image.load(Paths['cac2'])
cac3=pygame.image.load(Paths['cac3'])
cac4=pygame.image.load(Paths['cac4'])
cac5=pygame.image.load(Paths['cac5'])
cac6=pygame.image.load(Paths['cac6'])
class Ptera(pygame.sprite.Sprite):
    def __init__(self,images):
        pygame.sprite.Sprite.__init__(self)
        self.images=images
        self.image=self.images[0]
        self.rect_1=self.image.get_rect()
        self.rect_1.left=1400
        self.speed=-5
        self.rect_1.bottom=575
        self.ref_counter=0
        self.exist=False
    def draw(self,screen):
        screen.blit(self.image,self.rect_1)
    def refresh(self):
        if self.image==self.images[0]:
            self.image=self.images[1]
        else:
            self.image=self.images[0]
    def update(self):
        self.rect_1.left+=self.speed
        if self.rect_1.right<0:
            self.exist=False
            self.rect_1.left=1400
            change = random.randint(1, 2)
            if change == 1:
                self.rect_1.bottom = 475
            else:
                self.rect_1.bottom = 505
        if self.ref_counter==10:#调节翅膀煽动频率
            self.ref_counter=0
            self.refresh()
        self.ref_counter+=1
    def spawn(self):
        if self.exist==False:
            self.spawn_num=random.randint(1,250)
        if self.spawn_num==6:
            self.exist=True
            self.spawn_num=0
class Cactus(pygame.sprite.Sprite):
    def __init__(self,images):
        pygame.sprite.Sprite.__init__(self)
        self.image=ima
    def spawn(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass
