import pygame

pygame.init()
# создадим экран
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# создадим меню, кнопки
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
text7=pygame.font.SysFont('microsofttaile',20)
finalnaya7=text.render("square", 0, (0,0,0))
text8=pygame.font.SysFont('microsofttaile',20)
finalnaya8=text.render("right triangle", 0, (0,0,0))
text9=pygame.font.SysFont('microsofttaile',20)
finalnaya9=text.render("equilateral triangle", 0, (0,0,0))
text10=pygame.font.SysFont('microsofttaile',20)
finalnaya10=text.render("rhombus", 0, (0,0,0))

running=True
t=0 # фигуры
c=0 # цвета


# функции для создания фигур
def rec(x_mouse,y_mouse):
    return pygame.draw.rect(screen,(255,255,255),[x_mouse,y_mouse,15,25],0)
def cir(x_mouse,y_mouse):
    return pygame.draw.circle(screen,(255,255,255),(x_mouse,y_mouse),15,0)
def sqr(x_mouse,y_mouse):
    return pygame.draw.rect(screen,(255,255,255),[x_mouse,y_mouse,15,15],0)
def rigtr(x_mouse,y_mouse):
    return pygame.draw.polygon(screen, (255,255,255), ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)
def eqtr(x_mouse,y_mouse):
    return pygame.draw.polygon(screen, (255,255,255), ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)
def romb(x_mouse,y_mouse):
    return pygame.draw.polygon(screen, (255,255,255), ((x_mouse, y_mouse), (x_mouse+20, y_mouse-20), (x_mouse+40, y_mouse), (x_mouse+20, y_mouse+20)))


while running:
    
    pressed = pygame.key.get_pressed()  
        
    for event in pygame.event.get():

        # screen.fill((0, 0, 0))
        # добавили надписи в приложение
        pygame.draw.rect(screen,(255,255,255),(0,0,640,80))
        screen.blit(finalnaya, (0,0))
        screen.blit(finalnaya2, (90,0))
        screen.blit(finalnaya3, (180,0))
        screen.blit(finalnaya4, (270,0))
        screen.blit(finalnaya5, (360,0))
        screen.blit(finalnaya6, (450,0))
        screen.blit(finalnaya7, (0,40))
        screen.blit(finalnaya8, (90,40))
        screen.blit(finalnaya9, (240,40))
        screen.blit(finalnaya10, (444,40))  

        

        if event.type == pygame.QUIT:
            running=False
        # если нажали мышкой, то делается проверка по какой кнопке нажато, если по пустому месту, то ничего не произойдет
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
            elif x_mouse<=90 and y_mouse<=80:
                t=3
            elif x_mouse<=240 and y_mouse<=80:
                t=4
            elif x_mouse<=444 and y_mouse<=80:
                t=5
            elif x_mouse<=600 and y_mouse<=80:
                t=6
            # print(c)

        # когда ведешь мышкой, то рисуются фигруки
        elif event.type == pygame.MOUSEMOTION:
            if t==1:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                rec(x_mouse,y_mouse)
            if t==2:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                cir(x_mouse,y_mouse)
            if t==3:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                sqr(x_mouse,y_mouse)
            if t==4:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                rigtr(x_mouse,y_mouse)
            if t==5:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                eqtr(x_mouse,y_mouse)
            if t==6:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                romb(x_mouse,y_mouse)
            if c==3 and t==2:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(0,0,0),(x_mouse,y_mouse),15,0)
            if c== 3 and t==1:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(0,0,0),[x_mouse,y_mouse,15,25],0)
            if c == 3 and t == 3:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(0,0,0),[x_mouse,y_mouse,15,15],0)
            if c == 3 and t == 4:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (0,0,0), ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)
            if c == 3 and t == 5:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (0,0,0), ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)
            if c == 3 and t == 6:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (0,0,0), ((x_mouse, y_mouse), (x_mouse+20, y_mouse-20), (x_mouse+40, y_mouse), (x_mouse+20, y_mouse+20)))
            if c==4 and t==2:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(255,0,0),(x_mouse,y_mouse),15,0)
            if c== 4 and t==1:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(255,0,0),[x_mouse,y_mouse,15,25],0)
            if c == 4 and t == 3:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(255,0,0),[x_mouse,y_mouse,15,15],0)
            if c == 4 and t == 4:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (255,0,0), ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)
            if c == 4 and t == 5:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (255,0,0), ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)
            if c == 4 and t == 6:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (255,0,0), ((x_mouse, y_mouse), (x_mouse+20, y_mouse-20), (x_mouse+40, y_mouse), (x_mouse+20, y_mouse+20)))
            
            
            if c==5 and t==2:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(0,255,0),(x_mouse,y_mouse),15,0)
            if c== 5 and t==1:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(0,255,0),[x_mouse,y_mouse,15,25],0)
            if c == 5 and t == 3:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(0,255,0),[x_mouse,y_mouse,15,15],0)
            if c == 5 and t == 4:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (0,255,0), ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)
            if c == 5 and t == 5:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (0,255,0), ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)
            if c == 5 and t == 6:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (0,255,0), ((x_mouse, y_mouse), (x_mouse+20, y_mouse-20), (x_mouse+40, y_mouse), (x_mouse+20, y_mouse+20)))
            
            
            if c==6 and t==2:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(screen,(0,0,255),(x_mouse,y_mouse),15,0)
            if c==6 and t==1:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(0,0,255),[x_mouse,y_mouse,15,25],0)
            if c == 6 and t == 3:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.rect(screen,(0,0,255),[x_mouse,y_mouse,15,15],0)
            if c == 6 and t == 4:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (0,0,255), ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)
            if c == 6 and t == 5:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (0,0,255), ((x_mouse, y_mouse), (x_mouse, y_mouse+40), (x_mouse+40, y_mouse+40)), 0)
            if c == 6 and t == 6:
                x_mouse,y_mouse = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, (0,0,255), ((x_mouse, y_mouse), (x_mouse+20, y_mouse-20), (x_mouse+40, y_mouse), (x_mouse+20, y_mouse+20)))


        pygame.display.flip()
        
        clock.tick(60)
