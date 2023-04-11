import pygame
import datetime
import math
pygame.init()
running = True
black=(0,0,0)
radius=200
clock=pygame.time.Clock()
# start_pos=(0,0)
# end_pos=(0,0)
image=pygame.image.load("tsts 7 pygame copy\micky111.png")
screen=pygame.display.set_mode((800,600))
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    # print(datetime.datetime.now())
    screen.blit(image,(0,0))
    d=datetime.datetime.now()
    h=d.second
    if h<30:
        ay=h*6
        ayy=ay/360*math.pi*2
        c=math.cos(ayy)
        y=c*radius
    # print(y)
        x=math.sqrt(radius*radius-y*y)+400
    
        
    # pygame.draw.line(screen,color=(0,0,0),start_pos=(400,300),end_pos=(400,100),width=10)
        pygame.draw.line(screen,color=(0,0,0),start_pos=(400,300),end_pos=(x,300-y),width=10)
    elif h>=30:
        ay=h*6
        ayy=ay/360*math.pi*2
        c=math.cos(ayy)
        y=c*radius
    # print(y)
        x=400-math.sqrt(radius*radius-y*y)
    
        
    # pygame.draw.line(screen,color=(0,0,0),start_pos=(400,300),end_pos=(400,100),width=10)
        pygame.draw.line(screen,color=(0,0,0),start_pos=(400,300),end_pos=(x,300-y),width=10)
    m=d.minute
    
    if m<30:
        ay=m*6
        ayy=ay/360*math.pi*2
        c=math.cos(ayy)
        y=c*radius
    # print(y)
        x=math.sqrt(radius*radius-y*y)+400
    
        
    # pygame.draw.line(screen,color=(0,0,0),start_pos=(400,300),end_pos=(400,100),width=10)
        pygame.draw.line(screen,color=(0,0,0),start_pos=(400,300),end_pos=(x,300-y),width=10)
    elif m>=30:
        ay=m*6
        ayy=ay/360*math.pi*2
        c=math.cos(ayy)
        y=c*radius
    # print(y)
        x=400-math.sqrt(radius*radius-y*y)
    
        
    # pygame.draw.line(screen,color=(0,0,0),start_pos=(400,300),end_pos=(400,100),width=10)
        pygame.draw.line(screen,color=(0,0,0),start_pos=(400,300),end_pos=(x,300-y),width=10)
    pygame.display.flip()
    clock.tick(60)
