import pygame
import random

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
        pygame .sprite.Sprite.__init__()
        self.images=images[0]
        self.rect=self.images.get_rect()
    def duck(self):
        pass
    def jump(self):
        pass
    def update(self):
        pass
    def draw(self,screen):
        pass