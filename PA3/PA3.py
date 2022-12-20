import pygame
import sys  # sys 是 python 的标准库，提供 Python 运行时环境变量的操控
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
class Ground(Scene):
    def __init__(self):
        super(Ground, self).__init__()
    def draw(self,pos):
        pass
    def update(self):
        pass
class Cloud(Scene):
    def __init__(self):
        super(Cloud, self).__init__()
    def draw(self,pos):
        pass
    def update(self):
        pass
class Scoreboard(Scene):
    def __init__(self):
        super(Scoreboard, self).__init__()
    def set_score(self,score):
        pass
    def draw(self,score):
        pass
# 内部各功能模块进行初始化创建及变量设置，默认调用
pygame.init()

# 设置游戏窗口大小，分别是宽度和高度
size = width, height = 800, 600

# 初始化显示窗口
screen = pygame.display.set_mode(size)

# 设置显示窗口的标题内容，str 类型
pygame.display.set_caption('DinoGame')

# 无限循环，直到 Python 运行时退出结束
while True:

    # 从 Pygame 的事件队列中取出事件，并从队列中删除该事件
    for event in pygame.event.get():

        # 获得事件类型，并逐类响应
        if event.type == pygame.QUIT:
            # 用于退出结束游戏并退出
            sys.exit()

    # 对显示窗口进行更新，默认窗口全部重绘
    pygame.display.update()