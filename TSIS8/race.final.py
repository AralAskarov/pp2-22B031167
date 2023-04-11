import pygame
import random
pygame.init()
screen=pygame.display.set_mode((400,600)) # создаем поле

clock=pygame.time.Clock() # fps
running = True
dx=dy=0 # для создания движения синей машины
dx2=dy2=0 # для создания движения красной машины
step=15 # шаг смещения
x=y=0 
x2=y2=0 # нач положение красной машины
x4=y4=0 # нач положение коина

#  количество монет
sum=0

# добавим изображения
image1=pygame.image.load("tsis 8 pygame\AnimatedStreet.png")
image2=pygame.image.load("tsis 8 pygame\Player.png")
w2,h2=image2.get_size()
image3=pygame.image.load("tsis 8 pygame\Enemy.png")
w3,h3=image3.get_size()
image4=pygame.image.load("tsis 8 pygame\coin.png")
resized_image4=pygame.transform.scale(image4,(40,40))

text=pygame.font.SysFont('microsofttaile',32)

# рандомное положение красной машины по х
def randommm():
    x=random.randint(0,400-w3)
    y=0
    redcar = redcars(x,y)
    
    return redcar.x2
# класс красных машин
class redcars:
    def __init__(self,x2,y2):
        self.x2=x2
        self.y2=y2
# класс коинов, чтобы удобней с ними работать
class coins:
    def __init__(self,x4,y4):
        self.x4=x4
        self.y4=y4
    
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    screen.blit(image1,(0,0)) 
    pressed=pygame.key.get_pressed() # принимаем клики
    
    # создадим движение синей машимны
    if(pressed[pygame.K_LEFT] and x>0 and x<=400):
        dx=-1
        dy=0
    elif(pressed[pygame.K_RIGHT] and x>=0 and x<400-w2):
        dx=1
        dy=0
    else:
        dx=0
    
    # текущее положение синей машины
    x += dx * step 
    y += dy * step


    # добавим синюю машину и счетчик коинов
    screen.blit(image2,(x,600-h2))
    final=text.render(f'coins: {sum}', 0, (255,255,255))
    screen.blit(final,(0,0))
    #  в начале y2 =0 , потом оно увел, и когда дойдет до конца, то обнулиться и появиться новая машина.

    if y2==0:
        a=redcars(randommm(),y2)
    a.y2+=25
    y2+=25


    screen.blit(image3,(a.x2,a.y2))
    if(y2>600):
        a.y2=0
        y2=0
    
    # Логика красной машинв распространяется на коины
    if y4==0:
        c=coins(randommm(),y4)
    c.y4+=25
    y4+=25
    screen.blit(resized_image4,(c.x4,c.y4))
    if y4>600:
        c.y4=0
        y4=0
    
    if x-w2<=c.x4 and x+w2>=c.x4 and y==c.y4: # сбор коинов
        sum+=1
        c.y4=1000
        print(sum)

    if x-w2<=a.x2 and x+w2>=a.x2 and 600-h2<=y2 and 600>=y2: # авария
        music=pygame.mixer.Sound('tsis 8 pygame\Lab_8_rider_crash.wav')
        music.play()
        screen.fill((0,0,0))
        sum=0

    pygame.display.flip()
    clock.tick(20)