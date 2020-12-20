import pygame
from pygame.locals import  *  # 載入pygame中所有常量
from itertools import cycle   # 迭代工具
import random
import os
SCREENWITDH=800   # 寬度
SCREENHEIGHT=260  # 高度
FPS=30  # 更新畫面的時間

mypath = "C:/Users/okahe/Desktop/dinosaur-master"

#定義地圖
class MyMap:
    #載入背景圖片
    def __init__(self,x,y):
        self.bg = pygame.image.load(os.path.join(mypath, "image/bg.png"))
        self.x = x
        self.y = y
    def map_rolling(self):
        if self.x <- 790: # 說明地圖已經移動完畢
            self.x = 800  # 給地圖新座標
        else:
            self.x -= 5  # 移動5個像素
    #更新地圖
    def map_update(self):
        SCREEN.blit(self.bg,(self.x,self.y))

#定義恐龍類
class Dinasaur:
    def __init__(self):
        # 初始化小恐龍矩形
        self.rect = pygame.Rect(0,0,0,0)
        self.jumpState = False  # 跳躍的狀態
        self.squatState = False  #蹲下的狀態
        self.jumpHeight = 140   # 跳躍高度
        self.squatHeight = -100   # 蹲下高度
        self.lowest_y = 140     # 最低座標
        self.jumpValue = 0      # 跳躍增變量
        self.squatValue = 0      # 蹲下增變量
        self.dinasaurIndex = 0
        self.dinasaurIndexGen = cycle([0,1,2])
        self.dinasaur_image=(pygame.image.load(os.path.join(mypath, "image/dinosaur1.png")).convert_alpha(),
                             pygame.image.load(os.path.join(mypath, "image/dinosaur2.png")).convert_alpha(),
                             pygame.image.load(os.path.join(mypath, "image/dinosaur3.png")).convert_alpha(),)
        self.jump_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/jump.wav"))  # 載入跳躍音效
        self.squat_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/smb_stomp.wav"))  # 載入跳躍音效
        self.hear_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/蹲3.wav")) # 載入蹲下指示音效
        self.jump2_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/跳3.wav")) # 載入跳躍指示音效
        self.rect.size = self.dinasaur_image[0].get_size()     # 設置小恐龍矩形大小
        self.x = 50 # 設置小恐龍的X座標
        self.y = self.lowest_y # 設置小恐龍的Y座標
        self.rect.topleft = (self.x,self.y) # 設置左上角為準
    # 跳躍
    def jump(self):
        self.jumpState = True
    # 蹲下
    def squat(self):
        self.squatState = True
    #小恐龍的移動
    def move(self):
        if self.jumpState: # 當處在可起跳狀態
            if self.rect.y >= self.lowest_y:
                self.jumpValue = - 5  # 以5個像素向上移動
            if self.rect.y <= self.lowest_y-self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue # 透過循環改變恐龍的Y值
            if self.rect.y == self.lowest_y: # 當恐龍回到地面
                self.jumpState = False        # 關閉跳躍狀態
        if self.squatState:      # 當處在可蹲下狀態
            if self.rect.y <= self.lowest_y:
                self.squatValue = 5  # 以5個像素向下移動
            if self.rect.y >= self.lowest_y - self.squatHeight:
                self.squatValue = -5
            self.rect.y += self.squatValue # 透過循環改變恐龍的Y值
            if self.rect.y == self.lowest_y:  # 小恐龍回到地面
                self.squatState = False        # 關閉蹲下狀態

    #繪製小恐龍
    def draw_dinasour(self):
        # 匹配恐龍動圖
        dinasaurindex = next(self.dinasaurIndexGen)
        # 實現繪製
        SCREEN.blit(self.dinasaur_image[dinasaurindex],(self.x,self.rect.y))

