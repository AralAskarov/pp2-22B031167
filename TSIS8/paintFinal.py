import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480)) # создаем экран
clock = pygame.time.Clock()

# меню пэинта
text=pygame.font.SysFont('microsofttaile',20)
finalnaya=text.render("Rectang", 0, (0,0,0))
text2=pygame.font.SysFont('microsofttaile',20)
finalnaya2=text.render("cicrle", 0, (0,0,0))
text3=pygame.font.SysFont('microsofttaile',20)
finalnaya3=text.render("Eraser", 0, (0,0,0))
text4=pygame.font.SysFont('microsofttaile',20)
finalnaya4=text.render("red", 0, (0,0,0))
text5=pygame.font.SysFont('microsofttaile',20)
finalnaya5=text.render("green", 0, (0,0,0))
text6=pygame.font.SysFont('microsofttaile',20)
finalnaya6=text.render("blue", 0, (0,0,0))

running=True
t=0 # номера фигур
c=0 # номера цветов
while running:
    
    pressed = pygame.key.get_pressed()  
        
    for event in pygame.event.get():
# cделаем меню пэинта
        pygame.draw.rect(screen,(255,255,255),(0,0,640,40))
        screen.blit(finalnaya, (0,0))
        screen.blit(finalnaya2, (90,0))
        screen.blit(finalnaya3, (180,0))
        screen.blit(finalnaya4, (270,0))
        screen.blit(finalnaya5, (360,0))
        screen.blit(finalnaya6, (450,0)) 
        

        

        if event.type == pygame.QUIT:
            running=False
        # если зажимается мышь, то смотрим где произошло нажате. если на ректангле, то будем рисовать их и тд.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse,y_mouse = pygame.mouse.get_pos()
            if x_mouse<=90 and y_mouse<=40:
                t=1
            elif x_mouse<=180 and y_mouse<=40:
                t=2
            elif x_mouse<=270 and y_mouse<=40:
                c=3
            elif x_mouse<=360 and y_mouse<=40:
                c=4
            elif x_mouse<=450 and y_mouse<=40:
                c=5
            elif x_mouse<=540 and y_mouse<=40:
                c=6
        elif event.type == pygame.MOUSEMOTION: # по движению мыши рисуются фигуры
            if t==1:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(255,255,255),[x_mouse,y_mouse,15,25],0)
            if t==2:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(255,255,255),(x_mouse,y_mouse),15,0)
            if c==3 and t==2:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(0,0,0),(x_mouse,y_mouse),15,0)
            if c== 3 and t==1:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(0,0,0),[x_mouse,y_mouse,15,25],0)
            if c==4 and t ==2:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(255,0,0),(x_mouse,y_mouse),15,0)
            if c==4 and t==1:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(255,0,0),[x_mouse,y_mouse,15,25],0)
            if c==5 and t==2:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(0,255,0),(x_mouse,y_mouse),15,0)
            if c==5 and t==1:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(0,255,0),[x_mouse,y_mouse,15,25],0)
            if c==6 and t==2:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(0,0,255),(x_mouse,y_mouse),15,0)
            if c==6 and t==1:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(0,0,255),[x_mouse,y_mouse,15,25],0)


        pygame.display.flip()
        
        clock.tick(60)

