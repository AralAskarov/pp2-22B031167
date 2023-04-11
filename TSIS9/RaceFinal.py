import pygame
import random
pygame.init()
screen=pygame.display.set_mode((400,600)) # создали экран

global z
clock=pygame.time.Clock()
running = True
dx=dy=0 # положение синей машины меняем
dx2=dy2=0 # положение красной машины меняем
step=15 # шаг машин
x=y=0 
x2=y2=0 # нач положение красной
x4=y4=0 # нач положение коинов
aa=0 # для контроля того, каким монетам сколько очков
bb=0
cc=0 
speed=1 # скорость игры

a3=0 # проверка какая монета выпала
b3=0
c3=0

sum=0
# добавим изображения
image1=pygame.image.load("tsis 9 pygame\AnimatedStreet.png")
image2=pygame.image.load("tsis 9 pygame\Player.png")
w2,h2=image2.get_size()
image3=pygame.image.load("tsis 9 pygame\Enemy.png")
w3,h3=image3.get_size()
image4=pygame.image.load("tsis 9 pygame\coin.png")
resized_image4=pygame.transform.scale(image4,(40,40))
image5=pygame.image.load("tsis 9 pygame\sssssss.png")
# w3,h3=image3.get_size()
image6=pygame.image.load("tsis 9 pygame\pngegg.png")
resized_image5=pygame.transform.scale(image5,(70,70))
resized_image6=pygame.transform.scale(image6,(70,70))

text=pygame.font.SysFont('microsofttaile',32)
text2=pygame.font.SysFont('microsofttaile',32)

# для рандомнго положения красной машины по х
def randommm():
    x=random.randint(0,400-w3)
    y=0
    redcar = redcars(x,y)
    return redcar.x2
# вес коина 
def randomcoin():
    a=random.randint(0,10)
    y=0
    redcar = redcars(a,y)
    return redcar.x2

# cоздали класс, чтобв удобнее было работать с красными машинами
class redcars:
    def __init__(self,x2,y2):
        self.x2=x2
        self.y2=y2
# cоздали класс, чтобв удобнее было работать с коинами
class coins:
    def __init__(self,x4,y4):
        self.x4=x4
        self.y4=y4
    
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    screen.blit(image1,(0,0)) # фон
    pressed=pygame.key.get_pressed() # считываем нажатия клавиш
    
    # создали движение синей машины
    if(pressed[pygame.K_LEFT] and x>0 and x<=400):
        dx=-1
        dy=0
    elif(pressed[pygame.K_RIGHT] and x>=0 and x<400-w2):
        dx=1
        dy=0
    else:
        dx=0

    
    # cмещение в пространстве синей машины
    x += dx * step
    y += dy * step

# изобр синей машины
    screen.blit(image2,(x,600-h2))
    final=text.render(f'coins: {sum}', 0, (255,255,255)) # счет очков
    screen.blit(final,(0,0))
    finaall=text2.render(f'speed: {speed}', 0, (255,255,255)) # счет скорости
    screen.blit(finaall,(0,40))


# вначале кр машина в 0 по у, а потом меняет положение по у, если столкнется с машиной то конец игре, если не врежется, то y выйдет за пределы экрана, тогда создастся новая машина. та же логика с коинами
    if y2==0: 
        a=redcars(randommm(),y2)
    a.y2+=25
    y2+=25
    screen.blit(image3,(a.x2,a.y2))
    if(y2>600):
        a.y2=0
        y2=0
    
    if y4==0:
        c=coins(randommm(),y4)
        
        z=randomcoin()
        # если 1-5 то коин весом 1 очко, для 6-8 2 очка, для 9-10 3 очка
        if(z>=1 and z<=5):
           aa=1
        elif(z>=6 and z<=8):
           bb=1
        elif z>=9 and z<=10:
            cc=1
    c.y4+=25
    y4+=25
    if aa==1:
        screen.blit(resized_image4,(c.x4,c.y4))
        a3=1
    elif(bb==1):
        screen.blit(resized_image5,(c.x4,c.y4))
        b3=1
    else:
        screen.blit(resized_image6,(c.x4,c.y4))
        c3=1
    if y4>600:
        c.y4=0
        y4=0
        aa=0
        bb=0
        cc=0
        
    
    if x-w2//2<=c.x4 and x+w2//2>=c.x4 and y==c.y4:
        speed = sum//12 + 1 # каждые 12 очков повышение скорости
        
        if c3==1:
           c3=0
           sum+=3
           c.y4=1000
           print(sum)
        elif b3==1:
            b3=0
            sum+=2
            c.y4=1000
            print(sum)
        elif a3==1:
            a3=0
            sum+=1
            c.y4=1000
            print(sum)

    if x-w2<=a.x2 and x+w2>=a.x2 and 600-h2<=y2 and 600>=y2: # если врещется, то конеу игре и будет звук и игра заново стартанет
        music=pygame.mixer.Sound('tsis 9 pygame\Lab_8_rider_crash.wav')
        music.play()
        screen.fill((0,0,0))
        sum=0

    pygame.display.flip()
    clock.tick(20)