import pygame
import sys  # sys 是 python 的标准库，提供 Python 运行时环境变量的操控
import random
# settings
FPS = 60
TITLE = 'Chrome Dino'
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
IMAGE_PATHS = {
    'ground': 'C:/Users/17354/Desktop/ground.png',
    'cloud': 'C:/Users/17354/Desktop/cloud.png',
}
ground_image=pygame.image.load(IMAGE_PATHS['ground'])
cloud_image=pygame.image.load(IMAGE_PATHS['cloud'])
class Dinosaur:
    def __init__(self):
        pass
    def jump(self):
        pass
    def duck(self):
        pass
    def unduck(self):
        pass
    def die(self):
        pass
    def draw(self,status):
        pass
    def load_image(self):
        pass
    def update(self):
        pass
class obstacle:
    def __init__(self):
        pass
class Cactus(obstacle):
    def __init__(self):
        super(Cactus, self).__init__()
    def draw(self,pos):
        pass
    def update(self):
        pass
class Ptera(obstacle):
    def __init__(self):
        super(Ptera, self).__init__()
    def draw(self,pos):
        pass
    def update(self):
        pass
class Scene:
    def __init__(self):
        pass
class Ground(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)

        # two same pictures
        self.image_0 = image
        self.rect_0 = self.image_0.get_rect()
        self.rect_0.left, self.rect_0.bottom = position

        self.image_1 = image
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.left, self.rect_1.bottom = self.rect_0.right, self.rect_0.bottom

        # pixels move each term
        self.speed = -10

    # calculate position
    def update(self):
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
        self.speed = -10
    def draw(self,pos):
        screen.blit(self.image, self.rect)
    def update(self):
        self.rect.right += self.speed
        if self.rect.right < 0:
            self.rect.right=700
            self.rect.y=random.randint(20,90)
            self.speed=random.randint(-15,-5)
class Scoreboard(Scene):
    def __init__(self):
        super(Scoreboard, self).__init__()
    def set_score(self,score):
        pass
    def draw(self,score):
        pass

# 内部各功能模块进行初始化创建及变量设置，默认调用
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
ground=Ground(ground_image,(0,SCREENSIZE[1]))
cloud=Cloud(cloud_image)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BACKGROUND_COLOR)
    cloud.draw(screen)
    cloud.update()
    ground.draw(screen)
    ground.update()
    pygame.display.update()
    clock.tick(FPS)