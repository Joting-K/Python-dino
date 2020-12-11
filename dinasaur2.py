import numpy as np 
import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import pickle
import pygame
from pygame.locals import  *  #加载pygame中所有常量
from pygame.locals import  QUIT
from itertools import cycle   #迭代工具
import random
import sys 
import tkinter.font as Font


class GUI():
    def __init__(self):
        pass
    def gui(self):
        self.gui= tk.Tk()
        self.gui.geometry("1250x570+30+30") 
        self.gui.title('小恐龍遊戲')
        
        self.canvas = tk.Canvas(self.gui, bg = 'white', height = 500, width = 500)
        self.canvas.place(x = 220, y = 30)

        x = 20
        y = 30
        xgap = 100
        ygap = 35
        i = 0
        self.role_label = tk.Label(self.gui, text = '角色選擇', font = (20))
        self.role_label.place(x = x, y = y + i*ygap)

        self.role_combobox = ttk.Combobox(self.gui, textvariable = tk.StringVar(),font = (20))
        self.role_combobox["value"] = ('小恐龍')
        self.role_combobox.current(0)
        self.role_combobox.place(x = x + xgap, y = y + i*ygap, width = 150)
        i += 2
        
        self.name_label = tk.Label(self.gui, text = '輸入名字', font = (20))
        self.name_label.place(x = x , y = y + i*ygap)
        

        self.name_entry = tk.Entry(self.gui,font = (20))
        self.name_entry.place(x = x + xgap, y = y + i*ygap, width = 150)
        i += 2

        self.type_label = tk.Label(self.gui, text = '關卡種類', font = (20))
        self.type_label.place(x = x, y = y + i*ygap)

        self.type_combobox = ttk.Combobox(self.gui, textvariable = tk.StringVar(),font = (20))
        self.type_combobox["value"] = ('視覺關','聽覺關')
        self.type_combobox.current(0)
        self.type_combobox.place(x = x + xgap, y = y + i*ygap, width = 150)
        i += 2

        self.difficulty_label = tk.Label(self.gui, text = '關卡難度',font = (20))
        self.difficulty_label.place(x = x, y =  y + i*ygap)
        
        self.difficulty_combobox = ttk.Combobox(self.gui, textvariable = tk.StringVar(),font = (20))
        self.difficulty_combobox["value"] = ('簡單','普通','難','超難')
        self.difficulty_combobox.current(0)
        self.difficulty_combobox.place(x = x + xgap, y = y + i*ygap, width = 150)
        i += 2

        
        self.sound_label = tk.Label(self.gui, text = '關卡聲音',font = (20))
        self.sound_label.place(x = x, y = y + i*ygap) 
        self.sound_combobox = ttk.Combobox(self.gui, textvariable = tk.StringVar(),font = (20))
        self.sound_combobox["value"] = ['google 小姐']
        self.sound_combobox.current(0)
        self.sound_combobox.place(x = x + xgap, y = y + i*ygap, width = 150)
        i += 2

        self.ok_button =  tk.Button(self.gui, command = self.do_ok, text = 'Start',font = (20))
        self.ok_button.place(x = x + xgap, y = y + i*ygap, width = 150)
        i += 2

        self.score_label = tk.Label(self.gui, text = '記分板', font = (50))
        self.score_label.place(x = 700, y = 10)
        cols_name = ['名次','姓名', '關卡種類', '難度', "聲音", '得分']
        style_head = ttk.Style()
        style_head.configure("Treeview.Heading", font=(20))
        style_head.configure("Treeview", font=(20))
        self.table = ttk.Treeview(self.gui, columns=cols_name, show='headings', height = 30)
        for col in cols_name:
            self.table.column(col, minwidth=0,width=150, stretch=False,)
        
        for col in cols_name:
            self.table.heading(col, text=col)
        self.table.place(x = 320, y = 50)
        
        self.gui.mainloop()
        
        
        
     
    def do_ok(self):
        if self.type_combobox.get()=='視覺關':
            SCREENWITDH=800   #宽度
            SCREENHEIGHT=260  #高度
            FPS=30  #更新画面的时间
            
            #定义一个地图类
            class MyMap:
                #加载背景图片
                def __init__(self,x,y):
                    self.bg=pygame.image.load("image/bg.png")
                    self.x=x
                    self.y=y
                def map_rolling(self):
                    if self.x<-790: #说明地图已经移动完毕
                        self.x=800  #给地图新坐标
                    else:
                        self.x -=5  # 移动5个像素
                #更新地图
                def map_update(self):
                    SCREEN.blit(self.bg,(self.x,self.y))
            
            #恐龙类
            class Dinasaur:
                def __init__(self):
                    #初始化小恐龙矩形
                    self.rect=pygame.Rect(0,0,0,0)
                    self.jumpState=False  #跳跃的状态
                    self.jumpHeight=140   #跳跃高度
                    self.lowest_y=140     #最低坐标
                    self.jumpValue=0      #跳跃增变量
                    self.dinasaurIndex=0
                    self.dinasaurIndexGen=cycle([0,1,2])
                    self.dinasaur_image=(pygame.image.load('image/dinosaur1.png').convert_alpha(),
                                         pygame.image.load('image/dinosaur2.png').convert_alpha(),
                                         pygame.image.load('image/dinosaur3.png').convert_alpha(),)
                    self.jump_audio=pygame.mixer.Sound('audio/jump.wav') #加载音效
                    self.rect.size=self.dinasaur_image[0].get_size()     #设置小恐龙矩形大小
                    self.x=50                                            #设置小恐龙的x坐标
                    self.y=self.lowest_y                                 #设置小恐龙的y坐标
                    self.rect.topleft=(self.x,self.y)                    #设置左上角为准
                #跳跃
                def jump(self):
                    self.jumpState=True
                #小恐龙的移动
                def move(self):
                    if self.jumpState:      #可以起跳
                        if self.rect.y>=self.lowest_y:
                            self.jumpValue =- 5  #以5个像素向上移动
                        if self.rect.y<=self.lowest_y-self.jumpHeight:
                            self.jumpValue=5
                        self.rect.y+=self.jumpValue #通过循环改变恐龙的Y值
                        if self.rect.y >=self.lowest_y:#恐龙回到地面
                            self.jumpState=False        #关闭跳跃状态
                #绘制恐龙
                def draw_dinasour(self):
                    #匹配恐龙动图
                    dinasaurindex=next(self.dinasaurIndexGen)
                    #实现绘制
                    SCREEN.blit(self.dinasaur_image[dinasaurindex],(self.x,self.rect.y))
            
            #障碍物类
            class Obstacle:
                score=1 #分数
                def __init__(self):
                    #初始化障碍物的矩形
                    self.rect=pygame.Rect(0,0,0,0)
                    #加载障碍物的图片
                    self.stone=pygame.image.load('image/stone.png').convert_alpha() #加载石头
                    self.cacti=pygame.image.load('image/cacti.png').convert_alpha() #加载仙人掌
                    # 加载分数图片
                    self.numbers=(pygame.image.load('image/0.png').convert_alpha(), #convert_alpha()透明度
                                  pygame.image.load('image/1.png').convert_alpha(),
                                  pygame.image.load('image/2.png').convert_alpha(),
                                  pygame.image.load('image/3.png').convert_alpha(),
                                  pygame.image.load('image/4.png').convert_alpha(),
                                  pygame.image.load('image/5.png').convert_alpha(),
                                  pygame.image.load('image/6.png').convert_alpha(),
                                  pygame.image.load('image/7.png').convert_alpha(),
                                  pygame.image.load('image/8.png').convert_alpha(),
                                  pygame.image.load('image/9.png').convert_alpha(),
                                  )
                    #加载加分的音效
                    self.score_audio=pygame.mixer.Sound('audio/score.wav')
                    #创建0，1之间的随机数,0是石头，1是仙人掌
                    r=random.randint(0,1)
                    if r ==0:
                        self.image=self.stone
                    else:
                        self.image=self.cacti
                    #根据障碍物位图的宽高设置矩形
                    self.rect.size=self.image.get_size()
                    #获取位图的宽高
                    self.width,self.height=self.rect.size
                    #障碍物绘制坐标
                    self.x=800
                    self.y=200-(self.height/2)
                    self.rect.center=(self.x,self.y)
            
                #移动障碍物
                def obstacle_move(self):
                    self.rect.x -=5
            
                #绘制障碍物
                def draw_obstacle(self):
                    SCREEN.blit(self.image,(self.rect.x,self.rect.y))
            
                #获取分数
                def getScore(self):
                    self.score
                    tmp=self.score
                    if tmp==1:
                        self.score_audio.play()
                    self.score=0
                    return tmp
            
                #显示分数
                def showScore(self,score):
                    self.scoreDigits=[int(x) for x in list(str(score))]
                    totalWidth=0                #要显示的数字的总宽度
                    for digit in self.scoreDigits:
                        #获取积分图片的宽度
                        totalWidth+=self.numbers[digit].get_width()
                    #分数横向位置
                    xoffset=(SCREENWITDH - totalWidth)/2
                    for digit in self.scoreDigits:
                        #绘制分数
                        SCREEN.blit(self.numbers[digit],(xoffset,SCREENHEIGHT*0.1))
                        #随着数字增加改变位置
                        xoffset+=self.numbers[digit].get_width()
            
            #游戏结束的方法
            def game_over():
                bump_audio=pygame.mixer.Sound('audio/bump.wav')
                bump_audio.play()
                #获取窗口宽高
                screen_w=pygame.display.Info().current_w
                screen_h=pygame.display.Info().current_h
                #加载游戏结束的图片
                over_img=pygame.image.load('image/gameover.png').convert_alpha()
                #绘制游戏结束的图标在窗体中间
                SCREEN.blit(over_img,((screen_w-over_img.get_width())/2,(screen_h-over_img.get_height())/2))
                
            
            def mainGame():
                score=0 #记录分值
                over=False
                global SCREEN,FPSLOCK
                pygame.init() #初始化pygame
                FPSLOCK=pygame.time.Clock() #刷新屏幕的时间锁
                SCREEN=pygame.display.set_mode((SCREENWITDH,SCREENHEIGHT)) #设置屏幕的大小
                pygame.display.set_caption(self.name_entry.get()+'的'+self.role_combobox.get())  #随意定义的游戏标题
            
                bg1=MyMap(0,0) #地图1
                bg2=MyMap(800,0) #地图2
                #创建小恐龙
                dinasaur=Dinasaur()
            
                addobstacleTimer=0 #初始化障碍物时间为0
            
                obstacle_list=[] #障碍物对象的列表
            
                while True:
                    #判断是否单击了关闭窗口
                    for event in pygame.event.get():
                        if event.type==QUIT:
                            over=True
                            pygame.display.quit()
                            pygame.quit()  #退出程序(主畫面還在)
                            self.table.insert("", "end", 
                                              values = [0, self.name_entry.get(), self.type_combobox.get(),
                                                        self.difficulty_combobox.get(),self.sound_combobox.get(), score])
                            cols_name = ['名次','姓名', '關卡種類', '難度', "聲音", '得分']
                            for col in cols_name:
                                self.table.heading(col, text=col)
                        if event.type==KEYDOWN and event.key==K_SPACE:  #判断是否按下了空格键
                            if dinasaur.rect.y >=dinasaur.lowest_y:  #判断恐龙是不是在地面上
                                dinasaur.jump() #开启恐龙跳动状态
                                dinasaur.jump_audio.play() #播放音效
                    if over==False:
                        bg1.map_update() #绘制地图到更新的作用
                        bg1.map_rolling() #地图移动
                        bg2.map_update()
                        bg2.map_rolling()
                        dinasaur.move() #移动小恐龙
                        #绘制恐龙
                        dinasaur.draw_dinasour()
                        #计算障碍物间隔的时间
                        if addobstacleTimer>=1300:
                            r=random.randint(0,100)
                            if r>40:
                                #创建障碍物对象
                                obstacle=Obstacle()
                                #将障碍物推向添加到列表中
                                obstacle_list.append(obstacle)
                            #重置添加障碍物的时间
                            addobstacleTimer=0
                        #遍历障碍物
                        for i in range(len(obstacle_list)):
                            #移动障碍物
                            obstacle_list[i].obstacle_move()
                            #绘制障碍物
                            obstacle_list[i].draw_obstacle()
                            if pygame.sprite.collide_rect(dinasaur, obstacle_list[i]):
                                over=True
                                game_over()
                            else:
                                if(obstacle_list[i].rect.x+obstacle_list[i].rect.width)<dinasaur.rect.x:
                                    #加分
                                    score+=obstacle_list[i].getScore()
                            obstacle_list[i].showScore(score)
                        
                    addobstacleTimer +=20  #增加障碍物时间
                    pygame.display.update() #更新窗口
                    FPSLOCK.tick(FPS) #多久更新一次
        
        
        
            if __name__ == '__main__':
                mainGame()



if __name__ == "__main__":
    G = GUI()
    G.gui()