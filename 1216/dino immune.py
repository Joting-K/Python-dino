import pygame
from pygame.locals import  *  #加载pygame中所有常量
from itertools import cycle   #迭代工具
import random
import os
SCREENWITDH=800   #宽度
SCREENHEIGHT=260  #高度
FPS=30  #更新画面的时间

mypath = "D:\Desktop\程式期末"

#定义一个地图类
class MyMap:
    #加载背景图片
    def __init__(self,x,y):
        self.bg=pygame.image.load(os.path.join(mypath, "image/bg.png"))
        self.x=x
        self.y=y
    def map_rolling(self):
        if self.x<-790: #说明地图已经移动完毕
            self.x=800  #给地图新坐标
        else:
            self.x -=10  # 移动5个像素
    #更新地图
    def map_update(self):
        SCREEN.blit(self.bg,(self.x,self.y))

#恐龙类
class Dinasaur:
    def __init__(self):
        #初始化小恐龙矩形
        self.rect=pygame.Rect(0,0,0,0)
        self.jumpState=False  #跳跃的状态
        self.squatState=False  #蹲下的状态
        self.jumpHeight=100   #跳跃高度
        self.squatHeight=-100   #蹲下高度
        self.lowest_y=140     #最低坐标
        self.jumpValue= 0      #跳跃增变量
        self.squatValue= 0      #蹲下增变量
        self.dinasaurIndex=0
        self.dinasaurIndexGen=cycle([0,1,2])
        self.dinasaur_image=(pygame.image.load(os.path.join(mypath, "image/dinosaur1.png")).convert_alpha(),
                             pygame.image.load(os.path.join(mypath, "image/dinosaur2.png")).convert_alpha(),
                             pygame.image.load(os.path.join(mypath, "image/dinosaur3.png")).convert_alpha(),)
        self.jump_audio=pygame.mixer.Sound(os.path.join(mypath, "audio/jump.wav"))  # 加载音效
        self.hear_audio=pygame.mixer.Sound(os.path.join(mypath, "audio/蹲3.wav")) #加载音效
        self.jump2_audio=pygame.mixer.Sound(os.path.join(mypath, "audio/跳3.wav")) #加载音效
        self.rect.size=self.dinasaur_image[0].get_size()     #设置小恐龙矩形大小
        self.x=50                                            #设置小恐龙的x坐标
        self.y=self.lowest_y                                 #设置小恐龙的y坐标
        self.rect.topleft=(self.x,self.y)                    #设置左上角为准
    #跳跃
    def jump(self):
        self.jumpState=True
    #蹲下
    def squat(self):
        self.squatState=True
    #小恐龙的移动
    def move(self):
        if self.jumpState:      #可以起跳
            if self.rect.y >= self.lowest_y:
                self.jumpValue = - 5  #以5个像素向上移动
            if self.rect.y <= self.lowest_y-self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue #通过循环改变恐龙的Y值
            if self.rect.y == self.lowest_y:#恐龙回到地面
                self.jumpState = False        #关闭跳跃状态
        
        if self.squatState:      #可以蹲下
            if self.rect.y <= self.lowest_y:
                self.squatValue = 5  #以5个像素向下移动
            if self.rect.y >= self.lowest_y - self.squatHeight:
                self.squatValue = -5
            self.rect.y += self.squatValue # 透過循環改變恐龍的Y值
            if self.rect.y == self.lowest_y: # 小恐龍回到地面
                self.squatState = False        # 關閉蹲下狀態

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
        # 初始化障碍物的矩形
        self.rect=pygame.Rect(0,0,0,0)
        # 加载障碍物的图片
        self.stone=pygame.image.load(os.path.join(mypath, "image/stone.png")).convert_alpha() #加载石头
        self.cacti=pygame.image.load(os.path.join(mypath, "image/cacti.png")).convert_alpha() #加载仙人掌
        # 加载分数图片
        self.numbers=(pygame.image.load(os.path.join(mypath, "image/0.png")).convert_alpha(), #convert_alpha()透明度
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
        #加载加分的音效
        self.score_audio=pygame.mixer.Sound(os.path.join(mypath, "audio/score.wav"))
        #创建0，1之间的随机数,0是石头，1是仙人掌
        r=random.randint(0,1)
        if r == 0:
            self.image=self.stone
        else:
            self.image=self.cacti
        #根据障碍物位图的宽高设置矩形
        self.rect.size=self.image.get_size()
        #获取位图的宽高
        self.width,self.height=self.rect.size
        #障碍物绘制坐标
        if r == 0: #石頭
            self.x=800
            self.y=130
            self.rect.center=(self.x,self.y)
        elif r == 1: #仙人掌
            self.x=800
            self.y=215
            self.rect.center=(self.x,self.y)

    #移动障碍物
    def obstacle_move(self):
        self.rect.x -= 10

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
            
     # 顯示倒數秒數
    def showCountdown(self, ms):
        self.msDigits=[int(x) for x in list(str(ms))]
        totalWidth=0                #要显示的数字的总宽度
        for digit in self.msDigits:
            #获取积分图片的宽度
            totalWidth+=self.numbers[digit].get_width()
            
        #分数横向位置
        xoffset=((SCREENWITDH - totalWidth)/2)+300
        for digit in self.msDigits:
            #绘制分数
            SCREEN.blit(self.numbers[digit],(xoffset,SCREENHEIGHT*0.1))
            #随着数字增加改变位置
            xoffset+=self.numbers[digit].get_width()
            
#游戏结束的方法
def game_over():
    bump_audio=pygame.mixer.Sound(os.path.join(mypath, "audio/bump.wav"))
    bump_audio.play()
    #获取窗口宽高
    screen_w=pygame.display.Info().current_w
    screen_h=pygame.display.Info().current_h
    #加载游戏结束的图片
    over_img=pygame.image.load(os.path.join(mypath, "image/gameover.png")).convert_alpha()
    #绘制游戏结束的图标在窗体中间
    SCREEN.blit(over_img,((screen_w-over_img.get_width())/2,(screen_h-over_img.get_height())/2))

def Hear_game():    
    #获取窗口宽高
    screen_w=pygame.display.Info().current_w
    screen_h=pygame.display.Info().current_h
    #加载聽力遊戲的图片
    hear_img=pygame.image.load(os.path.join(mypath, "image\\hear.png")).convert_alpha()
    #绘制游戏结束的图标在窗体中间
    SCREEN.blit(hear_img,((screen_w-hear_img.get_width())/2,(screen_h-hear_img.get_height())/2))
    for i in range(20):
        pygame.display.update()
        FPSLOCK.tick(FPS) 

def Watch_game():    
    #获取窗口宽高
    screen_w=pygame.display.Info().current_w
    screen_h=pygame.display.Info().current_h
    #加载視覺遊戲的图片
    watch_img=pygame.image.load(os.path.join(mypath, "image\\obstacle-peo2.png")).convert_alpha()
    #绘制游戏结束的图标在窗体中间
    SCREEN.blit(watch_img,((screen_w-watch_img.get_width())/2,(screen_h-watch_img.get_height())/2))
    for i in range(20):
        pygame.display.update()
        FPSLOCK.tick(FPS) 
    

def game_over2():
    pass_audio=pygame.mixer.Sound(os.path.join(mypath, "audio/Duck Quack.mp3"))
    pass_audio.play() # 播放蹲下音效  
    #获取窗口宽高
    screen_w=pygame.display.Info().current_w
    screen_h=pygame.display.Info().current_h
    #加载游戏结束的图片
    over_img=pygame.image.load(os.path.join(mypath, "image/gameover.png")).convert_alpha()
    #绘制游戏结束的图标在窗体中间
    SCREEN.blit(over_img,((screen_w-over_img.get_width())/2,(screen_h-over_img.get_height())/2))    
def gameStartPrepared(game_prepared):       
    print("game starting")        
    game_state = "Watching"
    Watch_game()
    game_prepared = True

def mainGame():
    sound_r = -1 # -1是預設沒有聲音狀態, 0是蹲，1是跳
    game_prepared = False
    score=0 #记录分值
    over=False
    global SCREEN,FPSLOCK
    pygame.init() #初始化pygame
    FPSLOCK=pygame.time.Clock() #刷新屏幕的时间锁
    SCREEN=pygame.display.set_mode((SCREENWITDH,SCREENHEIGHT)) #设置屏幕的大小
    pygame.display.set_caption("恐龍遊戲-眼睛耳朵不一樣")  #随意定义的游戏标题

    bg1=MyMap(0,0) #地图1
    bg2=MyMap(800,0) #地图2
    #创建小恐龙
    dinasaur=Dinasaur()

    addobstacleTimer=0 #初始化障碍物时间为0
    addLevelTimer=0 #初始化關卡變數
    
    obstacle_list=[] #障碍物对象的列表
    
    success = False
    num_of_failure = 0
    max_num_of_failure = 150
    game_state = "Watching"
    
    immune = False
    immune_time = 0
    

    while True:
        #判断是否单击了关闭窗口
        for event in pygame.event.get():
            if event.type==QUIT:
                over=True
                exit() #退出程序                   
            if event.type==KEYDOWN and event.key==K_SPACE:  #判断是否按下了空格键
                if dinasaur.rect.y ==dinasaur.lowest_y:  #判断恐龙是不是在地面上
                    dinasaur.jump() #开启恐龙跳动状态
                    dinasaur.jump_audio.play() #播放音效
                    
                if game_state == "Hearing" and sound_r == 0:
                    print("jump")
                    success = True
                    num_of_failure = 0
                    score += 1
                    print("you succeed the hear-jump game")
                    obstacle.score_audio.play()
                    sound_r = -1
                    success = False
                    
            if event.type==KEYDOWN and event.key==K_DOWN:  #判断是否按下了向下键
                if dinasaur.rect.y ==dinasaur.lowest_y:  #判断恐龙是不是在地面上
                    dinasaur.squat() # 開啟恐龍蹲下狀態
                  
                if game_state == "Hearing" and sound_r == 1:
                    print("squat")
                    success = True
                    num_of_failure = 0
                    score += 1
                    print("you succeed the hear-squat game")
                    obstacle.score_audio.play()
                    sound_r = -1
                    success = False


        if over==False:
            #if not game_prepared:
                #gameStartPrepared(game_prepared)

        
            bg1.map_update() #绘制地图到更新的作用
            bg1.map_rolling() #地图移动
            bg2.map_update()
            bg2.map_rolling()
            dinasaur.move() #移动小恐龙
            #绘制恐龙
            dinasaur.draw_dinasour()
            #计算障碍物间隔的时间
            if addobstacleTimer>=1300:
                
                # 隨機產生障礙物
                obstacle_crl = random.randint(0,100)
                if obstacle_crl > 50:                                
                    #创建障碍物对象
                    obstacle=Obstacle()
                    #将障碍物推向添加到列表中
                    obstacle_list.append(obstacle)
                #重置添加障碍物的时间
                addobstacleTimer=0
                
                # 關卡控制
                
                if addLevelTimer >= 2000 and dinasaur.rect.y ==dinasaur.lowest_y:  #判断恐龙是不是在地面上
                    print(addLevelTimer)                
                    # 視覺關    
                    r=random.randint(0,100)
                    if r>50 and game_state != "Watching":
                        immune = True
                        immune_time = 200
                        game_state = "Watching"
                        print("start watch game")
                        Watch_game()
                        addLevelTimer=0

                # 聽覺關
                    if r<50  and game_state != "Hearing":
                        immune = True
                        immune_time = 100
                        game_state = "Hearing"
                        print("start Hearing game")
                        Hear_game()                             
                        success = False
                        addLevelTimer=0
                    
            # 隨機撥放跳蹲指令音效        
                sound_crl = random.randint(0,100)               
                if sound_crl > 70:                                
                    sound_r = random.randint(0,1)
                    if sound_r == 0:
                        print("play jump sound")
                        dinasaur.jump2_audio.play() #播放跳的指令音效
                        if game_state == "Watching":
                            sound_r = -1 # 回歸預設
                    if sound_r == 1:
                        print("play squat sound")
                        dinasaur.hear_audio.play() #播放蹲的指令音效
                        if game_state == "Watching":
                            sound_r = -1 # 回歸預設


            # 遍历障碍物
            for i in range(len(obstacle_list)):
                #移动障碍物
                obstacle_list[i].obstacle_move()
                #绘制障碍物
                obstacle_list[i].draw_obstacle()
                
                # 如果是免疫狀態
                if immune == True:
                    immune_time -= 1
                    #print('im', immune_time)
                    #print(immune)
                    if immune_time <= 0:
                        immune = False
                
                # 不是免疫狀態
                if immune == False:
                    
                    # 視覺關
                    if game_state == "Watching":
                        if pygame.sprite.collide_rect(dinasaur, obstacle_list[i]):
                            print("you fail the game")
                            over=True
                            game_over()
                        
                        if (obstacle_list[i].rect.x+obstacle_list[i].rect.width)<dinasaur.rect.x:
                            #加分
                            score+=obstacle_list[i].getScore()
                        
                    # 聽覺關
                    if game_state == "Hearing" and not success and sound_r != -1:  #如果進入聽覺遊戲時且未作出蹲下時
                        num_of_failure += 1 #失敗次數加1
                        print(max_num_of_failure - num_of_failure)
                        if pygame.sprite.collide_rect(dinasaur, obstacle_list[i]): # 聽覺關時遇到障礙物不會死                                       
                            over=False
                        if num_of_failure >= max_num_of_failure: # 若未在容錯次數內完成動作
                            print("you fail the extra game") #遊戲失敗
                            over = True
                            game_over2()                        
                            #exit() #退出程序
                    
                    

                
                
                obstacle_list[i].showScore(score)
                Countdown = ( max_num_of_failure - num_of_failure) // FPS 
                if Countdown >= 0:
                    obstacle_list[i].showCountdown(Countdown)

        addobstacleTimer += 20  #增加障碍物时间
        addLevelTimer += 20 # 增加關卡的時間
        pygame.display.update() #更新窗口
        FPSLOCK.tick(FPS) #多久更新一次
        

if __name__ == '__main__':
    mainGame()