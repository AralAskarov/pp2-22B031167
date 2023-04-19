
import pygame
import sys
import random
pygame.init()



running=True


text=pygame.font.SysFont('microsofttaile',32)
text_speed=pygame.font.SysFont('microsofttaile',32)
text_level=text=pygame.font.SysFont('microsofttaile',32)


# цвета
screen_color = (0,255,204)
white = (255,255,255)
blue = (204,255,255)
header_color=(0,204,153)
snake_color=(0,102,0)
red=(255,0,0)
level=0
clock=pygame.time.Clock()

SIZE_BLOCK=20
COUNT_BLOCK=20
prob=3
header_margin=70
d_row=1
d_col=0
total = 0
speed = 1
t = True
size=(SIZE_BLOCK*COUNT_BLOCK+(COUNT_BLOCK+1)*prob+1+2*SIZE_BLOCK,header_margin+SIZE_BLOCK*COUNT_BLOCK+COUNT_BLOCK*prob+2*SIZE_BLOCK)

screen=pygame.display.set_mode((size))
pygame.display.set_caption("SNAKE 3.0")



class SNAKE_BLOCK:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def isinside(self):
        
            
        return  0<=self.x<SIZE_BLOCK and 0 <= self.y <SIZE_BLOCK
    def isindark(self,block):
        return head.x==self.x and head.y==self.y
        
        # return 0<=self.x<SIZE_BLOCK and 0 <= self.y <SIZE_BLOCK
        # print(0<=self.x<SIZE_BLOCK and 0 <= self.y <SIZE_BLOCK)
        # return 0<=self.x<SIZE_BLOCK and 0 <= self.y <SIZE_BLOCK
    

    def __eq__(self,other): # метод eq чтобы есть яблоки
        return self.x== other.x and self.y == other.y


SNAKE_BLOCKS=[SNAKE_BLOCK(9,9), SNAKE_BLOCK(9,10), SNAKE_BLOCK(9,11)]

def DRAWRECT(color,i,j):
    pygame.draw.rect(screen,color,(SIZE_BLOCK+i*SIZE_BLOCK+(i+1)*prob,header_margin+SIZE_BLOCK+j*SIZE_BLOCK+(j+1)*prob,SIZE_BLOCK,SIZE_BLOCK))


def getrandomemptyblock():
    x=random.randint(0,COUNT_BLOCK-1) # включает границы
    y=random.randint(0,COUNT_BLOCK-1)
    empty_block=SNAKE_BLOCK(x,y)
    while empty_block in SNAKE_BLOCKS: # если емпти блок совпадает с блок внутри змейки. выйдем из цикла если блока нет в змейке
        empty_block.x=random.randint(0,COUNT_BLOCK-1)
        empty_block.y=random.randint(0,COUNT_BLOCK-1)
    while empty_block in kordlevel1:
        empty_block.x=random.randint(0,COUNT_BLOCK-1)
        empty_block.y=random.randint(0,COUNT_BLOCK-1)

    return empty_block


kordlevel1=[]

ass=getrandomemptyblock()        
apple=getrandomemptyblock()


while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col==0:
                d_row=0
                d_col=-1
            elif event.key == pygame.K_DOWN and d_col==0:
                d_row=0
                d_col=1
            elif event.key == pygame.K_LEFT and d_row==0:
                d_row=-1
                d_col=0
            elif event.key == pygame.K_RIGHT and d_row==0:
                d_row=1
                d_col=0
    


    screen.fill(screen_color)
    pygame.draw.rect(screen,header_color,(0,0,COUNT_BLOCK*SIZE_BLOCK+(prob)+2*SIZE_BLOCK*COUNT_BLOCK,header_margin))

    finalnaya=text.render(f"Total: {total}", 0, white)
    totspeed=text_speed.render(f"Speed: {speed}", 0, white)
    totlevel=text_level.render(f"Level: {level}", 0 , white)


    screen.blit(finalnaya, (SIZE_BLOCK,SIZE_BLOCK))
    screen.blit(totspeed, (SIZE_BLOCK + 150,SIZE_BLOCK))
    screen.blit(totlevel, (SIZE_BLOCK+300, SIZE_BLOCK))
    


    
    for i in range(COUNT_BLOCK):
        for j in range(COUNT_BLOCK):
            if (i+j)%2 == 0:
                color=blue
            else:
                color=white
            DRAWRECT(color,i,j)
        



    head = SNAKE_BLOCKS[-1]
    if not head.isinside():
        print("DEAD")
        running=False
        sys.exit()

   
    for block in SNAKE_BLOCKS:
        DRAWRECT(snake_color,block.x,block.y)
    for kord in kordlevel1:
        if kord.isindark(head):
            print("DEAD")
            running=False
            sys.exit()

    if apple==head:
        SNAKE_BLOCKS.append(apple) 
        apple= getrandomemptyblock()
        total+=1
        speed=total//5+1
        if total>=1 and total<5:
            kordlevel1=[]
            for i in range(10):
                deadblock=getrandomemptyblock()
            
                kordlevel1.append(deadblock)
                print(len(kordlevel1))
                level=1
        if total>=5 and total<10:
            korlevel1=[]
            for i in range(15):
                deadblock=getrandomemptyblock()
                level=2
            
                kordlevel1.append(deadblock)
                print(len(kordlevel1))
        if total>=10 and total<15:
            korlevel1=[]
            for i in range(20):
                deadblock=getrandomemptyblock()
                level=3
                kordlevel1.append(deadblock)
                print(len(kordlevel1))
        if  total>=15 and total<20:
            korlevel1=[]
            for i in range(25):
                deadblock=getrandomemptyblock()
                level=4
                kordlevel1.append(deadblock)
                print(len(kordlevel1))
        if total>=20:
            korlevel1=[]
            for i in range(30):
                deadblock=getrandomemptyblock()
                level=5
                kordlevel1.append(deadblock)
                print(len(kordlevel1))
                
        
    for block in kordlevel1:
        DRAWRECT((0,0,0),block.x,block.y)    

    head_block=SNAKE_BLOCKS[-1]
    new_head=SNAKE_BLOCK(head_block.x+d_row,head_block.y+d_col)

    SNAKE_BLOCKS.append(new_head)
    SNAKE_BLOCKS.pop(0)

    DRAWRECT(red, apple.x, apple.y)
    pygame.display.flip()
    clock.tick(3+speed)