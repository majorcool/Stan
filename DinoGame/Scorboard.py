import pygame
SC_IMAGES={'0':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-0.png',
'1':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-1.png',
'2':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-2.png',
'3':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-3.png',
'4':"C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-4.png",
'5':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-5.png',
'6':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-6.png',
'7':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-7.png',
'8':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-8.png',
'9':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-9.png',
'HI':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/scoreboard-10.png',
'Blank':'C:/Users/17354/Desktop/pythonProject/DinoGame/resources/resources/images/scoreboard/blank.png'
}
class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self,images):
        self.cal_img=images
        pygame.sprite.Sprite.__init__(self)
        self.score=0
        self.images_0=self.cal_img[0]
        self.rect_0=self.images_0.get_rect()
        self.rect_0.left=1160
        self.rect_0.bottom=50
        self.images_1=self.cal_img[0]
        self.rect_1=self.images_1.get_rect()
        self.rect_1.left=1180
        self.rect_1.bottom=50
        self.images_2=self.cal_img[0]
        self.rect_2=self.images_2.get_rect()
        self.rect_2.left=1200
        self.rect_2.bottom=50
        self.images_3=self.cal_img[0]
        self.rect_3=self.images_3.get_rect()
        self.rect_3.left=1220
        self.rect_3.bottom=50
        self.images_4=self.cal_img[0]
        self.rect_4=self.images_4.get_rect()
        self.rect_4.left=1240
        self.rect_4.bottom=50
        self.images_5=self.cal_img[0]
        self.image_HI=images[10]
        self.rect_HI=self.image_HI.get_rect()
        self.rect_HI.left=970
        self.rect_HI.bottom=50
        self.image_HI_0=images[0]
        self.image_HI_0_rect=self.image_HI_0.get_rect()
        self.image_HI_0_rect.left=1040
        self.image_HI_0_rect.bottom=50
        self.image_HI_1=images[0]
        self.image_HI_1_rect=self.image_HI_1.get_rect()
        self.image_HI_1_rect.left=1060
        self.image_HI_1_rect.bottom=50
        self.image_HI_2=images[0]
        self.image_HI_2_rect=self.image_HI_2.get_rect()
        self.image_HI_2_rect.left=1080
        self.image_HI_2_rect.bottom=50
        self.image_HI_3=images[0]
        self.image_HI_3_rect=self.image_HI_3.get_rect()
        self.image_HI_3_rect.left=1100
        self.image_HI_3_rect.bottom=50
        self.image_HI_4=images[0]
        self.image_HI_4_rect=self.image_HI_4.get_rect()
        self.image_HI_4_rect.left=1120
        self.image_HI_4_rect.bottom=50
        self.count=0
        self.flick_counter=0
    def draw(self,screen):
        self.count+=1
        screen.blit(self.images_0,self.rect_0)
        screen.blit(self.images_1,self.rect_1)
        screen.blit(self.images_2,self.rect_2)
        screen.blit(self.images_3,self.rect_3)
        screen.blit(self.images_4,self.rect_4)
        screen.blit(self.image_HI,self.rect_HI)
        screen.blit(self.image_HI_0,self.image_HI_0_rect)
        screen.blit(self.image_HI_1,self.image_HI_1_rect)
        screen.blit(self.image_HI_2,self.image_HI_2_rect)
        screen.blit(self.image_HI_3,self.image_HI_3_rect)
        screen.blit(self.image_HI_4,self.image_HI_4_rect)

        if self.count and self.count%7==0:
            self.score+=1
    def calculate(self):
        self.images_4=self.cal_img[self.score%10]
        self.images_3=self.cal_img[(self.score%100)//10]
        self.images_2=self.cal_img[(self.score%1000)//100]
        self.images_1=self.cal_img[(self.score%10000)//1000]
        self.images_0=self.cal_img[self.score//10000]
    def flicker(self,screen):
        screen.blit(self.image_HI,self.rect_HI)
        screen.blit(self.image_HI_0,self.image_HI_0_rect)
        screen.blit(self.image_HI_1,self.image_HI_1_rect)
        screen.blit(self.image_HI_2,self.image_HI_2_rect)
        screen.blit(self.image_HI_3,self.image_HI_3_rect)
        screen.blit(self.image_HI_4,self.image_HI_4_rect)
        self.flick_counter+=1
        if self.flick_counter>=20 and self.flick_counter<=30 or self.flick_counter>=50 and self.flick_counter<=60 or self.flick_counter>=70 and self.flick_counter<=80 or self.flick_counter>=90:
            screen.blit(self.images_0, self.rect_0)
            screen.blit(self.images_1, self.rect_1)
            screen.blit(self.images_2, self.rect_2)
            screen.blit(self.images_3, self.rect_3)
            screen.blit(self.images_4, self.rect_4)
        if self.flick_counter>=130:
            self.score+=self.flick_counter//7
            self.flick_counter=0

