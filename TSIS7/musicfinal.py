import pygame
pygame.init()

screen=pygame.display.set_mode((500,500))

running=True
text1=pygame.font.SysFont('comicsansms',16)
text2=pygame.font.SysFont('comicsansms',16)
text3=pygame.font.SysFont('comicsansms',16)
text4=pygame.font.SysFont('comicsansms',16)
start=text1.render("Запуск песни",1,(0,0,0),(120,120,120))
pause=text2.render("Пауза",1,(0,0,0),(120,120,120))
previous=text3.render("Предыдущая песня",1,(0,0,0),(120,120,120))
next=text4.render("Следующая песня",1,(0,0,0),(120,120,120))
# music1 = pygame.mixer.Sound(".\Tame Impala - Let It Happen_(muzfan.net).mp3")
# music1 = pygame.mixer.music.load("tsts 7 pygame\TameImpalaLetitHappen_(muzfan.net).mp3")
# music2 = pygame.mixer.Sound("tame-impala-the-less-i-know-the-better.mp3")
music1 = pygame.mixer.Sound("tsts 7 pygame\TameImpalaLetitHappen_(muzfan.net).mp3")
music2 = pygame.mixer.Sound("tsts 7 pygame\Tame_impala_the_less_i_know_the_better.mp3")
music3 = pygame.mixer.Sound("tsts 7 pygame\Tame_Impala_No_Choice_(musmore.com).mp3")

w1,h1=start.get_size()
w2,h2=pause.get_size()
w3,h3=previous.get_size()
w4,h4=next.get_size()
playlist = [music1,music2]
t=0
index=0

pygame.mixer.init()
playlisy=["tsts 7 pygame\TameImpalaLetitHappen_(muzfan.net).mp3","tsts 7 pygame\Tame_impala_the_less_i_know_the_better.mp3", "tsts 7 pygame\Tame_Impala_No_Choice_(musmore.com).mp3"]
pygame.mixer.music.load(playlisy[index])
mas=[]
for i in range(10):
    a=[0]*10
    mas.append(a)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x={x_mouse} y={y_mouse}')
            if x_mouse>=120 and x_mouse<=120+w1 and y_mouse>=0 and y_mouse<=h1 and t==0:
                pygame.mixer.music.play()
                t=1
            elif x_mouse>=120 and x_mouse<=120+w2 and y_mouse>=100 and y_mouse<=100+h2:
                pygame.mixer.music.pause()
            elif x_mouse>=120 and x_mouse<=120+w1 and y_mouse>=0 and y_mouse<=h1 and t==1:
                pygame.mixer.music.unpause()
            
            elif x_mouse>=120 and x_mouse<=120+w4 and y_mouse>=300 and y_mouse<=300+h4:
                if index<=len(playlisy)-1 and index>=0:
                    index+=1
                    if index==3:
                        index=0
                        pygame.mixer.music.load(playlisy[index])
                        pygame.mixer.music.play()
                    else:
                        print(index)
                        pygame.mixer.music.load(playlisy[index])
                        pygame.mixer.music.play()
                
            elif x_mouse>=120 and x_mouse<=120+w3 and y_mouse>=200 and y_mouse<=200+h3:
                if index<len(playlisy) and index>=0:
                    index-=1
                    if index<0:
                        print(index)
                        index=2
                        pygame.mixer.music.load(playlisy[index])
                        pygame.mixer.music.play()
                    else:
                        print(index)
                        pygame.mixer.music.load(playlisy[index])
                        pygame.mixer.music.play()
                
                # pygame.mixer.music.play()
            # elif index==3:
            #     index=0
            #     pygame.mixer.music.load(playlisy[index])
            #     pygame.mixer.music.play()
            # elif index==-1:
            #     index=3
            #     pygame.mixer.music.load(playlisy[index])
            #     pygame.mixer.music.play()

                
            
                

    # music1.load(".\Tame Impala - Let It Happen_(muzfan.net).mp3")
    # pygame.mixer.music.play(0)
    # music1.play()
    # music2.play()
    screen.fill((255,255,255))
    screen.blit(start,(120,0))
    screen.blit(pause,(120,100))
    screen.blit(previous,(120,200))
    screen.blit(next,(120,300))
    pygame.display.flip()
