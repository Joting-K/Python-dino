import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import pickle
import pygame
from pygame.locals import *  # 加載pygame中所有常量
from pygame.locals import QUIT
from itertools import cycle  # 迭代工具
import random
import sys
import tkinter.font as Font
import os
import tkinter.font as tkFont
from PIL import ImageTk, Image

# 使用者介面 使用tk
play_times = 1  # 遊玩順序
path = "D:\Desktop\程式期末"


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
        # 主題選擇
        self.role_combobox, i = my_button(['過街老鼠', '噴泉漫步', '侏儸紀草原'], i)

        # 輸入名字
        self.name_entry = tk.Entry(self.gui, font=('微軟正黑體', 20, "bold"))
        self.name_entry.place(x=x + xgap, y=y + i * ygap, width=150)
        i += 1.7

        # 關卡種類
        self.type_combobox, i = my_button(['視覺關', '聽覺關', '挑戰關'], i)

        # 關卡聲音
        self.sound_combobox, i = my_button(['性感男聲', '平靜女聲'], i)
        i += 0.3

        # 三個按鈕
        # 1.遊戲說明
        self.explain_button = tk.Button(self.gui, bg='lightgray', command=self.do_explain, text='遊戲說明',
                                        font=('微軟正黑體', 20, "bold"))
        self.explain_button.place(x=100, y=550, width=150)

        # 2.Start
        self.ok_button = tk.Button(self.gui, bg='lightgray', command=self.do_ok, text='Start',
                                   font=('微軟正黑體', 20, "bold"))
        self.ok_button.place(x=300, y=550, width=150)
        i += 2

        # 3.參考資料
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

        # Treeview、列名、排列方式
        def treeview_sort_column(tv, col, reverse):
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

    # 按下start鍵的動作
    def do_ok(self):
        global path

        # 不同背景選擇、聲音選擇(透過路徑)
        theme = {'噴泉漫步': 'theme1', '侏儸紀草原': 'theme2', '過街老鼠': 'theme3'}
        sound = {'性感男聲': 'audio1', '平靜女聲': 'audio2'}
        mypath = os.path.join(path, theme[self.role_combobox.get()], sound[self.sound_combobox.get()])

        SCREENWITDH = 800  # 寬度
        SCREENHEIGHT = 300  # 高度
        FPS = 30  # 更新畫面的時間

        # 第一個class：地圖
        class MyMap:
            # 加載背景圖片
            def __init__(self, x, y):
                self.bg = pygame.image.load(os.path.join(mypath, "image/bg.png"))  # background
                self.x = x
                self.y = y

            # 地圖移動
            def map_rolling(self):
                if self.x < -790:  # 說明地圖已經移動完畢
                    self.x = 800  # 給地圖新座標
                else:
                    self.x -= 10  # 移動10像素

            # 更新地圖
            def map_update(self):
                SCREEN.blit(self.bg, (self.x, self.y))

        # 第二個class：小恐龍(遊戲角色)
        class Dinasaur:
            def __init__(self):
                # 初始化小恐龍矩形
                self.rect = pygame.Rect(0, 0, 0, 0)
                self.jumpState = False  # 跳躍的狀態
                self.squatState = False  # 蹲下的狀態
                self.jumpHeight = 100  # 跳躍高度
                self.squatHeight = -100  # 蹲下高度
                self.lowest_y = 140  # 地面座標
                self.jumpValue = 0  # 跳躍增加的高度
                self.squatValue = 0  # 蹲下降低的高度

                # 小恐龍的連續動作圖片
                self.dinasaurIndex = 0
                self.dinasaurIndexGen = cycle([0, 1, 2, 3, 4, 5])
                self.dinasaur_image = (pygame.image.load(os.path.join(mypath, "image/role1.png")).convert_alpha(),
                                       pygame.image.load(os.path.join(mypath, "image/role1.png")).convert_alpha(),
                                       pygame.image.load(os.path.join(mypath, "image/role2.png")).convert_alpha(),
                                       pygame.image.load(os.path.join(mypath, "image/role2.png")).convert_alpha(),
                                       pygame.image.load(os.path.join(mypath, "image/role3.png")).convert_alpha(),
                                       pygame.image.load(os.path.join(mypath, "image/role3.png")).convert_alpha())

                # 加載遊戲音效
                self.jump_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/jump.wav"))
                self.squat_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/蹲.wav"))
                self.jump2_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/跳.wav"))

                # 設定小恐龍初始座標
                self.rect.size = self.dinasaur_image[0].get_size()  # 設定小恐龍的矩形大小
                self.x = 50  # 設定小恐龍的x座標
                self.y = self.lowest_y  # 設定小恐龍的y座標
                self.rect.topleft = (self.x, self.y)  # 以左上角為準

            # 跳躍
            def jump(self):
                self.jumpState = True

            # 蹲下
            def squat(self):
                self.squatState = True

            # 小恐龍的移動
            def move(self):
                # 當處在可起跳狀態
                if self.jumpState:
                    if self.rect.y >= self.lowest_y:
                        self.jumpValue = - 5  # 以5個像素向上移動
                    if self.rect.y <= self.lowest_y - self.jumpHeight:
                        self.jumpValue = 5
                    self.rect.y += self.jumpValue  # 透過循環改變小恐龍的Y值
                    if self.rect.y == self.lowest_y:  # 當小恐龍回到地面
                        self.jumpState = False  # 關閉跳躍狀態

                # 當處在可蹲下狀態
                if self.squatState:
                    if self.rect.y <= self.lowest_y:
                        self.squatValue = 5  # 以5個像素向下移動
                    if self.rect.y >= self.lowest_y - self.squatHeight:
                        self.squatValue = -5
                    self.rect.y += self.squatValue  # 透過循環改變小恐龍的Y值
                    if self.rect.y == self.lowest_y:  # 當小恐龍回到地面
                        self.squatState = False  # 關閉蹲下狀態

            # 繪製小恐龍
            def draw_dinasour(self):
                # 小恐龍的連續動作圖片
                dinasaurindex = next(self.dinasaurIndexGen)
                # 實現繪製
                SCREEN.blit(self.dinasaur_image[dinasaurindex], (self.x, self.rect.y))

        # 第三個class：障礙物
        class Obstacle:
            score = 1  # 分數(每次加1分)

            def __init__(self):
                # 初始化障礙物矩形
                self.rect = pygame.Rect(0, 0, 0, 0)
                # 加載障礙物圖片
                self.stone = pygame.image.load(os.path.join(mypath, "image/obstacle1.png")).convert_alpha()  # 石頭(地上障礙物1)
                self.cacti = pygame.image.load(os.path.join(mypath, "image/obstacle2.png")).convert_alpha()  # 仙人掌(地上障礙物2)
                self.cloud = pygame.image.load(os.path.join(mypath, "image/obstacle3.png")).convert_alpha()  # 雲(天上障礙物)

                # 加載分數圖片
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

                # 加載加分的音效
                self.score_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/score.wav"))
                # 加載扣分的音效
                self.minus_audio=pygame.mixer.Sound(os.path.join(mypath, "audio/Duck Quack.mp3"))

                # 創建隨機的變數0，1，2
                r = random.randint(0, 2)

                # 0是石頭(地上障礙物1)
                if r == 0:
                    self.image = self.stone
                    # 繪製障礙物矩形、座標
                    self.rect.size = self.image.get_size()
                    self.width, self.height = self.rect.size
                    self.x = 800
                    self.y = 215
                    self.rect.center = (self.x, self.y)

                # 1是仙人掌(地上障礙物2)
                elif r == 1:
                    self.image = self.cacti
                    # 繪製障礙物矩形、座標
                    self.rect.size = self.image.get_size()
                    self.width, self.height = self.rect.size
                    self.x = 800
                    self.y = 215
                    self.rect.center = (self.x, self.y)

                # 2是雲(天上障礙物)
                else:
                    self.image = self.cloud
                    # 繪製障礙物矩形、座標
                    self.rect.size = self.image.get_size()
                    self.width, self.height = self.rect.size
                    self.x = 800
                    self.y = 150 - (self.height / 2)
                    self.rect.center = (self.x, self.y)

            # 移動障礙物
            def obstacle_move(self):
                self.rect.x -= 10  # 以10像素移動

            # 繪製障礙物
            def draw_obstacle(self):
                SCREEN.blit(self.image, (self.rect.x, self.rect.y))

            # 得分
            def getScore(self):
                self.score
                tmp = self.score
                if tmp == 1:
                    self.score_audio.play()
                self.score = 0
                return tmp

            # 顯示分數
            def showScore(self, score):
                # 分數
                self.scoreDigits = [int(x) for x in list(str(score))]
                # 要顯示數字的寬度
                totalWidth = 0
                for digit in self.scoreDigits:
                    totalWidth += self.numbers[digit].get_width()
                # 分數横向位置
                xoffset = (SCREENWITDH - totalWidth) / 2
                for digit in self.scoreDigits:
                    # 繪製分数
                    SCREEN.blit(self.numbers[digit], (xoffset, SCREENHEIGHT * 0.1))
                    # 隨著數字增加改變位置
                    xoffset += self.numbers[digit].get_width()

            # 通過障礙物狀態(挑戰關使用)
            # 通過障礙物時，標註此障礙物是"Watching" or "Hearing"
            pass_state = ""  # 初始值

            # 紀錄該障礙物的關卡狀態
            def setPassState(self, state):
                if self.pass_state == "":
                   self.pass_state = state

            # 取得該障礙物的關卡狀態
            def getPassState(self): # 取得"經過狀態下的關卡"
                return self.pass_state

        # 三大class以外的其他函數
        # 1.遊戲結束
        def game_over():
            # 加載遊戲結束音效並播放
            bump_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/bump.wav"))
            bump_audio.play()
            # 獲取窗口寬高
            screen_w = pygame.display.Info().current_w
            screen_h = pygame.display.Info().current_h
            # 加載gameover圖片
            over_img = pygame.image.load(os.path.join(mypath, "image/gameover.png")).convert_alpha()
            # 繪製gameover圖片在畫面中間
            SCREEN.blit(over_img, ((screen_w - over_img.get_width()) / 2, (screen_h - over_img.get_height()) / 2))

        # 2.關卡模式
        def what_game(subtitle_path):
            """聽覺關：subtitle_path == 'image/hearing.png'"""
            """視覺關：subtitle_path == 'image/watching.png'"""
            # 獲取窗口寬高
            screen_w = pygame.display.Info().current_w
            screen_h = pygame.display.Info().current_h
            # 加載關卡模式圖片
            this_img = pygame.image.load(os.path.join(mypath, subtitle_path)).convert_alpha()
            # 繪製關卡模式圖片在畫面中間
            SCREEN.blit(this_img, ((screen_w - this_img.get_width()) / 2, (screen_h - this_img.get_height()) / 2))
            # 讓圖片稍微停留
            for i in range(20):
                pygame.display.update()
                FPSLOCK.tick(FPS)

        # 3.主要遊戲
        def mainGame():
            sound_r = -1  # -1是預設沒有聲音狀態, 0是跳，1是蹲
            score = 0  # 分數
            over = False  # over==True代表遊戲結束
            global SCREEN, FPSLOCK
            pygame.init()  # 初始化pygame
            FPSLOCK = pygame.time.Clock()  # 刷新螢幕的時間鎖
            SCREEN = pygame.display.set_mode((SCREENWITDH,SCREENHEIGHT))  # 設置螢幕的大小
            pygame.display.set_caption("恐龍遊戲-眼睛耳朵不一樣")  # 遊戲標題

            bg1 = MyMap(0,0)  # 地圖1
            bg2 = MyMap(800,0)  # 地圖2

            dinasaur = Dinasaur()  # 創建小恐龍
            
            addobstacleTimer = 0  # 初始化障礙物出現時間為0
            obstacle_list = []  # 障礙物的列表

            #一.視覺關
            if self.type_combobox.get() == '視覺關':

                while True:
                    for event in pygame.event.get():
                        # 判斷是否點擊關閉
                        if event.type == QUIT:
                            over = True
                            pygame.display.quit()
                            pygame.quit()  # 退出程序(主畫面還在)

                            # 遊玩次數(進行後續排行)
                            global play_times
                            self.table.insert("", "end",
                                              values=[play_times, self.name_entry.get(), self.type_combobox.get(),
                                                      self.sound_combobox.get(), int(score)])
                            cols_name = ['遊玩順序', '姓名', '關卡種類', "聲音", '得分']
                            play_times += 1
                            for col in cols_name:
                                self.table.heading(col, text=col)

                        '''按鍵動作判斷'''
                        # 判斷是否按下了空白鍵
                        if event.type == KEYDOWN and event.key == K_SPACE:
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判斷小恐龍是否在地面
                                dinasaur.jump()  # 開啟小恐龍跳躍狀態
                                dinasaur.jump_audio.play()  # 播放跳躍音效


                        # 判斷是否按下了向下鍵
                        if event.type == KEYDOWN and event.key == K_DOWN:
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判斷小恐龍是否在地面
                                dinasaur.squat()  # 開啟小恐龍蹲下狀態

                    if over == False:
                        # 地圖更新和移動
                        bg1.map_update()
                        bg1.map_rolling()
                        bg2.map_update()
                        bg2.map_rolling()
                        # 小恐龍移動和繪製
                        dinasaur.move()
                        dinasaur.draw_dinasour()

                        # 計算創造障礙物的間隔時間
                        if addobstacleTimer >= 1300:

                            # 1.隨機產生障礙物
                            obstacle_crl = random.randint(0, 100)
                            if obstacle_crl > 50:
                                # 創造障礙物
                                obstacle = Obstacle()
                                # 將障礙物放進list裡
                                obstacle_list.append(obstacle)
                            # 重置創造障礙物的間隔時間
                            addobstacleTimer = 0

                            # 2.隨機撥放跳蹲指令音效
                            sound_crl = random.randint(0, 100)
                            if sound_crl > 70:
                                # 創造指令音效
                                sound_r = random.randint(0,1)
                                # 播放跳的指令音效
                                if sound_r == 0:
                                    dinasaur.jump2_audio.play()
                                # 播放蹲的指令音效
                                if sound_r == 1:
                                    dinasaur.squat_audio.play()

                        # 遍歷障礙物
                        for i in range(len(obstacle_list)):
                            # 移動障礙物
                            obstacle_list[i].obstacle_move()
                            # 繪製障礙物
                            obstacle_list[i].draw_obstacle()

                            # 如果小恐龍撞到障礙物，則遊戲結束
                            if pygame.sprite.collide_rect(dinasaur, obstacle_list[i]):
                                over=True
                                game_over()

                            # 小恐龍成功通過障礙物，加分!
                            else:
                                obswidth = obstacle_list[i].rect.x + obstacle_list[i].rect.width
                                if obswidth < dinasaur.rect.x:
                                    score += obstacle_list[i].getScore()
                            # 顯示分數
                            obstacle_list[i].showScore(score)

                    addobstacleTimer += 20  # 增加障礙物時間
                    pygame.display.update() # 更新窗口
                    FPSLOCK.tick(FPS)  # 多久更新一次

            #二.聽覺關
            elif self.type_combobox.get() == '聽覺關':

                # 聽覺關mainGame增加的
                success = False
                num_of_failure = 0
                max_num_of_failure = 40
                first_obs = True

                while True:
                    for event in pygame.event.get():
                        # 判斷是否點擊關閉
                        if event.type == QUIT:
                            over = True
                            pygame.display.quit()
                            pygame.quit()  # 退出程序(主畫面還在)

                            # 遊玩次數(進行後續排行)
                            play_times
                            self.table.insert("", "end",
                                              values=[play_times, self.name_entry.get(), self.type_combobox.get(),
                                                      self.sound_combobox.get(), int(score)])
                            cols_name = ['遊玩順序', '姓名', '關卡種類', "聲音", '得分']
                            play_times += 1
                            for col in cols_name:
                                self.table.heading(col, text=col)

                        '''按鍵動作判斷'''
                        # 判斷是否按下了空白鍵
                        if event.type == KEYDOWN and event.key == K_SPACE:
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判斷小恐龍是否在地面
                                dinasaur.jump()  # 開啟小恐龍跳躍狀態
                                dinasaur.jump_audio.play()  # 播放跳躍音效

                            # 如果播放的音效是的是跳
                            if sound_r == 0:
                                # 成功
                                success = True
                                # 加分
                                score += 1
                                # 撥放加分音效
                                obstacle = Obstacle()
                                obstacle.score_audio.play()

                                # 回歸預設
                                num_of_failure = 0
                                sound_r = -1
                                success = False

                            # 如果播放的音效是蹲
                            if sound_r == 1:
                                # 錯誤動作，遊戲結束
                                over = True
                                game_over()

                        # 判斷是否按下了向下鍵
                        if event.type == KEYDOWN and event.key == K_DOWN:
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判斷小恐龍是否在地面
                                dinasaur.squat()  # 開啟小恐龍蹲下狀態

                            # 如果播放的音效是的是蹲
                            if sound_r == 1:
                                # 成功
                                success = True
                                # 加分
                                score += 1
                                # 撥放加分音效
                                obstacle = Obstacle()
                                obstacle.score_audio.play()

                                # 回歸預設
                                num_of_failure = 0
                                sound_r = -1
                                success = False

                            # 如果播放的音效是跳
                            if sound_r == 0:
                                # 錯誤動作，遊戲結束
                                over = True
                                game_over()

                    if over == False:
                        # 地圖更新和移動
                        bg1.map_update()
                        bg1.map_rolling()
                        bg2.map_update()
                        bg2.map_rolling()
                        # 小恐龍移動和繪製
                        dinasaur.move()
                        dinasaur.draw_dinasour()

                        # 第一個障礙物(讓遊戲能早點開始)
                        if first_obs == True:
                            obstacle = Obstacle()
                            obstacle_list.append(obstacle)
                            first_obs = False

                        else:
                            # 計算創造障礙物的間隔時間
                            if addobstacleTimer >= 1300:

                                # 1.隨機產生障礙物
                                obstacle_crl = random.randint(0, 100)
                                if obstacle_crl > 50:
                                    # 創造障礙物
                                    obstacle = Obstacle()
                                    # 將障礙物放進list裡
                                    obstacle_list.append(obstacle)
                                # 重置創造障礙物的間隔時間
                                addobstacleTimer = 0

                                # 2.隨機撥放跳蹲指令音效
                                # 小恐龍在地面上時才撥放音效
                                if dinasaur.rect.y == dinasaur.lowest_y:
                                    sound_crl = random.randint(0, 100)
                                    if sound_crl > 1:
                                        # 創造指令音效
                                        sound_r = random.randint(0,1)
                                        # 播放跳的指令音效
                                        if sound_r == 0:
                                            dinasaur.jump2_audio.play()
                                        # 播放蹲的指令音效
                                        if sound_r == 1:
                                            dinasaur.squat_audio.play()

                        # 遍歷障礙物
                        for i in range(len(obstacle_list)):
                            # 移動障礙物
                            obstacle_list[i].obstacle_move()
                            # 繪製障礙物
                            obstacle_list[i].draw_obstacle()
                            # 顯示分數
                            obstacle_list[i].showScore(score)

                        # 如果有聽覺指令，但未做出相對應舉動時
                        if  not success and sound_r != -1:
                            num_of_failure += 1  # 失敗次數加1
                            # 若未在容錯次數內完成動作
                            if num_of_failure >= max_num_of_failure:
                                # 遊戲失敗
                                over = True
                                game_over()

                    addobstacleTimer += 20  # 增加障礙物時間
                    pygame.display.update() # 更新窗口
                    FPSLOCK.tick(FPS)  # 多久更新一次

            #三.挑戰關
            elif self.type_combobox.get() == '挑戰關':

                # 聽覺關mainGame增加的
                success = False
                num_of_failure = 0
                max_num_of_failure = 40
                first_obs = True

                # 挑戰關mainGame增加的
                start_watch = True  # 開始遊戲出現watch字樣
                game_state = "Watching"  # 關卡狀態(初始為視覺關)
                addLevelTimer = 0  # 關卡切換的時間間隔
                # 處理視覺錯誤的扣分
                watch_success = False
                watch_num_of_failure = 0
                watch_max_num_of_failure = 30
                watch_obstacle_list = []  # 視覺關障礙物的list

                while True:
                    for event in pygame.event.get():
                        # 判斷是否點擊關閉
                        if event.type == QUIT:
                            over = True
                            pygame.display.quit()
                            pygame.quit()  # 退出程序(主畫面還在)

                            # 遊玩次數(進行後續排行)
                            play_times
                            self.table.insert("", "end",
                                              values=[play_times, self.name_entry.get(), self.type_combobox.get(),
                                                      self.sound_combobox.get(), int(score)])
                            cols_name = ['遊玩順序', '姓名', '關卡種類', "聲音", '得分']
                            play_times += 1
                            for col in cols_name:
                                self.table.heading(col, text=col)

                        # 讓開頭就有watch字樣
                        if start_watch == True:
                            what_game('image/watching.png')
                            start_watch = False

                        '''按鍵動作判斷'''
                        # 判斷是否按下了空白鍵
                        if event.type == KEYDOWN and event.key == K_SPACE:
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判斷小恐龍是否在地面
                                dinasaur.jump()  # 開啟恐龍跳躍狀態
                                dinasaur.jump_audio.play()  # 播放跳躍音效

                            # 聽覺關時
                            if game_state == "Hearing":
                                # 如果播放的音效是的是跳
                                if sound_r == 0:
                                    # 成功
                                    success = True
                                    # 加分
                                    score += 1
                                    # 撥放加分音效
                                    obstacle = Obstacle()
                                    obstacle.score_audio.play()
                                    # 回歸預設
                                    num_of_failure = 0
                                    sound_r = -1
                                    success = False

                                # 如果播放的音效是蹲
                                if sound_r == 1:
                                    # 錯誤動作，遊戲結束
                                    over = True
                                    game_over()

                            # 視覺關時
                            if game_state == "Watching":
                                # 如果播放的音效是的是跳
                                if sound_r == 0:
                                    # 依照聽覺指令做出動作
                                    watch_success = True
                                    # 扣分!!(因為你不應該依照聽覺指令做動作)
                                    if score > 0:
                                        score -= 1
                                    # 撥放扣分音效
                                    obstacle = Obstacle()
                                    obstacle.minus_audio.play()
                                    # 回歸預設
                                    watch_num_of_failure = 0
                                    sound_r = -1
                                    watch_success = False

                        if event.type == KEYDOWN and event.key == K_DOWN:  # 判断是否按下了向下键
                            if dinasaur.rect.y == dinasaur.lowest_y:  # 判断恐龙是不是在地面上
                                dinasaur.squat()  # 開啟恐龍蹲下狀態

                            # 聽覺關時
                            if game_state == "Hearing":
                                # 如果播放的音效是的是蹲
                                if sound_r == 1:
                                    # 成功
                                    success = True
                                    # 加分
                                    score += 1
                                    # 撥放加分音效
                                    obstacle = Obstacle()
                                    obstacle.score_audio.play()
                                    # 回歸預設
                                    num_of_failure = 0
                                    sound_r = -1
                                    success = False

                                # 如果播放的音效是跳
                                if sound_r == 0:
                                    # 錯誤動作，遊戲結束
                                    over = True
                                    game_over()


                            # 視覺關時
                            if game_state == "Watching":
                                # 如果播放的音效是的是蹲
                                if sound_r == 1:
                                    # 依照聽覺指令做出動作
                                    watch_success = True
                                    # 扣分!!(因為你不應該依照聽覺指令做動作)
                                    if score > 0:
                                        score -= 1
                                    # 撥放扣分音效
                                    obstacle = Obstacle()
                                    obstacle.minus_audio.play()
                                    # 回歸預設
                                    watch_num_of_failure = 0
                                    sound_r = -1
                                    watch_success = False

                    if over == False:
                        # 地圖更新和移動
                        bg1.map_update()
                        bg1.map_rolling()
                        bg2.map_update()
                        bg2.map_rolling()
                        # 小恐龍移動和繪製
                        dinasaur.move()
                        dinasaur.draw_dinasour()

                        # 第一個障礙物(讓遊戲能早點開始)
                        if first_obs == True:
                            obstacle=Obstacle()
                            obstacle_list.append(obstacle)
                            first_obs = False
                            if game_state == 'Watching':
                                watch_obstacle_list.append(obstacle)
                            first_obs = False

                        else:
                            # 計算創造障礙物的間隔時間
                            if addobstacleTimer >= 1300:

                                # 1.隨機產生障礙物
                                obstacle_crl = random.randint(0, 100)
                                if obstacle_crl > 50:
                                    # 創造障礙物
                                    obstacle = Obstacle()
                                    # 將障礙物放進list裡
                                    obstacle_list.append(obstacle)
                                    if game_state == 'Watching':
                                        watch_obstacle_list.append(obstacle)
                                # 重置創造障礙物的間隔時間
                                addobstacleTimer = 0

                                # 2.隨機撥放跳蹲指令音效
                                sound_crl = random.randint(0, 100)
                                if sound_crl > 50:
                                    # 創造指令音效
                                    sound_r = random.randint(0,1)
                                    # 播放跳的指令音效
                                    if sound_r == 0:
                                        dinasaur.jump2_audio.play()
                                    # 播放蹲的指令音效
                                    if sound_r == 1:
                                        dinasaur.squat_audio.play()

                            # 關卡控制
                            if addLevelTimer >= 5000:
                                # 判斷恐龍是否在地面上
                                if dinasaur.rect.y == dinasaur.lowest_y:
                                    r=random.randint(0,100)  # 關卡控制變數

                                    # 視覺關
                                    if r > 50 and game_state != "Watching":
                                        game_state = "Watching"
                                        what_game('image/watching.png')
                                        addLevelTimer=0

                                    # 聽覺關
                                    if r < 50 and game_state != "Hearing":
                                        game_state = "Hearing"
                                        what_game('image/hearing.png')
                                        success = False
                                        addLevelTimer=0

                        # 遍歷障礙物
                        for i in range(len(obstacle_list)):
                            # 移動障礙物
                            obstacle_list[i].obstacle_move()
                            # 繪製障礙物
                            obstacle_list[i].draw_obstacle()
                            # 顯示分數
                            obstacle_list[i].showScore(score)

                        # 標註障礙物的過關狀態"Watching" or "Hearing"
                        # 在視覺關的障礙物裡面
                        for i in range(len(watch_obstacle_list)):

                            # 如果現在是視覺關
                            if game_state == "Watching":
                                # 撞到障礙物就直接gameover
                                if pygame.sprite.collide_rect(dinasaur, watch_obstacle_list[i]):
                                    over=True
                                    game_over()
                                # 如果通過，先把setPassState設定為視覺關通過
                                else:
                                    if (watch_obstacle_list[i].rect.x + watch_obstacle_list[i].rect.width) < dinasaur.rect.x:
                                        watch_obstacle_list[i].setPassState("Watching")

                            # 如果現在是聽覺關
                            if game_state == "Hearing":
                                # 撞到障礙物不會發生任何事
                                if pygame.sprite.collide_rect(dinasaur, watch_obstacle_list[i]):
                                    pass
                                # 如果通過障礙物，先把setPassState設定為聽覺關通過
                                if (watch_obstacle_list[i].rect.x + watch_obstacle_list[i].rect.width) < dinasaur.rect.x:
                                    watch_obstacle_list[i].setPassState("Hearing")


                        # 處理視覺關加分
                        # 如果setPassState為視覺關通過，才加分
                        for i in range(len(watch_obstacle_list)):
                            if watch_obstacle_list[i].getPassState() == "Watching":
                                score += watch_obstacle_list[i].getScore()

                        # 處理視覺關扣分
                        # 如果進入視覺遊戲，且未作出聽覺指令之動作
                        if game_state == "Watching" and not watch_success and sound_r != -1:
                            # 視覺的未做動作次數加1
                            watch_num_of_failure += 1
                            # 如果未在最大未做動作次數內做出動作，代表成功，回歸初始值
                            if watch_num_of_failure >= watch_max_num_of_failure:
                                watch_num_of_failure = 0
                                sound_r = -1

                        # 聽覺關
                        if game_state == "Hearing":
                            # 如果有聽覺指令，但未做出相對應舉動時
                            if  not success and sound_r != -1:
                                num_of_failure += 1  # 失敗次數加1
                                # 若未在容錯次數內完成動作
                                if num_of_failure >= max_num_of_failure:
                                    # 遊戲失敗
                                    over = True
                                    game_over()

                    addobstacleTimer += 20  # 增加障礙物時間
                    addLevelTimer += 20  # 增加關卡切換時間
                    pygame.display.update() # 更新窗口
                    FPSLOCK.tick(FPS)  # 多久更新一次

        if __name__ == '__main__':
            mainGame()

if __name__ == "__main__":
    G = GUI()
