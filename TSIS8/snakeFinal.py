# библиотеки
import pygame
import sys # чтобы игра кончалась хорошим кодом выхода без ошибки. дальше не читает код
import random
pygame.init()


# fps
clock=pygame.time.Clock()

# цвета
screen_color = (0,255,204)
white = (255,255,255)
blue = (204,255,255)
header_color=(0,204,153)
snake_color=(0,102,0)
red=(255,0,0)


#  переменные
x=y=20
SIZE_BLOCK = 20 # размер блока
COUNT_BLOCK = 20 # количество блоков
probel=1 # отступы между блоками
header_margin=70 # для надписи над змейкой
total=0 # сколько очков
speed = 1 # скорость змейки


# текста
text=pygame.font.SysFont('microsofttaile',32)
text_speed=pygame.font.SysFont('microsofttaile',32)


# размер экрана зависит от количества кубиков в змейке
size=(SIZE_BLOCK*COUNT_BLOCK + 2*SIZE_BLOCK + probel*COUNT_BLOCK,SIZE_BLOCK*COUNT_BLOCK + 2*SIZE_BLOCK + probel*COUNT_BLOCK+header_margin)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("SNAKE")
running = True


class SnakeBlock: # будем хранить корды х и у в классе каждого блока, а объекты класса в листе
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def isinside(self): # чтобы при ударе о стену кончалась игра
            return 0<=self.x<COUNT_BLOCK and 0 <= self.y <COUNT_BLOCK
    
    def __eq__(self,other): # метод eq  чтобы яблоко не появлалась в змее
        return self.x== other.x and self.y == other.y



snake_blocks=[SnakeBlock(9,8), SnakeBlock(9,9), SnakeBlock(9,10)] #  начальная змейка из 3 блоков, вначале из 1 блока змейка, стоит в центре
# голова будет в конце списка, в 0 индексе конец змеи

# яблоко будет блоко змеи но другого цвета

def drawblock(color,row,col): # функция для создания блоков
    pygame.draw.rect(screen, color, [SIZE_BLOCK+(col*SIZE_BLOCK)+ probel*(col+1),header_margin + SIZE_BLOCK +(row*SIZE_BLOCK)+probel*(row+1), SIZE_BLOCK,SIZE_BLOCK])

def getrandomemptyblock(): # функция ничего не примет, а вернет снэйк блок
    # генерим 2 числа для х и у
    x=random.randint(0,COUNT_BLOCK-1) # включает границы
    y=random.randint(0,COUNT_BLOCK-1)
    empty_block = SnakeBlock(x,y) 
    while empty_block in snake_blocks: # если емпти блок совпадает с блок внутри змейки. выйдем из цикла, если блока нет в змейке
        empty_block.x=random.randint(0,COUNT_BLOCK-1)
        empty_block.y=random.randint(0,COUNT_BLOCK-1)
    return empty_block
apple = getrandomemptyblock() # cоздали яблоко


d_row=0
d_col=1 # движение всегда стартует вправо. сразу начинается игра

while running:
    screen.fill(screen_color)
    pygame.draw.rect(screen,header_color,[0,0,size[0],header_margin]) #рисуем меню над змейкой
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.KEYDOWN: # настройка движения змеейки по полю
            if event.key == pygame.K_UP and d_col!=0: # проверка на то может ли идти назад. если до этого шли по верху, то можно вбок
                d_row=-1
                d_col=0
            elif event.key == pygame.K_DOWN and d_col!=0:
                d_row=1
                d_col=0
            elif event.key == pygame.K_LEFT and d_row!=0:
                d_row=0
                d_col= -1
            elif event.key == pygame.K_RIGHT and d_row!=0:
                d_row=0
                d_col=1
    
    finalnaya=text.render(f"Total: {total}", 0, white) # текст количества очков
    totspeed=text_speed.render(f"Speed: {speed}", 0, white) # текст скорости

    screen.blit(finalnaya, (SIZE_BLOCK,SIZE_BLOCK))  # добавили текст на экран
    screen.blit(totspeed, (SIZE_BLOCK + 150,SIZE_BLOCK))

    for row in range(COUNT_BLOCK): # 0-19
        for col in range(COUNT_BLOCK): # создаем поле
            if (row + col) % 2 == 0: # чтобы цвета полей чередовались
                color=blue
            else:
                color=white
            drawblock(color,row,col)

    # змейка движется по принципу того, что впереди создается блока змейки, а сзади удаляется
    head = snake_blocks[-1] # -1 это конец листа
    if not head.isinside(): # проверка на проигрыш игры
        print("DEAD")
        running=False
        sys.exit()
    
    drawblock(red, apple.x, apple.y) # создали яблоко на поле   
    for block in snake_blocks: # каждый раз рисуются элементы змейки
        drawblock(snake_color,block.x,block.y) # знаем что х это х а у это у. не нужны индексы, где стоят корды, не нужно обращ по индексу
        # сначала рисуем старые значения а потом новые
        
    

    if apple==head:  # чтобы можно было есть яблоки
        total += 1 # очки за съеденные яблоки
        speed = total//5 + 1 # увеличение скорости каждое 5 яблоко
        snake_blocks.append(apple) # Добавим яблоко в конец списк снэйк блокс, так увеличивается размер змейки
        apple= getrandomemptyblock() # создали новое и добавили в рандом место
       

    head = snake_blocks[-1] # -1 это конец листа
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    # создали новый обьект и добавим его в конец. новая голова
    snake_blocks.append(new_head)
    # удалим первый блок
    snake_blocks.pop(0)

    pygame.display.flip()
    clock.tick(3 + speed) # fps