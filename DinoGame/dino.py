import pygame
import random
import keyboard
import pygame.sprite
Image_Paths={
    'DinoDie':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-die-1.png",
    'DinoDuck1':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-duck-1.png",
    'DinoDuck2':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-duck-2.png",
    'DinoJump':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-jump.png",
    'DinoRun1':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-run-1.png",
    'DinoRun2':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-run-2.png",
    'DinoStart':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-start.png"
}
class Dino(pygame.sprite.Sprite):
    def __init__(self,images):
        pygame .sprite.Sprite.__init__(self)
        self.images=images
        self.image=self.images[0]
        self.rect=self.image.get_rect()
        self.status='unstarted'
        self.rect.bottom=590
        self.rect.left=150
        self.jump_count=0
        self.jumped=False
        self.dino_stat='run'
        self.refresh_count=0
        self.jump_spd=1
        self.c_limit=150
        self.d_limit=301
        self.music_played=False
        self.d_count=0
        self.ducked=False
    def duck(self):
        self.ducked=True
        if self.d_count%5==0:
            if self.image!=self.images[4] and self.image!=self.images[5]:
                self.image=self.images[4]
            elif self.image==self.images[4]:
                self.image=self.images[5]
            else:
                self.image=self.images[4]
        self.d_count+=1
    def jump(self):
        if self.jumped==False and self.dino_stat=='jump' or self.status=="Start_Animation":
            if self.ducked==False:
                self.image=self.images[3]
            if self.jump_count<=self.c_limit:
                self.rect.bottom-=self.jump_spd
            elif self.jump_count<=self.d_limit:
                self.rect.bottom+=self.jump_spd
            else:
                self.jumped=True
                self.music_played=False
                self.jump_count=0
                self.image=self.images[1]
                self.dino_stat='run'
                if self.status=='Start_Animation':
                    self.status='half_started'
            self.jump_count+=1

    def update(self):
        self.refresh_count+=1
        if self.rect.bottom==590:
            self.jumped=False
        if self.dino_stat=='run' and self.ducked==False:
            if self.refresh_count%5==0:
                if self.image==self.images[1]:
                    self.image=self.images[2]
                else:
                    self.image=self.images[1]
        elif self.dino_stat=='jump':
            self.jump()

        KeyInput=pygame.key.get_pressed()
        if KeyInput[pygame.K_SPACE] or KeyInput[pygame.K_UP]:
            self.dino_stat='jump'
            if self.jumped==False and self.music_played==False:
                pygame.mixer.Sound(
                    'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/audios/jump.mp3').play()
                self.music_played=True
        if KeyInput[pygame.K_DOWN]:
            self.duck()
        else:
            self.ducked=False


    def draw(self,screen):
        screen.blit(self.image,self.rect)
    def start(self):
        if self.status=='unstarted':
            keyboard.wait(' ')
            self.image=self.images[0]
            self.status="Start_Animation"
        if self.status=="Start_Animation":
            self.jump()


