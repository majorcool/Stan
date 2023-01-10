import pygame
import keyboard
import pygame.sprite

Image_Paths = {  # src
    'DinoDie': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-die-1.png",
    'DinoDuck1': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-duck-1.png",
    'DinoDuck2': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-duck-2.png",
    'DinoJump': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-jump.png",
    'DinoRun1': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-run-1.png",
    'DinoRun2': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-run-2.png",
    'DinoStart': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/dinosaur/dinosaur-start.png"
}


class Dino(pygame.sprite.Sprite):
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.status = 'unstarted'
        self.rect.bottom = 590
        self.rect.left = 150
        self.jump_count = -1
        self.jumped = False
        self.dino_stat = 'run'
        self.refresh_count = 0
        self.jump_spd = 20
        self.c_limit = 18
        self.d_limit = 36
        self.music_played = False
        self.d_count = 0
        self.ducked = False

    def duck(self):
        if self.dino_stat != 'jump':  # 跳的时候只作速降用，不改image
            self.ducked = True
            if self.d_count % 5 == 0:
                if self.image != self.images[4] and self.image != self.images[5]:
                    self.image = self.images[4]
                elif self.image == self.images[4]:
                    self.image = self.images[5]
                else:
                    self.image = self.images[4]  # 切换蹲着跑步的图片
            self.d_count += 1
        else:
            self.ducked = True  # 用于速降的判断

    def jump(self):
        if not self.jumped and self.dino_stat == 'jump' or self.status == "Start_Animation":
            self.jump_count += 1
            self.image = self.images[3]
            if self.jump_count <= self.c_limit:
                if self.jump_count % 6 == 0 and self.jump_count != 18:
                    self.jump_spd -= 4  # 达到重力效果（最高处速度最慢)
                self.rect.bottom -= self.jump_spd
            elif self.jump_count <= self.d_limit:
                if self.ducked:
                    if (self.jump_count + 1) % 6 != 0 and self.jump_count % 6 != 0:
                        if self.jump_count != 36 and self.jump_count % 6 == 0:
                            self.jump_spd += 4
                        self.rect.bottom += self.jump_spd * 2  # 速降
                        self.jump_count += 1
                    else:
                        if self.jump_count != 36 and self.jump_count % 6 == 0:
                            self.jump_spd += 4  # 重力效果
                        self.rect.bottom += self.jump_spd

                else:
                    if self.jump_count != 36 and self.jump_count % 6 == 0:  # 下降
                        self.jump_spd += 4
                    self.rect.bottom += self.jump_spd
            else:
                self.jumped = True
                self.music_played = False
                self.jump_count = -1
                self.jump_spd = 20
                self.image = self.images[1]
                self.dino_stat = 'run'
                if self.status == 'Start_Animation':
                    self.status = 'half_started'  # 跳完了，初始化

    def update(self):
        self.refresh_count += 1
        if self.rect.bottom == 590:  # 查看是否满足跳的条件
            self.jumped = False
        if self.dino_stat == 'run' and not self.ducked:  # 正常跑步
            if self.refresh_count % 5 == 0:
                if self.image == self.images[1]:
                    self.image = self.images[2]
                else:
                    self.image = self.images[1]
        elif self.dino_stat == 'jump':  # 跳跃
            self.jump()
        KeyInput = pygame.key.get_pressed()  # 检测按键
        if KeyInput[pygame.K_SPACE] or KeyInput[pygame.K_UP]:  # 空格和上建均可跳跃
            self.dino_stat = 'jump'
            if not self.jumped and not self.music_played:
                pygame.mixer.Sound(
                    'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/audios/jump.mp3').play()
                self.music_played = True  # 防止多次播放
        if KeyInput[pygame.K_DOWN]:  # 蹲下来
            self.duck()
        else:
            self.ducked = False  # 只有按下时才蹲

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def start(self):  # 只作开始动效使用
        if self.status == 'unstarted':
            keyboard.wait(' ')
            self.image = self.images[0]
            self.status = "Start_Animation"
        if self.status == "Start_Animation":
            self.jump()
