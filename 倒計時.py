# 1
import time 

def countdown(count): 
    while (count >= 0): 
     count -= 1 
     time.sleep(1) 

countdown(2)
print("Times up!")


# 2

import pygame as py
py.init()
clock = py.time.Clock()

start_time = py.time.get_ticks()
print("started at:",start_time)

for i in range(0,30): #wait 1 second
    clock.tick(30)

end_time = py.time.get_ticks()
print("finished at:",end_time)

time_taken = end_time-start_time
print("time taken:",time_taken)



# 3
import pygame
from pygame.locals import *
def main():
    key = 0
    pygame.init()

    self = pygame.time.Clock()

    surface_sz = 480

    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)

    while True:
        ev = pygame.event.poll()

        if ev.type == pygame.QUIT:
            break;
        elif ev.type == KEYUP:
            if ev.key == K_SPACE:       #Sets the key to be used
                key += 1                #Updates counter for number of keypresses
                while ev.type == KEYUP:
                    self.tick_busy_loop()
                    test = (self.get_time()/1000.0)
                    print("number: ", key, "duration: ", test)
                    ev = pygame.event.poll()

main()
