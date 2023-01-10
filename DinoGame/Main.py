import sys  # sys 是 python 的标准库，提供 Python 运行时环境变量的操控
from Obstacles import *
from Scorboard import *
from dino import *
from scene import *
from pygame.locals import *

# settings
FPS = 60  # 刷新率
TITLE = 'Chrome Dino'
BACKGROUND_COLOR = (235, 235, 235)  # 初始背景颜色 米白色
SCREENSIZE = (1400, 600)  # 屏幕大小 勿动
IMAGE_PATHS = {  # src
    'ground': 'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground.png',
    'cloud': 'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cloud/cloud.png',
    'bird1': 'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/pterodactyl/pterodactyl-1.png',
    'bird2': 'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/pterodactyl/pterodactyl-2.png',
    'ani_gr_1': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground——an1.png",
    'ani_gr_2': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an2.png",
    'ani_gr_3': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an3.png",
    'ani_gr_4': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an4.png",
    'ani_gr_5': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an5.png",
    'ani_gr_6': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an6.png",
    'ani_gr_7': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an7.png",
    'ani_gr_8': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an8.png",
    'ani_gr_9': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an9.png",
    'ani_gr_10': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an10.png",
    'ani_gr_11': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ground/ground-an11.png",
    'Start_Hint': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/StartHint.png",
    'gg': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ending/game-over.png",
    'end_pic1': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ending/restart-1.png",
    'end_pic2': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ending/restart-2.png",
    'end_pic3': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ending/restart-3.png",
    'end_pic4': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ending/restart-4.png",
    'end_pic5': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ending/restart-5.png",
    'end_pic6': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ending/restart-6.png",
    'end_pic7': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ending/restart-7.png",
    'end_pic8': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/ending/restart-8.png",
    'star1': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/star/star-1.png",
    'star2': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/star/star-2.png",
    'star3': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/star/star-3.png",
    'Moon1': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/moon/moon-1.png",
    'Moon2': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/moon/moon-2.png",
    'Moon3': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/moon/moon-3.png",
    'Moon4': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/moon/moon-4.png",
    'Moon5': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/moon/moon-5.png",
    'Moon6': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/moon/moon-6.png",
    'Moon7': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/moon/moon-7.png",
    'Cloud-Night': "C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/cloud/cloud-night.png"
}
Moon1 = pygame.image.load(IMAGE_PATHS['Moon1'])  # 各种导入
Moon2 = pygame.image.load(IMAGE_PATHS['Moon2'])
Moon3 = pygame.image.load(IMAGE_PATHS['Moon3'])
Moon4 = pygame.image.load(IMAGE_PATHS['Moon4'])
Moon5 = pygame.image.load(IMAGE_PATHS['Moon5'])
Moon6 = pygame.image.load(IMAGE_PATHS['Moon6'])
Moon7 = pygame.image.load(IMAGE_PATHS['Moon7'])
e_1 = pygame.image.load(IMAGE_PATHS['end_pic1'])
e_2 = pygame.image.load(IMAGE_PATHS['end_pic2'])
e_3 = pygame.image.load(IMAGE_PATHS['end_pic3'])
e_4 = pygame.image.load(IMAGE_PATHS['end_pic4'])
e_5 = pygame.image.load(IMAGE_PATHS['end_pic5'])
e_6 = pygame.image.load(IMAGE_PATHS['end_pic6'])
e_7 = pygame.image.load(IMAGE_PATHS['end_pic7'])
e_8 = pygame.image.load(IMAGE_PATHS['end_pic8'])
GG = pygame.image.load(IMAGE_PATHS['gg'])
Start_Hint = pygame.image.load(IMAGE_PATHS['Start_Hint'])
an1 = pygame.image.load(IMAGE_PATHS['ani_gr_1'])
an2 = pygame.image.load(IMAGE_PATHS['ani_gr_2'])
an3 = pygame.image.load(IMAGE_PATHS['ani_gr_3'])
an4 = pygame.image.load(IMAGE_PATHS['ani_gr_4'])
an5 = pygame.image.load(IMAGE_PATHS['ani_gr_5'])
an6 = pygame.image.load(IMAGE_PATHS['ani_gr_6'])
an7 = pygame.image.load(IMAGE_PATHS['ani_gr_7'])
an8 = pygame.image.load(IMAGE_PATHS['ani_gr_8'])
an9 = pygame.image.load(IMAGE_PATHS['ani_gr_9'])
an10 = pygame.image.load(IMAGE_PATHS['ani_gr_10'])
an11 = pygame.image.load(IMAGE_PATHS['ani_gr_11'])
ground_image = pygame.image.load(IMAGE_PATHS['ground'])
cloud_image = pygame.image.load(IMAGE_PATHS['cloud'])
bird1 = pygame.image.load(IMAGE_PATHS['bird1'])
bird2 = pygame.image.load(IMAGE_PATHS['bird2'])
zero = pygame.image.load(SC_IMAGES['0'])
one = pygame.image.load(SC_IMAGES['1'])
two = pygame.image.load(SC_IMAGES['2'])
three = pygame.image.load(SC_IMAGES['3'])
four = pygame.image.load(SC_IMAGES['4'])
five = pygame.image.load(SC_IMAGES['5'])
six = pygame.image.load(SC_IMAGES['6'])
seven = pygame.image.load(SC_IMAGES['7'])
eight = pygame.image.load(SC_IMAGES['8'])
nine = pygame.image.load(SC_IMAGES['9'])
HI = pygame.image.load(SC_IMAGES['HI'])
blank = pygame.image.load(SC_IMAGES['Blank'])
dino_die = pygame.image.load(Image_Paths['DinoDie'])
dino_duck1 = pygame.image.load(Image_Paths['DinoDuck1'])
dino_duck2 = pygame.image.load(Image_Paths['DinoDuck2'])
dino_jump = pygame.image.load(Image_Paths['DinoJump'])
dino_run1 = pygame.image.load(Image_Paths['DinoRun1'])
dino_run2 = pygame.image.load(Image_Paths['DinoRun2'])
dino_start = pygame.image.load(Image_Paths['DinoStart'])
Star1 = pygame.image.load(IMAGE_PATHS['star1'])
Star2 = pygame.image.load(IMAGE_PATHS['star2'])
Star3 = pygame.image.load(IMAGE_PATHS['star3'])
cloud_night = pygame.image.load(IMAGE_PATHS['Cloud-Night'])


