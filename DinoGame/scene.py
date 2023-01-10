import pygame
import random


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)

        # two same pictures
        self.image_0 = image
        self.rect_0 = self.image_0.get_rect()
        self.rect_0.left, self.rect_0.bottom = position
        self.displacement = 0
        self.image_1 = image
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.left, self.rect_1.bottom = self.rect_0.right, self.rect_0.bottom

        # pixels move each term
        self.speed = -10

    # calculate position
    def update(self):
        self.displacement += 1
        self.rect_0.left += self.speed
        self.rect_1.left += self.speed
        if self.rect_0.right < 0:
            self.rect_0.left = self.rect_1.right
            self.rect_0, self.rect_1 = self.rect_1, self.rect_0

    # draw to screen
    def draw(self, screen):
        screen.blit(self.image_0, self.rect_0)
        screen.blit(self.image_1, self.rect_1)


class Cloud(pygame.sprite.Sprite):  # pygame.sprite.Sprite is the base for any visible elements
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.images = image
        # two same pictures
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.right = 700
        # pixels move each term
        self.speed = -5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.right += self.speed
        if self.rect.right < 0:
            self.rect.left = 1400
            self.rect.y = random.randint(200, 350)
            self.speed = random.randint(-8, -5)  # 每次云位置不同，显得更自然


class Die_button(pygame.sprite.Sprite):  # GameOver后那个重开按钮
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.bottom = 350
        self.rect.left = 680
        self.rate = 0
        self.start_waiting = False

    def update(self):
        if not self.start_waiting:
            if self.rate % 5 == 0 and self.rate:
                self.image = self.images[self.rate // 5]   # 重开按钮的动效
            if self.image == self.images[7]:
                self.start_waiting = True
            self.rate += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Stars(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.speed = random.randint(1, 2)
        self.images = images
        self.image = self.images[random.randint(0, 2)]
        self.rect = self.image.get_rect()
        self.rect.bottom = random.randint(50, 300)  # 星星随机分布
        self.rect.left = random.randint(0, 1400)  # 黑夜星星随机分布

    def update(self):
        self.rect.left -= self.speed
        if self.rect.right <= -50:
            self.rect.left = 1400
            self.rect.bottom = random.randint(50, 300)
            self.image = self.images[random.randint(0, 2)]  # 随机外观的星星

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Moon(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.speed = -0.5  # 月亮移动是比较慢的
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(500, 1000)
        self.rect.bottom = 250
        self.change_skin = 1

    def update(self):
        self.rect.right += self.speed
        if self.rect.right <= 0:
            self.rect.right = 1400
            self.image = self.images[self.change_skin]
            self.change_skin += 1  # 每次切换一次月亮外观
            if self.change_skin > 6:  # 循环
                self.change_skin = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
