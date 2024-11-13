import pygame
import random

pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("space invador(original)")

fire_rad=10
fire_x=250
fire_y=10
fire_color=(169, 66, 63)

rgb_backround_color=(0,0,0)

rc_color=(243,30,104)
rc_h=50
rc_w=25
rc_x=250
rc_y=400

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()


    if fire_y>520:
        fire_y=-20
        fire_x=random.randint(10,490)

    else:
        fire_y=fire_y+5


    key=pygame.key.get_pressed() 


    if key[pygame.K_LEFT]:
        rc_x=rc_x-5 

    if key[pygame.K_RIGHT]:
        rc_x=rc_x+5 

    if key[pygame.K_UP]:
        rc_y=rc_y-5 

    if key[pygame.K_DOWN]:
        rc_y=rc_y+5 

    screen.fill(rgb_backround_color)

    pygame.draw.circle(screen,fire_color,(fire_x,fire_y),fire_rad)
    pygame.draw.rect(screen,rc_color,(rc_x,rc_y,rc_w,rc_h))

    pygame.time.delay(15)
    pygame.display.update()

    