#定義障礙物類
class Obstacle:
    score = 1 # 分數
    def __init__(self):
        # 初始化障礙物的矩形
        self.rect = pygame.Rect(0,0,0,0)
        # 載入障礙物的圖片
        self.stone = pygame.image.load(os.path.join(mypath, "image/stone.png")).convert_alpha() #載入石頭
        self.cacti = pygame.image.load(os.path.join(mypath, "image/cacti.png")).convert_alpha() #載入仙人掌
        # 載入分數圖片
        self.numbers = (pygame.image.load(os.path.join(mypath, "image/0.png")).convert_alpha(), #convert_alpha()透明度
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
        # 載入加分的音效
        self.score_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/score.wav"))
        # 創建0，1之間的隨機數字, 0是石頭，1是仙人掌
        r = random.randint(0,1)
        if r == 0:
            self.image = self.stone
        else:
            self.image = self.cacti
        # 根據障礙物位圖的寬高设置矩形
        self.rect.size = self.image.get_size()
        # 獲取位圖的寬高
        self.width,self.height = self.rect.size
        # 障礙物繪製座標
        if r == 0: # 石頭
            self.x = 800
            self.y = 130
            self.rect.center = (self.x,self.y)
        elif r == 1: # 仙人掌
            self.x = 800
            self.y = 215
            self.rect.center = (self.x,self.y)

    #移動障礙物
    def obstacle_move(self):
        self.rect.x -= 5

    #繪製障礙物
    def draw_obstacle(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    # 獲取分數
    def getScore(self):
        self.score
        tmp = self.score
        if tmp == 1:
            self.score_audio.play()
        self.score = 0
        return tmp

    # 顯示分數
    def showScore(self,score):
        self.scoreDigits = [int(x) for x in list(str(score))]
        totalWidth = 0 # 要顯示的數字的總寬度
        for digit in self.scoreDigits:
            # 獲取積分圖片的寬度
            totalWidth += self.numbers[digit].get_width()
        # 分數横向位置
        xoffset = (SCREENWITDH - totalWidth) / 2
        for digit in self.scoreDigits:
            # 繪製分数
            SCREEN.blit(self.numbers[digit],(xoffset,SCREENHEIGHT * 0.1))
            # 隨著數字增加改變位置
            xoffset+=self.numbers[digit].get_width()
            
     # 顯示倒數秒數
    def showCountdown(self, ms):
        self.msDigits = [int(x) for x in list(str(ms))]
        totalWidth = 0 # 要顯示的倒數秒數的總寬度
        for digit in self.msDigits:
            # 獲取倒數秒數的寬度
            totalWidth += self.numbers[digit].get_width()            
        # 倒數秒數的橫向位置
        xoffset = ((SCREENWITDH - totalWidth)/2)+300
        for digit in self.msDigits:
            # 繪製秒數
            SCREEN.blit(self.numbers[digit],(xoffset,SCREENHEIGHT*0.1))
            #随着秒數增加改變位置
            xoffset += self.numbers[digit].get_width()
            
# 遊戲结束的方法
def game_over():
    bump_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/bump.wav"))
    bump_audio.play()
    # 獲取窗口寬高
    screen_w = pygame.display.Info().current_w
    screen_h = pygame.display.Info().current_h
    # 載入遊戲结束的圖片
    over_img = pygame.image.load(os.path.join(mypath, "image/gameover.png")).convert_alpha()
    # 繪製遊戲结束的圖標在視窗中間
    SCREEN.blit(over_img, ((screen_w-over_img.get_width()) / 2, (screen_h-over_img.get_height()) / 2))

# 聽覺關遊戲圖片載入
def Hear_game():    
    # 獲取窗口寬高
    screen_w=pygame.display.Info().current_w
    screen_h=pygame.display.Info().current_h
    # 載入聽覺關遊戲的圖片
    hear_img=pygame.image.load(os.path.join(mypath, "image\\hear.png")).convert_alpha()
    # 繪製聽覺關遊戲的圖標在視窗中間
    SCREEN.blit(hear_img,((screen_w-hear_img.get_width()) / 2,(screen_h-hear_img.get_height()) / 2))
    for i in range(20):
        pygame.display.update()
        FPSLOCK.tick(FPS) 

# 視覺關遊戲圖片載入
def Watch_game():    
    # 獲取窗口寬高
    screen_w = pygame.display.Info().current_w
    screen_h = pygame.display.Info().current_h
    # 載入視覺關遊戲的圖片
    watch_img = pygame.image.load(os.path.join(mypath, "image\\Watching(金色字體).png")).convert_alpha()
    # 繪製視覺關遊戲的圖標在視窗中間
    SCREEN.blit(watch_img,((screen_w-watch_img.get_width()) / 2,(screen_h-watch_img.get_height()) / 2))
    for i in range(20):
        pygame.display.update()
        FPSLOCK.tick(FPS) 

def gameStartPrepared(game_prepared):       
    print("game starting")        
    game_state = "Watching"
    Watch_game()
    game_prepared = True

# 主遊戲
def mainGame():
    sound_r = -1 # -1是預設沒有聲音狀態, 0是蹲，1是跳
    game_prepared = False
    score = 0 # 紀錄分數
    over = False
    global SCREEN,FPSLOCK
    pygame.init() # 初始化pygame
    FPSLOCK = pygame.time.Clock() # 更新螢幕的時間鎖
    SCREEN = pygame.display.set_mode((SCREENWITDH,SCREENHEIGHT)) # 設置視窗的大小
    pygame.display.set_caption("眼睛耳朵不一樣")  # 定義遊戲標題

    bg1 = MyMap(0,0) # 地圖1
    bg2 = MyMap(800,0) # 地圖2
    # 創建小恐龍
    dinasaur = Dinasaur()
    
    addobstacleTimer = 0 # 初始化障礙物時間为0
    addLevelTimer = 0 # 初始化關卡變數    
    obstacle_list = [] # 障礙物對象的列表
    
    success = False
    num_of_failure = 0
    max_num_of_failure = 90
    game_state = "Watching" # 預設挑戰關的初始狀態為"視覺關"
    watching_game_start_time = pygame.time.get_ticks()
    score_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/score.wav"))
    #score_minus_audio = pygame.mixer.Sound(os.path.join(mypath, "audio/Duck Quack.mp3"))
    while True:
        # 判斷是否點擊了關閉視窗
        for event in pygame.event.get():
            if event.type==QUIT:
                over=True
                exit() #退出程序                   
            if event.type == KEYDOWN and event.key == K_SPACE:  # 判斷是否按下了空白鍵
                if dinasaur.rect.y == dinasaur.lowest_y:  # 判斷恐龍是不是在地面上
                    dinasaur.jump() # 開啟恐龍的跳躍狀態
                    dinasaur.jump_audio.play() # 播放跳躍的音效
                    
                if game_state == "Hearing" and sound_r == 0: # 當處在聽覺關下，且撥放跳躍指示音效
                    print("jump")
                    success = True
                    num_of_failure = 0 # 成功跳躍時，將失敗次數歸零
                    score += 1 # 成功跳躍時，分數加1
                    score_audio.play()                    
                    print("you succeed the hear-jump game")
                    sound_r = -1 # 將變數回歸預設
                    
            if event.type == KEYDOWN and event.key == K_DOWN:  # 判斷是否按下了向下鍵
                if dinasaur.rect.y == dinasaur.lowest_y:  # 判斷恐龍是不是在地面上
                    dinasaur.squat() # 開啟恐龍的蹲下狀態
                    dinasaur.squat_audio.play() # 播放跳躍的音效
                  
                if game_state == "Hearing" and sound_r == 1: # 當處在聽覺關下，且撥放蹲下指示音效
                    print("squat")
                    success = True
                    num_of_failure = 0 # 成功蹲下時，將失敗次數歸零
                    score += 1 # 成功蹲下時，分數加1                    
                    score_audio.play()
                    print("you succeed the hear-squat game")
                    sound_r = -1 # 將變數回歸預設


        if over == False:        
            bg1.map_update() # 繪製地圖到更新的作用
            bg1.map_rolling() # 地圖移動
            bg2.map_update()
            bg2.map_rolling()
            dinasaur.move() # 移動小恐龍
            # 繪製恐龍
            dinasaur.draw_dinasour()
            # 計算障礙物間隔的時間
            if addobstacleTimer>=1300:                
                # 隨機產生障礙物
                obstacle_crl = random.randint(0,100)
                if obstacle_crl > 50:                                
                    # 創建障礙物對象
                    obstacle = Obstacle()
                    # 將障礙物推向添加到list內
                    obstacle_list.append(obstacle)
                # 重置添加障礙物的時間
                addobstacleTimer = 0
                
                # 關卡控制
                if addLevelTimer >= 2000 and dinasaur.rect.y == dinasaur.lowest_y:  # 判斷恐龍是不是在地上              
                    # 視覺關    
                    r = random.randint(0,100) # 以隨機產生的亂數來決定視覺關和聽覺關出現的機率
                    if r > 50 and game_state != "Watching":
                        game_state = "Watching"                        
                        watching_game_start_time = pygame.time.get_ticks()                        
                        print("start watch game")
                        Watch_game()
                        addLevelTimer = 0
                # 聽覺關
                    if r<50  and game_state != "Hearing":                
                        game_state = "Hearing"
                        print("start Hearing game")
                        Hear_game()                             
                        success = False
                        addLevelTimer=0
                    
            # 隨機撥放跳蹲指令音效        
                sound_crl = random.randint(0,100) # 以隨機產生的亂數來決定跳蹲指令音效出現的機率
                if sound_crl > 70:
                    sound_r = random.randint(0,1)
                    if sound_r == 0:
                        print("play jump sound")
                        dinasaur.jump2_audio.play() # 播放跳的指令音效
                        if game_state == "Watching":
                            sound_r == -1 # 回歸預設
                    if sound_r == 1:
                        print("play squat sound")
                        dinasaur.hear_audio.play() # 播放蹲的指令音效
                        if game_state == "Watching":
                            sound_r = -1 # 回歸預設
            
            # 歷遍障礙物
            for i in range(len(obstacle_list)):
                # 移動障礙物
                obstacle_list[i].obstacle_move()
                # 繪製障礙物
                obstacle_list[i].draw_obstacle()                
                Collision = pygame.sprite.collide_rect(dinasaur, obstacle_list[i])
                
                # 當聽覺關轉換到視覺關時: 在2秒內不會死
                if game_state == "Watching"and Collision == True: 
                    if pygame.time.get_ticks() - watching_game_start_time >= 2000:    # The time is in ms.
                        over=True
                        game_over()
                        
                #如果進入聽覺遊戲時且未依照音效指示，做出蹲下或跳躍時
                if game_state == "Hearing" and not success and sound_r != -1:  
                    num_of_failure += 1 #失敗次數加1
                    print(max_num_of_failure - num_of_failure)                    
                    if Collision == True: # 聽覺關時遇到障礙物不會死                                       
                        over = False
                    if num_of_failure >= max_num_of_failure: # 若未在容錯次數內完成動作
                        print("you fail the Hearing game") # 遊戲失敗
                        over = True
                        game_over()                        
                        #exit() #退出程序
                else:
                    if game_state == "Watching" and (obstacle_list[i].rect.x+obstacle_list[i].rect.width) < dinasaur.rect.x:
                        # 加分
                        score += obstacle_list[i].getScore()
                obstacle_list[i].showScore(score)
                if game_state == "Hearing":
                    Countdown = ( max_num_of_failure - num_of_failure) // FPS 
                    if Countdown >= 0:
                        obstacle_list[i].showCountdown(Countdown)

        addobstacleTimer += 20  #增加障礙物的時間
        addLevelTimer += 20 # 增加關卡的時間
        pygame.display.update() #更新視窗
        FPSLOCK.tick(FPS) # 多久更新一次
        

if __name__ == '__main__':
    mainGame()