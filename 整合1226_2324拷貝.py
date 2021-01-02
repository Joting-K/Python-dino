import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import pickle
import pygame
from pygame.locals import *  # 加载pygame中所有常量
from pygame.locals import QUIT
from itertools import cycle  # 迭代工具
import random
import sys
import tkinter.font as Font
import os
import tkinter.font as tkFont
from PIL import ImageTk, Image

# 使用者介面 使用tk
nn = 1  # 遊玩順序
path = "/Users/qinglin/Documents/Python/FINALLY/my_dino"


class GUI():
    def __init__(self):
        self.gui = tk.Tk()
        self.gui.geometry("1250x700")
        self.gui.title('小恐龍遊戲')
        self.gui.attributes('-alpha', 1)
        self.canvas = tk.Canvas(self.gui, bg='white', height=700, width=1250)
        self.canvas.place(x=0, y=0)
        imgpath = os.path.join(path, 'mainbackground.png')
        image = Image.open(imgpath)
        img = image.resize((1250, 700), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(1250 / 2, 350, image=photo)
        x = 228
        y = 272
        xgap = 100
        ygap = 35
        i = 0

        def my_button(choice, now_i):
            """用來製造可選的選項"""
            combobox = ttk.Combobox(self.gui, textvariable=tk.StringVar(), font=('微軟正黑體', 20, "bold"))
            combobox["value"] = choice
            combobox.current(0)
            combobox.place(x=x + xgap, y=y + now_i * ygap, width=150)
            now_i += 1.7
            return combobox, now_i

        self.role_combobox, i = my_button(['過街老鼠', '噴泉漫步', '侏儸紀草原'], i)  # 主題選擇

        self.name_entry = tk.Entry(self.gui, font=('微軟正黑體', 20, "bold"))  # 輸入名字
        self.name_entry.place(x=x + xgap, y=y + i * ygap, width=150)
        i += 1.7

        self.type_combobox, i = my_button(['視覺關', '聽覺關', '挑戰關'], i)  # 關卡種類

        self.sound_combobox, i = my_button(['性感男聲', '平靜女聲'], i)  # 關卡聲音
        i += 0.3

        self.explain_button = tk.Button(self.gui, bg='lightgray', command=self.do_explain, text='遊戲說明',
                                        font=('微軟正黑體', 20, "bold"))
        self.explain_button.place(x=100, y=550, width=150)

        self.ok_button = tk.Button(self.gui, bg='lightgray', command=self.do_ok, text='Start',
                                   font=('微軟正黑體', 20, "bold"))
        self.ok_button.place(x=300, y=550, width=150)
        i += 2
        self.ref_button = tk.Button(self.gui, bg='lightgray', command=self.do_ref, text='參考資料',
                                    font=('微軟正黑體', 20, "bold"))
        self.ref_button.place(x=500, y=550, width=150)
        i += 2

        cols_name = ['順序', '姓名', '種類', "聲音", '得分']
        self.table = ttk.Treeview(self.gui, columns=cols_name, show='headings', height=32)
        style_head = ttk.Style()
        style_head.theme_use("clam")
        style_head.configure("Treeview.Heading", font=('微軟正黑體', 15), background='#C6A300', foreground="Black")
        style_head.configure("Treeview", font=('微軟正黑體', 13), background='#E9C85D', foreground='red',
                             fieldbackground='LightGoldenrod')
        for col in cols_name:
            self.table.column(col, minwidth=0, width=94, stretch=False, anchor='center')

        for col in cols_name:
            self.table.heading(col, text=col)
        self.table.place(x=744, y=64)

        def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            print(tv.get_children(''))
            try:
                l.sort(key=lambda t: int(t[0]), reverse=reverse)

            except ValueError:
                l.sort(reverse=reverse)
                # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):  # 根據排序後索引移動
                self.table.move(k, '', index)
                print(k)
            self.table.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 重寫標題，使之成為再點倒序的標題

        for col in cols_name:  # 給所有標題加（迴圈上邊的“手工”）
            self.table.heading(col, text=col, command=lambda _col=col: treeview_sort_column(self.table, _col, False))

        self.gui.mainloop()

    # 按下遊戲說明的動作
    def do_explain(self):
        newWindow = tk.Toplevel()
        newWindow.geometry("980x600")
        newWindow.title('遊戲說明')
        newWindow.attributes('-alpha', 1)
        newWindow.canvas = tk.Canvas(newWindow, bg='white', height=600, width=980)
        newWindow.canvas.place(x=0, y=0)
        imgpath1 = os.path.join(path, 'ref.jpg')
        image1 = Image.open(imgpath1)
        img1 = image1.resize((980, 600), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(img1)
        newWindow.canvas.create_image(980 / 2, 300, image=photo1)
        newWindow.mainloop()

    # 按下參考資料的動作
    def do_ref(self):
        newWindow = tk.Toplevel()
        newWindow.geometry("980x600")
        newWindow.title('參考資料')
        newWindow.attributes('-alpha', 1)
        newWindow.canvas = tk.Canvas(newWindow, bg='white', height=600, width=980)
        newWindow.canvas.place(x=0, y=0)
        imgpath1 = os.path.join(path, 'ref.jpg')
        image1 = Image.open(imgpath1)
        img1 = image1.resize((980, 600), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(img1)
        newWindow.canvas.create_image(980 / 2, 300, image=photo1)
        newWindow.mainloop()

    # 按下start 鍵的動作
    def do_ok(self):
        global path

        # 不同背景選擇、聲音選擇(透過路徑)
        theme = {'噴泉漫步': 'theme1', '侏儸紀草原': 'theme2', '過街老鼠': 'theme3'}
        sound = {'性感男聲': 'audio1', '平靜女聲': 'audio2'}
        mypath = os.path.join(path, theme[self.role_combobox.get()], sound[self.sound_combobox.get()])

        SCREENWITDH = 800  # 宽度
        SCREENHEIGHT = 300  # 高度
        FPS = 30  # 更新画面的时间

        # 定义一个地图类
        class MyMap:
            # 加载背景图片
            def __init__(self, x, y):
                self.bg = pygame.image.load(os.path.join(mypath, "image/bg.png"))  # background
                self.x = x
                self.y = y

            def map_rolling(self):
                if self.x < -790:  # 说明地图已经移动完毕
                    self.x = 800  # 给地图新坐
                else:
                    self.x -= 10  # 移动5个像素

            # 更新地图
            def map_update(self):
                SCREEN.blit(self.bg, (self.x, self.y))

        # 恐龙类
        class Dinasaur:
            def __init__(self):
                # 初始化小恐龙矩形
                self.rect = pygame.Rect(0, 0, 0, 0)
                self.jumpState = False  # 跳跃的状态
                self.squatState = False  # 蹲下的状态
                self.jumpHeight = 100  # 跳跃高度
                self.squatHeight = -100  # 蹲下高度
                self.lowest_y = 140  # 最低坐标
                self.jumpValue = 0  # 跳跃增变量
                self.squatValue = 0  # 蹲下增变量
                self.dinasaurIndex = 0
                self.dinasaurIndexGen = cycle([0, 1, 2, 3, 4, 5])
                self.dinasaur_image = (pygame.image.load(os.path.join(mypath, "image/role1.png")).convert_alpha(),
                                       pygame.image.load(os.path.join(mypath, "image/role1.png")).convert_alpha(),
                                       pygame.image.load(os.path.join(mypath, "image/role2.png")).convert_alpha(),
                                       pygame.image.load(os.path.join(mypath, "image/role2.png")).convert_alpha(),
                                       pygame.image.load(os.path.join(mypath, "image/role3.png")).convert_alpha(),
                                       pygame.image.load(os.path.join(mypath, "image/role3.png")).convert_alpha())
                self.jump_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/jump.wav"))  # 加载音效
                self.hear_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/蹲.wav"))  # 加载音效
                self.jump2_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/跳.wav"))  # 加载音效
                self.rect.size = self.dinasaur_image[0].get_size()  # 设置小恐龙矩形大小
                self.x = 50  # 设置小恐龙的x坐标
                self.y = self.lowest_y  # 设置小恐龙的y坐标
                self.rect.topleft = (self.x, self.y)  # 设置左上角为准

            # 跳躍
            def jump(self):
                self.jumpState = True

            # 蹲下
            def squat(self):
                self.squatState = True

            # 小恐龍的移動
            def move(self):
                if self.jumpState:  # 當處在可起跳狀態
                    if self.rect.y >= self.lowest_y:
                        self.jumpValue = - 5  # 以5個像素向上移動
                    if self.rect.y <= self.lowest_y - self.jumpHeight:
                        self.jumpValue = 5
                    self.rect.y += self.jumpValue  # 透過循環改變恐龍的Y值
                    if self.rect.y == self.lowest_y:  # 當恐龍回到地面
                        self.jumpState = False  # 關閉跳躍狀態
                if self.squatState:  # 當處在可蹲下狀態
                    if self.rect.y <= self.lowest_y:
                        self.squatValue = 5  # 以5個像素向下移動
                    if self.rect.y >= self.lowest_y - self.squatHeight:
                        self.squatValue = -5
                    self.rect.y += self.squatValue  # 透過循環改變恐龍的Y值
                    if self.rect.y == self.lowest_y:  # 小恐龍回到地面
                        self.squatState = False  # 關閉蹲下狀態

            # 繪製小恐龍
            def draw_dinasour(self):
                # 匹配恐龍動圖
                dinasaurindex = next(self.dinasaurIndexGen)
                # 實現繪製
                SCREEN.blit(self.dinasaur_image[dinasaurindex], (self.x, self.rect.y))

        # 障碍物类
        class Obstacle:
            score = 1  # 分数

            def __init__(self):
                # 初始化障碍物的矩形
                self.rect = pygame.Rect(0, 0, 0, 0)
                # 加载障碍物的图片
                self.stone = pygame.image.load(os.path.join(mypath, "image/obstacle1.png")).convert_alpha()  # 加载石头
                self.cacti = pygame.image.load(os.path.join(mypath, "image/obstacle2.png")).convert_alpha()  # 加载仙人掌
                self.cloud = pygame.image.load(os.path.join(mypath, "image/obstacle3.png")).convert_alpha()  # 加载雲

                # 加载分数图片
                self.numbers = (
                    pygame.image.load(os.path.join(mypath, "image/0.png")).convert_alpha(),  # convert_alpha()透明度
                    pygame.image.load(os.path.join(mypath, "image/1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(mypath, "image/2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(mypath, "image/3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(mypath, "image/4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(mypath, "image/5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(mypath, "image/6.png")).convert_alpha(),
                    pygame.image.load(os.path.join(mypath, "image/7.png")).convert_alpha(),
                    pygame.image.load(os.path.join(mypath, "image/8.png")).convert_alpha(),
                    pygame.image.load(os.path.join(mypath, "image/9.png")).convert_alpha(),

                )
                # 加载加分的音效
                self.score_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/score.wav"))
                # 创建0，1之间的随机数,0是石头，1是仙人掌
                r = random.randint(0, 2)
                if r == 0:
                    self.image = self.stone
                    self.rect.size = self.image.get_size()
                    # 获取位图的宽高
                    self.width, self.height = self.rect.size
                    # 障碍物绘制坐标
                    self.x = 800
                    self.y = 215
                    self.rect.center = (self.x, self.y)
                elif r == 1:
                    self.image = self.cacti
                    self.rect.size = self.image.get_size()
                    # 获取位图的宽高
                    self.width, self.height = self.rect.size
                    # 障碍物绘制坐标
                    self.x = 800
                    self.y = 215
                    self.rect.center = (self.x, self.y)
                else:
                    self.image = self.cloud
                    # 根据障碍物位图的宽高设置矩形
                    self.rect.size = self.image.get_size()
                    # 获取位图的宽高
                    self.width, self.height = self.rect.size
                    # 障碍物绘制坐标
                    self.x = 800
                    self.y = 150 - (self.height / 2)
                    self.rect.center = (self.x, self.y)

            # 移动障碍物
            def obstacle_move(self):
                self.rect.x -= 10

            # 绘制障碍物
            def draw_obstacle(self):
                SCREEN.blit(self.image, (self.rect.x, self.rect.y))

            # 获取分数
            def getScore(self):
                self.score
                tmp = self.score
                if tmp == 1:
                    self.score_audio.play()
                self.score = 0
                return tmp

            # 顯示分數
            def showScore(self, score):
                self.scoreDigits = [int(x) for x in list(str(score))]
                totalWidth = 0  # 要顯示的數字的總寬度
                for digit in self.scoreDigits:
                    # 獲取積分圖片的寬度
                    totalWidth += self.numbers[digit].get_width()
                # 分數横向位置
                xoffset = (SCREENWITDH - totalWidth) / 2
                for digit in self.scoreDigits:
                    # 繪製分数
                    SCREEN.blit(self.numbers[digit], (xoffset, SCREENHEIGHT * 0.1))
                    # 隨著數字增加改變位置
                    xoffset += self.numbers[digit].get_width()

        # 游戏结束的方法
        def game_over():
            bump_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/bump.wav"))
            bump_audio.play()
            # 获取窗口宽高
            screen_w = pygame.display.Info().current_w
            screen_h = pygame.display.Info().current_h
            # 加载游戏结束的图片
            over_img = pygame.image.load(os.path.join(mypath, "image/gameover.png")).convert_alpha()
            # 绘制游戏结束的图标在窗体中间
            SCREEN.blit(over_img, ((screen_w - over_img.get_width()) / 2, (screen_h - over_img.get_height()) / 2))

        def what_game(subtitle_path):
            """聽覺關：subtitle_path == 'image/hearing.png'"""
            """視覺關：subtitle_path == 'image/watching.png'"""
            # 获取窗口宽高
            screen_w = pygame.display.Info().current_w
            screen_h = pygame.display.Info().current_h
            # 加载遊戲的图片
            this_img = pygame.image.load(os.path.join(mypath, subtitle_path)).convert_alpha()

            # 绘制游戏结束的图标在窗体中间
            SCREEN.blit(this_img, ((screen_w - this_img.get_width()) / 2, (screen_h - this_img.get_height()) / 2))
            for i in range(20):
                pygame.display.update()
                FPSLOCK.tick(FPS)


        def mainGame():
            sound_r = -1  # -1是預設沒有聲音狀態, 0是蹲，1是跳
            game_prepared = False
            score = 0  # 记录分值
            over = False
            global SCREEN, FPSLOCK
            pygame.init()  # 初始化pygame
            FPSLOCK = pygame.time.Clock()  # 刷新屏幕的时间锁
            SCREEN = pygame.display.set_mode((SCREENWITDH, SCREENHEIGHT))  # 设置屏幕的大小
            pygame.display.set_caption("恐龍遊戲-眼睛耳朵不一樣")  # 随意定义的游戏标题

            bg1 = MyMap(0, 0)  # 地图1
            bg2 = MyMap(800, 0)  # 地图2
            # 创建小恐龙
            dinasaur = Dinasaur()

            if self.type_combobox.get() == '視覺關':  # 視覺關

                addobstacleTimer = 0  # 初始化障碍物时间为0
                obstacle_list = []  # 障碍物对象的列表

                while True:
                    # 判断是否单击了关闭窗口
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            over = True
                            pygame.display.quit()
                            pygame.quit()  # 退出程序(主畫面還在)
                            global nn
                            self.table.insert("", "end",
                                              values=[nn, self.name_entry.get(), self.type_combobox.get(),
                                                      self.sound_combobox.get(), int(score)])
                            cols_name = ['遊玩順序', '姓名', '關卡種類', "聲音", '得分']
                            nn += 1
                            for col in cols_name:
                                self.table.heading(col, text=col)

                        if event.type == KEYDOWN and event.key == K_SPACE:  # 判断是否按下了空格键
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判断恐龙是不是在地面上
                                dinasaur.jump()  # 开启恐龙跳动状态
                                dinasaur.jump_audio.play()  # 播放音效

                        if event.type == KEYDOWN and event.key == K_DOWN:  # 判断是否按下了向下键
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判断恐龙是不是在地面上
                                dinasaur.squat()  # 開啟恐龍蹲下狀態

                    if over == False:
                        bg1.map_update()  # 绘制地图到更新的作用
                        bg1.map_rolling()  # 地图移动
                        bg2.map_update()
                        bg2.map_rolling()
                        dinasaur.move()  # 移动小恐龙
                        # 绘制恐龙
                        dinasaur.draw_dinasour()
                        # 计算障碍物间隔的时间
                        if addobstacleTimer >= 1300:

                            # 隨機產生障礙物
                            obstacle_crl = random.randint(0, 100)
                            if obstacle_crl > 50:
                                # 创建障碍物对象
                                obstacle = Obstacle()
                                # 将障碍物推向添加到列表中
                                obstacle_list.append(obstacle)
                            # 重置添加障碍物的时间
                            addobstacleTimer = 0

                            # 隨機撥放跳蹲指令音效
                            sound_crl = random.randint(0, 100)
                            if sound_crl > 70:
                                sound_r = random.randint(0, 1)
                                if sound_r == 0:
                                    print("play jump sound")
                                    dinasaur.jump2_audio.play()  # 播放跳的指令音效

                                if sound_r == 1:
                                    print("play squat sound")
                                    dinasaur.hear_audio.play()  # 播放蹲的指令音效

                        # 遍历障碍物
                        for i in range(len(obstacle_list)):
                            # 移动障碍物
                            obstacle_list[i].obstacle_move()
                            # 绘制障碍物
                            obstacle_list[i].draw_obstacle()
                            # 視覺關
                            if pygame.sprite.collide_rect(dinasaur, obstacle_list[i]):
                                print("you fail the game")
                                over = True
                                game_over()

                            else:
                                if (obstacle_list[i].rect.x + obstacle_list[i].rect.width) < dinasaur.rect.x:
                                    # 加分
                                    score += obstacle_list[i].getScore()
                            obstacle_list[i].showScore(score)

                    addobstacleTimer += 20  # 增加障碍物时间
                    pygame.display.update()  # 更新窗口
                    FPSLOCK.tick(FPS)  # 多久更新一次

            elif self.type_combobox.get() == '聽覺關':
                addobstacleTimer = 0  # 初始化障碍物时间为0
                obstacle_list = []  # 障碍物对象的列表

                success = False
                num_of_failure = 0
                max_num_of_failure = 40
                first_obs = True

                while True:
                    # 判断是否单击了关闭窗口
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            over = True
                            pygame.display.quit()
                            pygame.quit()  # 退出程序(主畫面還在)
                            global nn
                            self.table.insert("", "end",
                                              values=[nn, self.name_entry.get(), self.type_combobox.get(),
                                                      self.sound_combobox.get(), int(score)])
                            cols_name = ['順序', '姓名', '種類', "聲音", '得分']
                            nn += 1
                            for col in cols_name:
                                self.table.heading(col, text=col)

                        if event.type == KEYDOWN and event.key == K_SPACE:  # 判断是否按下了空格键
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判断恐龙是不是在地面上
                                dinasaur.jump()  # 开启恐龙跳动状态
                                dinasaur.jump_audio.play()  # 播放音效

                            if sound_r == 0:
                                print("jump")
                                success = True
                                num_of_failure = 0
                                score += 1
                                print("you succeed the hear-jump game")
                                obstacle = obstacle()
                                obstacle.score_audio.play()
                                sound_r = -1
                                success = False

                            if sound_r == 1:
                                over = True
                                game_over()

                        if event.type == KEYDOWN and event.key == K_DOWN:  # 判断是否按下了向下键
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判断恐龙是不是在地面上
                                dinasaur.squat()  # 開啟恐龍蹲下狀態

                            if sound_r == 1:
                                print("squat")
                                success = True
                                num_of_failure = 0
                                score += 1
                                print("you succeed the hear-squat game")
                                obstacle = Obstacle()
                                obstacle.score_audio.play()
                                sound_r = -1
                                success = False

                            if sound_r == 0:
                                over = True
                                game_over()

                    if over == False:
                        bg1.map_update()  # 绘制地图到更新的作用
                        bg1.map_rolling()  # 地图移动
                        bg2.map_update()
                        bg2.map_rolling()
                        dinasaur.move()  # 移动小恐龙
                        # 绘制恐龙
                        dinasaur.draw_dinasour()

                        # 第一個障礙物
                        if first_obs == True:
                            # 创建障碍物对象
                            obstacle = Obstacle()
                            # 将障碍物推向添加到列表中
                            obstacle_list.append(obstacle)
                            first_obs = False
                        else:
                            # 计算障碍物间隔的时间
                            if addobstacleTimer >= 1300:
                                print(first_obs)
                                # 隨機產生障礙物
                                obstacle_crl = random.randint(0, 100)
                                if obstacle_crl > 50:
                                    # 创建障碍物对象
                                    obstacle = Obstacle()
                                    # 将障碍物推向添加到列表中
                                    obstacle_list.append(obstacle)
                                # 重置添加障碍物的时间
                                addobstacleTimer = 0

                                if dinasaur.rect.y == dinasaur.lowest_y:
                                    # 隨機撥放跳蹲指令音效
                                    sound_crl = random.randint(0, 100)
                                    if sound_crl > 1:
                                        sound_r = random.randint(0, 1)
                                        if sound_r == 0:
                                            print("play jump sound")
                                            dinasaur.jump2_audio.play()  # 播放跳的指令音效
                                        if sound_r == 1:
                                            print("play squat sound")
                                            dinasaur.hear_audio.play()  # 播放蹲的指令音效

                        # 遍历障碍物
                        for i in range(len(obstacle_list)):
                            # 移动障碍物
                            obstacle_list[i].obstacle_move()
                            # 绘制障碍物
                            obstacle_list[i].draw_obstacle()
                            obstacle_list[i].showScore(score)

                        # 聽覺關
                        if not success and sound_r != -1:  # 如果進入聽覺遊戲時且未作出蹲下時
                            num_of_failure += 1  # 失敗次數加1
                            print(max_num_of_failure - num_of_failure)
                            if num_of_failure >= max_num_of_failure:  # 若未在容錯次數內完成動作
                                print("you fail the extra game")  # 遊戲失敗
                                over = True
                                game_over()


                    addobstacleTimer += 30  # 增加障碍物时间
                    pygame.display.update()  # 更新窗口
                    FPSLOCK.tick(FPS)  # 多久更新一次

            elif self.type_combobox.get() == '挑戰關':
                addobstacleTimer = 0  # 初始化障碍物时间为0
                addLevelTimer = 0  # 初始化關卡變數

                obstacle_list = []  # 障碍物对象的列表

                watch_obstacle_list = []

                success = False
                num_of_failure = 0
                max_num_of_failure = 50
                game_state = "Watching"
                watching_game_start_time = pygame.time.get_ticks()
                first_obs = True
                start_watch = True
                # immune = False
                # immune_time = 0
                watch_success = False
                watch_num_of_failure = 0
                watch_max_num_of_failure = 30


                while True:
                    # 判断是否单击了关闭窗口
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            over = True
                            pygame.display.quit()
                            pygame.quit()  # 退出程序(主畫面還在)
                            global nn
                            self.table.insert("", "end",
                                              values=[nn, self.name_entry.get(), self.type_combobox.get(),
                                                      self.sound_combobox.get(), int(score)])
                            cols_name = ['遊玩順序', '姓名', '關卡種類', "聲音", '得分']
                            nn += 1
                            for col in cols_name:
                                self.table.heading(col, text=col)

                        #  讓開頭就有watch字樣
                        if start_watch == True:
                            what_game('image/watching.png')
                            start_watch = False

                        if event.type == KEYDOWN and event.key == K_SPACE:  # 判断是否按下了空格键
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判断恐龙是不是在地面上
                                dinasaur.jump()  # 开启恐龙跳动状态
                                dinasaur.jump_audio.play()  # 播放音效

                            if game_state == "Hearing" and sound_r == 0:
                                print("jump")
                                success = True
                                num_of_failure = 0
                                score += 1
                                print("you succeed the hear-jump game")
                                obstacle = Obstacle()
                                obstacle.score_audio.play()
                                sound_r = -1
                                success = False
                            if game_state == "Hearing" and sound_r == 1:
                                over = True
                                game_over()

                            if game_state == "Watching" and sound_r == 0:
                                print("jump")
                                watch_success = True
                                watch_num_of_failure = 0
                                if score > 0:
                                    score -= 1
                                obstacle = Obstacle()
                                obstacle.minus_audio.play()
                                sound_r = -1
                                watch_success = False

                        if event.type == KEYDOWN and event.key == K_DOWN:  # 判断是否按下了向下键
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判断恐龙是不是在地面上
                                dinasaur.squat()  # 開啟恐龍蹲下狀態

                            if game_state == "Hearing" and sound_r == 1:
                                print("squat")
                                success = True
                                num_of_failure = 0
                                score += 1
                                print("you succeed the hear-squat game")
                                obstacle = Obstacle()
                                obstacle.score_audio.play()
                                sound_r = -1
                                success = False
                            if game_state == "Hearing" and sound_r == 0:
                                over = True
                                game_over()

                            if game_state == "Watching" and sound_r == 1:
                                print("squat")
                                watch_success = True
                                watch_num_of_failure = 0
                                if score > 0:
                                    score -= 1
                                obstacle = Obstacle()
                                obstacle.minus_audio.play()
                                sound_r = -1
                                watch_success = False

                    if over == False:
                        bg1.map_update()  # 绘制地图到更新的作用
                        bg1.map_rolling()  # 地图移动
                        bg2.map_update()
                        bg2.map_rolling()
                        dinasaur.move()  # 移动小恐龙
                        # 绘制恐龙
                        dinasaur.draw_dinasour()

                        # 第一個障礙物
                        if first_obs == True:
                            # 创建障碍物对象
                            obstacle = Obstacle()
                            # 将障碍物推向添加到列表中
                            obstacle_list.append(obstacle)
                            if game_state == 'Watching':
                                watch_obstacle_list.append(obstacle)
                            first_obs = False
                        else:
                            # 计算障碍物间隔的时间
                            if addobstacleTimer >= 1300:
                                # 隨機產生障礙物
                                obstacle_crl = random.randint(0, 100)
                                if obstacle_crl > 50:
                                    # 创建障碍物对象
                                    obstacle = Obstacle()
                                    # 将障碍物推向添加到列表中
                                    obstacle_list.append(obstacle)
                                    if game_state == 'Watching':
                                        watch_obstacle_list.append(obstacle)

                                # 重置添加障碍物的时间
                                addobstacleTimer = 0

                                # if dinasaur.rect.y == dinasaur.lowest_y:
                                # 隨機撥放跳蹲指令音效
                                sound_crl = random.randint(0, 100)
                                if sound_crl > 50:
                                    sound_r = random.randint(0, 1)
                                    if sound_r == 0:
                                        print("play jump sound")
                                        dinasaur.jump2_audio.play()  # 播放跳的指令音效
                                        # if game_state == "Watching":
                                        # sound_r = -1 # 回歸預設
                                    if sound_r == 1:
                                        print("play squat sound")
                                        dinasaur.hear_audio.play()  # 播放蹲的指令音效
                                        # if game_state == "Watching":
                                        # sound_r = -1 # 回歸預設

                            # 關卡控制
                            if addLevelTimer >= 5000 and dinasaur.rect.y == dinasaur.lowest_y:  # 判断恐龙是不是在地面上
                                # print('a', addLevelTimer)
                                # 視覺關
                                r = random.randint(0, 100)
                                # print(r)
                                if r > 50 and game_state != "Watching":
                                    # immune = True
                                    # immune_time = 100
                                    game_state = "Watching"
                                    watching_game_start_time = pygame.time.get_ticks()
                                    print("start watch game")
                                    what_game('image/watching.png')
                                    addLevelTimer = 0

                                # 聽覺關
                                if r < 50 and game_state != "Hearing":
                                    # immune = True
                                    # immune_time = 5
                                    game_state = "Hearing"
                                    print("start Hearing game")
                                    what_game('image/hearing.png')
                                    success = False
                                    addLevelTimer = 0

                        # 遍历障碍物
                        for i in range(len(obstacle_list)):
                            # 移动障碍物
                            obstacle_list[i].obstacle_move()
                            # 绘制障碍物
                            obstacle_list[i].draw_obstacle()

                        # 標註障礙物的過關狀態"Watching" or "Hearing"
                        for i in range(len(watch_obstacle_list)):
                            if game_state == "Watching":
                                if pygame.sprite.collide_rect(dinasaur, watch_obstacle_list[i]):
                                    print("you fail the game")
                                    over = True
                                    game_over()
                                else:
                                    if (watch_obstacle_list[i].rect.x + watch_obstacle_list[
                                        i].rect.width) < dinasaur.rect.x:
                                        watch_obstacle_list[i].setPassState("Watching")

                            if game_state == "Hearing":
                                if (score_obstacle_list[i].rect.x + score_obstacle_list[
                                    i].rect.width) < dinasaur.rect.x:
                                    score_obstacle_list[i].setPassState("Hearing")

                        # 處理視覺關加分
                        for i in range(len(watch_obstacle_list)):
                            if watch_obstacle_list[i].getPassState() == "Watching":
                                score += watch_obstacle_list[i].getScore()

                        # 視覺關扣分
                        if game_state == "Watching" and not watch_success and sound_r != -1:  # 如果進入視覺遊戲時且未作出蹲下時
                            watch_num_of_failure += 1  # 失敗次數加1
                            print(watch_max_num_of_failure - watch_num_of_failure)

                            if watch_num_of_failure >= watch_max_num_of_failure:  # 若未在容錯次數內完成動作
                                watch_num_of_failure = 0
                                sound_r = -1

                        # 聽覺關
                        if game_state == "Hearing" and not success and sound_r != -1:  # 如果進入聽覺遊戲時且未作出蹲下時
                            num_of_failure += 1  # 失敗次數加1
                            print(max_num_of_failure - num_of_failure)

                            if num_of_failure >= max_num_of_failure:  # 若未在容錯次數內完成動作
                                print("you fail the extra game")  # 遊戲失敗
                                over = True
                                game_over()
                                # exit() #退出程序

                        obstacle_list[i].showScore(score)

                    addobstacleTimer += 20  # 增加障碍物时间
                    addLevelTimer += 20  # 增加關卡的時間
                    pygame.display.update()  # 更新窗口
                    FPSLOCK.tick(FPS)  # 多久更新一次

            if __name__ == '__main__':
                mainGame()


if __name__ == "__main__":
    G = GUI()