class Ani_Ground(pygame.sprite.Sprite):  # pygame.sprite.Sprite is the base for any visible elements, 此类是过场动画
    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.rect.left = 0
        self.counter = 0
        self.finished = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if not self.finished:
            self.counter += 1
            if self.counter != 0 and self.counter % 50 == 0:
                self.image = self.images[self.counter // 100]
            if self.counter == 550:
                self.finished = True
                dino.status = 'started'


# 内部各功能模块进行初始化创建及变量设置，默认调用
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)
music_played = False
clock = pygame.time.Clock()
ground = Ground(ground_image, (0, SCREENSIZE[1]))
cloud = Cloud([cloud_image, cloud_night])
ptera = Ptera([bird1, bird2])
ani_gr = Ani_Ground([an1, an2, an3, an4, an5, an6, an7, an8, an9, an10, an11, ground_image])
scoreboard = ScoreBoard([zero, one, two, three, four, five, six, seven, eight, nine, HI, blank])
dino = Dino([dino_start, dino_run1, dino_run2, dino_jump, dino_duck1, dino_duck2, dino_die])
end_butt = Die_button([e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8])
Star = Stars([Star1, Star2, Star3])
Star_2 = Stars([Star1, Star2, Star3])
Star_3 = Stars([Star1, Star2, Star3])
Star_4 = Stars([Star1, Star2, Star3])
end_butt2 = Die_button([e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8])
end_butt2.rect.bottom = 450
Cac = Cactus([cac1, cac2, cac3, cac4, cac5, cac6])
Cac2 = Cactus([cac1, cac2, cac3, cac4, cac5, cac6])  # 各类初始化
screen.fill(BACKGROUND_COLOR)
moon = Moon([Moon1, Moon2, Moon3, Moon4, Moon5, Moon6, Moon7])
f = pygame.font.Font(None, 50)  # 用于显示开始字体
f2 = pygame.font.Font(None, 20)  # 用于显示结束字体
text = f.render("Press Space To Start", True, (154, 160, 166), (235, 235, 235))  # 开始字体
text2 = f2.render("Slow Mode", True, (154, 160, 166), None)  # 结束字体
file = open('High Score.txt')  # 记录最高分
scoreboard.Highscore = int(file.readline().rstrip())
file.close()
screen.blit(text, (100, 100))
dino.draw(screen)
pygame.display.update()  # 刷新开始页面的恐龙
bg_change_score_min = 500  # 黑天开始
bg_change_score_max = 1000  # 黑天结束
Score_Changed = False
accelerate_spd = 2  # 随着时间加速事物运动
Night = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP and dino.status == 'dead':  # 判断是否按下鼠标
            mouse_up = event.button
            mouse_up_x, mouse_up_y = event.pos
            if 680 <= mouse_up_x <= 752 and 286 <= mouse_up_y <= 350:  # 判断按下鼠标的位置是否是重新开始游戏按钮
                Score_Changed = False
                dino.status = 'started'
                Cac.rect.right = -100
                Cac2.rect.right = -100
                ptera.exist = False
                ptera.rect.left = 1400
                scoreboard.score = 0
                Cac.speed = -10
                Cac2.speed = -10
                ground.speed = -10
                ptera.speed = -8
                accelerate_spd = 2  # 正常速度2
                BACKGROUND_COLOR = (235, 235, 235)  # 初始化/重开
                Night = False
            if 680 <= mouse_up_x <= 752 and 386 <= mouse_up_y <= 450:  # 判断鼠标按下位置是否是重新开始慢速模式游戏按钮
                Score_Changed = False
                dino.status = 'started'
                Cac.rect.right = -100
                Cac2.rect.right = -100
                ptera.rect.left = 1400
                ptera.exist = False
                scoreboard.score = 0
                Cac.speed = -10
                Cac2.speed = -10
                ground.speed = -10
                ptera.speed = -8
                BACKGROUND_COLOR = (235, 235, 235)
                accelerate_spd = 1  # 慢速模式所以是1
                Night = False
    if dino.status == "unstarted" or dino.status == "Start_Animation":  # 按下空格开始进入ground的动画
        screen.fill(BACKGROUND_COLOR)
        dino.start()
        dino.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
    elif dino.status == 'half_started':  # 进入ground动画
        dino.dino_stat = 'run'
        screen.fill(BACKGROUND_COLOR)
        dino.update()
        dino.draw(screen)
        ani_gr.update()
        ani_gr.draw(screen)
        pygame.display.update()
    elif dino.status == "started":  # 游戏正式开始
        screen.fill(BACKGROUND_COLOR)
        if scoreboard.score > 0:  # 调这个数来决定从什么时候开始计算碰撞
            if pygame.sprite.collide_mask(dino, Cac) or pygame.sprite.collide_mask(dino,
                                                                                   Cac2) or pygame.sprite.collide_mask(
                dino,
                ptera):
                dino.image = dino.images[6]  # 切换死亡图片
                dino.status = 'dead'  # 如果检测到碰撞就死亡
                pygame.mixer.Sound(
                    'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/audios/die.mp3').play()
        if not Night:  # 白天
            if list(BACKGROUND_COLOR)[0] != 235:  # 没有变色完就一直变色
                BACKGROUND_COLOR = list(BACKGROUND_COLOR)
                BACKGROUND_COLOR[0] += 2
                BACKGROUND_COLOR[1] += 2
                BACKGROUND_COLOR[2] += 2
                BACKGROUND_COLOR = tuple(BACKGROUND_COLOR)  # 通过加减rgb形成渐变动画的效果
            cloud.image = cloud.images[0]  # 白天的云
            cloud.speed = -5  # 白天云速度比较快
            cloud.update()
            cloud.draw(screen)
        else:  # 夜晚
            if list(BACKGROUND_COLOR)[0] != 33:  # 渐变效果
                BACKGROUND_COLOR = list(BACKGROUND_COLOR)
                BACKGROUND_COLOR[0] -= 2
                BACKGROUND_COLOR[1] -= 2
                BACKGROUND_COLOR[2] -= 2
                BACKGROUND_COLOR = tuple(BACKGROUND_COLOR)
            if BACKGROUND_COLOR == (33, 33, 33):  # 这里特殊判断一下是因为晚上的云的背景没扣图
                cloud.speed = -3  # 晚上的云比较慢
                cloud.image = cloud.images[1]  # 晚上的云
                cloud.update()
                cloud.draw(screen)
            moon.update()
            moon.draw(screen)
            Star.update()
            Star_2.update()
            Star_3.update()
            Star_4.update()
            Star_2.draw(screen)
            Star_3.draw(screen)
            Star_4.draw(screen)
            Star.draw(screen)
        if dino.status != 'dead':  # 死了就不换图防止结束后恐龙不是死亡图
            dino.update()
        dino.draw(screen)
        ground.draw(screen)
        ground.update()
        if Cac.rect.left <= 1250 and Cac.wait_counter >= 40:  # 防止出现仙人掌重叠以及过于密集导致难度太大
            Cac2.spawn()
        Cac.spawn()
        if Cac.exist:
            Cac.update()
            Cac.draw(screen)
        if Cac2.exist:
            Cac2.update()
            Cac2.draw(screen)
        if bg_change_score_min <= scoreboard.score <= bg_change_score_max:  # 夜晚
            Night = True
        elif BACKGROUND_COLOR == (33, 33, 33):  # 白天
            Night = False
            bg_change_score_min += 1000
            bg_change_score_max += 1000  # 把夜晚往后调整
        if scoreboard.score >= 300:  # 300分后开始有鸟，仙人掌也出现了4连个
            ptera.spawn()
            Cac.spawn_random_max = 5
            Cac2.spawn_random_max = 5  # 5代表仙人掌的第6张图开始出现
        if ptera.exist:
            ptera.update()
            ptera.draw(screen)
        if scoreboard.score and not scoreboard.score % 100:  # 每次一百停一下
            scoreboard.calculate()  # 改分数
            if not music_played:  # 防止重复播放
                pygame.mixer.Sound(
                    'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/audios/score.mp3').play()
                # sound
                music_played = True
            scoreboard.flicker(screen)  # 分数闪烁特效
        else:
            music_played = False
            scoreboard.calculate()
            scoreboard.draw(screen)
        if scoreboard.SPD_Plus:  # 满足条件后所有事物的speed加快
            if Cac.speed >= -22:  # 限制最高速度
                Cac.speed -= accelerate_spd
                Cac2.speed -= accelerate_spd
                ground.speed -= accelerate_spd
                ptera.speed -= accelerate_spd
        if scoreboard.score >= 99999:  # 到100000就变0
            scoreboard.score = 0
        pygame.display.update()
        clock.tick(FPS)
    else:
        if scoreboard.score > scoreboard.Highscore:  # 记录最高分
            scoreboard.Highscore = scoreboard.score
            file = open('High Score.txt', mode='w')  # 记录到文件里
            file.write(str(scoreboard.score))
            file.close()
        screen.blit(GG, (520, 230))
        screen.blit(text2, (682, 450))
        end_butt.update()
        end_butt2.update()
        end_butt.draw(screen)
        end_butt2.draw(screen)  # 各种按钮提示(重开)
        pygame.display.update()
        clock.tick(FPS)
