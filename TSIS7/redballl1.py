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
        dy=-1
        dx=0
    elif pressed[pygame.K_DOWN] and y<500-radius:
        dy=1
        dx=0
    elif pressed[pygame.K_RIGHT] and x<500-radius:
        dx=1
        dy=0
    elif pressed[pygame.K_LEFT] and x>25:
        dx=-1
        dy=0
    else:
        dx=0
        dy=0
    x+=dx*step
    y+=dy*step
    pygame.draw.circle(screen,(255,0,0),(x,y),radius)
    clock.tick(10)
    pygame.display.flip()
