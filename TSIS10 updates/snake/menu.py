import pygame
import sys
import random
import pygame_menu
pygame.init()
running=True


text=pygame.font.SysFont('microsofttaile',32)
text_speed=pygame.font.SysFont('microsofttaile',32)
text_level=text=pygame.font.SysFont('microsofttaile',32)



# цвета
screen_color = (0,255,204) # цвет для поля по фану
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
# size=(SIZE_BLOCK*COUNT_BLOCK + 2*SIZE_BLOCK + probel*COUNT_BLOCK,SIZE_BLOCK*COUNT_BLOCK + 2*SIZE_BLOCK + probel*COUNT_BLOCK+header_margin)

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
# print(SNAKE_BLOCKS)
# for block in SNAKE_BLOCKS:
#     print (block.x,block.y)
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
# print(len(kordlevel1))
# def getrandomkordlevel1():
#     x=random.randint(0,COUNT_BLOCK-1)
#     y=random.randint(0,COUNT_BLOCK-1)
#     empty=SNAKE_BLOCK(x,y)
#     # while empty in kordlevel1:
#     #     empty.x=random.randint(0,COUNT_BLOCK-1)
#     #     empty.y=random.randint(0,COUNT_BLOCK-1)
#     return empty        
ass=getrandomemptyblock()        
apple=getrandomemptyblock()

    # print(a.x)
    # print(kordlevel1)
# for kord in kordlevel1:
#     a=kord.x
#     b=kord.y
#     print(a,b)


def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Demian')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
