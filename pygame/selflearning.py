import pygame
import sys  # sys 是 python 的标准库，提供 Python 运行时环境变量的操控
import pygame.gfxdraw#导入pygame不会自动导入gfxdraw,需要手动导入
# 内部各功能模块进行初始化创建及变量设置，默认调用
pygame.init()
pygame.display.init()#初始化模块
print(pygame.display.get_init())#如果已初始化显示模块，则返回True
pygame.display.quit()#取消初始化模块
# 设置游戏窗口大小，分别是宽度和高度
size = width, height = 800, 600
print(pygame.display.get_surface())
# 初始化显示窗口
screen = pygame.display.set_mode(size)#初始化屏幕或者窗口以供显示
# 设置显示窗口的标题内容，str 类型
pygame.display.set_caption('Hello World')#设置当前窗口标题
print(pygame.display.get_caption())#获取当前窗口标题
white=255,255,255#白色
red=255,0,0
pygame.draw.rect(screen,white,(200,10,200,200))#画一个长方形，前两个数值是坐标，后两个是width和height
pygame.draw.polygon(screen,red,((10,20),(90,20),(50,80)))#画多边形，数值是顶点坐标
pygame.draw.circle(screen,red,(100,200),30)#画一个圆，第一个坐标是圆心，30是radius
pygame.gfxdraw.pixel(screen,50,600,red)#画一个像素点(surface,x,y,color)
pygame.gfxdraw.rectangle(screen,(200,10,200,200),red)#画一个长方形(x,y,width,height)
pygame.gfxdraw.aacircle(screen,500,400,30,red)#画一个反锯齿圆(surfacem,x,y,radius,color)
pygame.gfxdraw.pie(screen,200,400,30,70,180,red)#画一个馅饼,(surface,x,y,radius,start_angle,stop_angle)
f=pygame.font.Font(None,25)
Print=f.render('HelloWorld',True,white)
pos=Print.get_rect()
screen.blit(Print,pos)
pygame.display.flip()#将完整显示面更新到屏幕上
pygame.display.update()#更新屏幕的软件显示部分
print(pygame.display.get_driver())#获取游戏显示后端的名称
pygame.display.Info()#创建视频显示信息对象
print(pygame.display.get_wm_info())#获取有关当前窗口系统的信息
#pygame.display.mode_ok() 选择显示模式的最佳颜色深度
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