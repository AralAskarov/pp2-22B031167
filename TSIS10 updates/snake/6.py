
import pygame
import sys
import random
import pygame_menu
import psycopg2
pygame.init()
conn = psycopg2.connect(    
            database="aral",
            user="postgres",
            password="aral2197",
            host="localhost",
            port="5432")
cur=conn.cursor()
print('введите имя')
userrrr=str(input())
t=1
# sql = cur.mogrify('''SELECT * FROM snake1 WHERE username=userrrr''')
# sql = cur.mogrify('''SELECT * FROM snake1 WHERE username (%s) ''', (userrrr))

# # print(sql)

# cur.execute(sql)

# print(cur.fetchall())
# sql='''SELECT * FROM snake1 WHERE username (%s) '''
# cur.execute(sql,(userrrr,))
# print(cur.fetchone())
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM snake_score2")
    rec = cur.fetchall()
    for row in rec:
        if row[0]==userrrr:
            t=0
            print("username ",row[0])
            print("score ",row[1])
            print("level ",row[2])
if t == 1:
    sql = """ INSERT INTO snake1 (username) VALUES (%s) """
    cur.execute(sql,(userrrr,))
# cur.execute('''INSERT INTO snake1(user)
# VALUES(%s)
# (userrrr);''')
# sql = '''INSERT INTO snake1(username) VALUES(%s)'''
# cur.execute(sql,str(userrrr))
# cur.execute('''INSERT INTO snake1  VALUES ('{userrrr}');''')

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
        return block.x==self.x and block.y==self.y
        
        # return 0<=self.x<SIZE_BLOCK and 0 <= self.y <SIZE_BLOCK
        # print(0<=self.x<SIZE_BLOCK and 0 <= self.y <SIZE_BLOCK)
        # return 0<=self.x<SIZE_BLOCK and 0 <= self.y <SIZE_BLOCK
    

    def __eq__(self,other): # метод eq чтобы есть яблоки
        return self.x== other.x and self.y == other.y


SNAKE_BLOCKS=[SNAKE_BLOCK(9,9), SNAKE_BLOCK(9,10), SNAKE_BLOCK(9,11)]
# head = SNAKE_BLOCKS[-1]
# print(SNAKE_BLOCKS)
# for block in SNAKE_BLOCKS:
#     print (block.x,block.y)
def DRAWRECT(color,i,j):
    pygame.draw.rect(screen,color,(SIZE_BLOCK+i*SIZE_BLOCK+(i+1)*prob,header_margin+SIZE_BLOCK+j*SIZE_BLOCK+(j+1)*prob,SIZE_BLOCK,SIZE_BLOCK))

def start_the_game():
    SNAKE_BLOCKS=[SNAKE_BLOCK(9,9), SNAKE_BLOCK(9,10), SNAKE_BLOCK(9,11)]

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
    total=0
    speed=1
    level=0
    d_row=1
    d_col=0
    # print(a.x)
    # print(kordlevel1)
    # for kord in kordlevel1:
    #     a=kord.x
    #     b=kord.y
    #     print(a,b)

    while 1:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('EXIT')
                quit()
                sys.exit()
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

        # pygame.draw.rect(screen,header_color,(100,100,COUNT_BLOCK*SIZE_BLOCK+(prob)+2*SIZE_BLOCK*COUNT_BLOCK,header_margin))

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
                #     pygame.draw.rect(screen,color,(SIZE_BLOCK+i*COUNT_BLOCK+i*COUNT_BLOCK,SIZE_BLOCK+i*COUNT_BLOCK+i*COUNT_BLOCK,SIZE_BLOCK,SIZE_BLOCK))
                else:
                    color=white
                ### pygame.draw.rect(screen,color,(SIZE_BLOCK+i*SIZE_BLOCK+(i+1)*prob,header_margin+SIZE_BLOCK+j*SIZE_BLOCK+(j+1)*prob,SIZE_BLOCK,SIZE_BLOCK))
                DRAWRECT(color,i,j)
            
            # pygame.draw.rect(screen, color, [SIZE_BLOCK+(col*SIZE_BLOCK)+ probel*(col+1),header_margin + SIZE_BLOCK +(row*SIZE_BLOCK)+probel*(row+1), SIZE_BLOCK,SIZE_BLOCK])



        head = SNAKE_BLOCKS[-1] # -1 это конец листа
        if not head.isinside():
            print("DEAD")
            sql = """ INSERT INTO snake_score2 (username, score, level) VALUES (%s,%s,%s) """
            cur.execute(sql,(userrrr, total, level))
        
            conn.commit()
            cur.close()
            conn.close()

            start_the_game
            break
            sys.exit()
            break

        # DRAWRECT(red, apple.x, apple.y)
        # print(apple.x)
        for block in SNAKE_BLOCKS:
            DRAWRECT(snake_color,block.x,block.y)
            # if not block.isinside():
            #     print("DEAD")
            #     running=False
            #     sys.exit()
            # block.y += d_col
            # block.x += d_row
        for kord in kordlevel1:
            if kord.isindark(head):
                sql = """ INSERT INTO snake_score2 (username, score, level) VALUES (%s,%s,%s) """
                cur.execute(sql,(userrrr, total, level))
                conn.commit()
                cur.close()
                conn.close()
                print("DEAD")
                quit()
                sys.exit()
                
        
        # print(ass.x)
        if apple==head:
            SNAKE_BLOCKS.append(apple) # Добавим яблоко в конец списк снэйк блокс
            apple= getrandomemptyblock()
            total+=1
            speed=total//5+1
            if total==1:
                for i in range(10):
                    ass=getrandomemptyblock()
                
                    kordlevel1.append(ass)
                    print(len(kordlevel1))
                    level=1
            if total==5:
                korlevel1=[]
                for i in range(15):
                    ass=getrandomemptyblock()
                    level=2
                
                    kordlevel1.append(ass)
                    print(len(kordlevel1))
            if total==10:
                korlevel1=[]
                for i in range(20):
                    ass=getrandomemptyblock()
                    level=3
                    kordlevel1.append(ass)
                    print(len(kordlevel1))
            if total==15:
                korlevel1=[]
                for i in range(25):
                    ass=getrandomemptyblock()
                    level=4
                    kordlevel1.append(ass)
                    print(len(kordlevel1))
            if total==20:
                korlevel1=[]
                for i in range(30):
                    ass=getrandomemptyblock()
                    level=5
                    kordlevel1.append(ass)
                    print(len(kordlevel1))
                    
        for block in kordlevel1:
            DRAWRECT((0,0,0),block.x,block.y)    

        head_block=SNAKE_BLOCKS[-1]
        new_head=SNAKE_BLOCK(head_block.x+d_row,head_block.y+d_col)
        # new_head=SNAKE_BLOCK(head_block.x+d_col,head_block.y+d_row)

        SNAKE_BLOCKS.append(new_head)
        SNAKE_BLOCKS.pop(0)

        # head = snake_blocks[-1] # -1 это конец листа
        # new_head = SnakeBlock(head.x + d_row, head.y + d_col)
        # # создали новый обьект и добавим его в конец. новая голова
        # snake_blocks.append(new_head)
        # # удалим первый блок
        # snake_blocks.pop(0)
        DRAWRECT(red, apple.x, apple.y)
       
        pygame.display.flip()
        clock.tick(3+speed)
        



menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)
default=userrrr
menu.add.text_input('Name :', default)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
conn.commit()
cur.close()
conn.close()