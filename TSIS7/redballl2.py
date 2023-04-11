import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("red ball")

running = True
clock=pygame.time.Clock()
step=20
x=y=100
radius=25
dx=dy=0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.fill((255,255,255))
    pressed=pygame.key.get_pressed()

    if pressed[pygame.K_UP] and y>25:
        y-=step
        # dx=0
    if pressed[pygame.K_DOWN] and y<500-radius:
        y+=step
        # dx=0
    if pressed[pygame.K_RIGHT] and x<500-radius:
        x+=step
        # dy=0
    if pressed[pygame.K_LEFT] and x>25:
        x-=step
        # dy=0
    # else:
    #     dx=0
    #     dy=0
    
    pygame.draw.circle(screen,(255,0,0),(x,y),radius)
    clock.tick(10)
    pygame.display.flip()
