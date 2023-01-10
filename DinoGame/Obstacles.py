import random
import pygame

Paths = {  # src
    'cac1': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-1.png",
    'cac2': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-2.png",
    'cac3': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-3.png",
    'cac4': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-4.png",
    'cac5': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-5.png",
    'cac6': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cactus/cactus-6.png"
}
cac1 = pygame.image.load(Paths['cac1'])
cac2 = pygame.image.load(Paths['cac2'])
cac3 = pygame.image.load(Paths['cac3'])
cac4 = pygame.image.load(Paths['cac4'])
cac5 = pygame.image.load(Paths['cac5'])
cac6 = pygame.image.load(Paths['cac6'])


class Ptera(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left = 1400
        self.speed = -8
        self.rect.bottom = 575
        self.ref_counter = 0
        self.exist = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def refresh(self):  # 扇动翅膀
        if self.image == self.images[0]:
            self.image = self.images[1]
        else:
            self.image = self.images[0]

    def update(self):
        self.rect.left += self.speed
        if self.rect.right < 0:
            self.exist = False
            self.rect.left = 1400
        if self.ref_counter == 10:  # 调节翅膀煽动频率
            self.ref_counter = 0
            self.refresh()
        self.ref_counter += 1

    def spawn(self):  # 生成鸟
        if not self.exist:
            self.spawn_num = random.randint(1, 250)
        if self.spawn_num == 6:  # 1/250的概率生成1个鸟
            self.exist = True
            self.spawn_num = 0
            choose_num = random.randint(0, 1)
            if choose_num == 1:  # 只有两个高度，一个必须跳，一个必须蹲，用于降低难度
                self.rect.bottom = 530
            else:
                self.rect.bottom = 580


class Cactus(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.spawn_num = 0
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left = 1400
        self.rect.bottom = 575
        self.speed = -10
        self.exist = False
        self.spawn_random_max = 4  # 300分一下只能出现前四种仙人掌，防止难度过大
        self.wait_counter = 0

    def spawn(self):
        if not self.exist:
            self.spawn_num = random.randint(1, 150)  # 1/150的概率生成，因为仙人掌比较常见
        if self.spawn_num == 6:
            self.wait_counter = 0
            self.exist = True
            self.spawn_num = 0
            Random_Image = random.randint(0, self.spawn_random_max)
            self.image = self.images[Random_Image]
            if Random_Image == 0 or Random_Image == 1 or Random_Image == 2:  # 根据每个仙人掌的高度不同来调整rect
                self.rect.bottom = 585
            else:
                self.rect.bottom = 560

    def update(self):
        if self.exist:
            self.wait_counter += 1
            self.rect.left += self.speed
            if self.rect.right < -100:
                self.rect.left = 1400
                self.exist = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
