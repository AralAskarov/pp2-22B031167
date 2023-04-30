import random#importing libs
import pygame
from collections import deque
import psycopg2
def pause(user,score,level):
    text_s = my_font.render('SAVE', False, (250, 0, 0))
    loop = 1
    svb = Button(WIDTH//2 + 100,HEIGHT//2 + 100,300,50,(0,255,0),text_s)
    #upd_usrscre(user, score, level)
    while loop:
        SCREEN.fill((0, 0, 0))
        text_f = my_font.render('PAUSED', False, (250, 0, 0))
        SCREEN.blit(text_f, (WIDTH//2,HEIGHT//2)) 
        svb.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.MOUSEBUTTONDOWN:#NEW Game button check
                if svb.rect.collidepoint(event.pos):
                    upd_usrscre(user,score,level)
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    loop = 0
        pygame.display.update()
        clock.tick(60)
print("User Name? : ")
user = str(input())
def print_table_userscores():   
    connection = psycopg2.connect(    
            database="snakescore",
            user="postgres",
            password="4PraeToriaN4",
            host="localhost",
            port="5432")
 
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM users_score")
        rec = cur.fetchall()
    print('\n')
    for row in rec:
        print("ID ",row[0])
        print("USER ",row[1])
        print("SCORE ",row[2])
        print("LEVEL ",row[3])
    print('\n')
def print_users():
    connection = psycopg2.connect(    
            database="snakescore",
            user="postgres",
            password="aral2196",
            host="localhost",
            port="5432")
 
    with connection:
        cur = connection.cursor()
        cur.execute("SELECT * FROM users")
        rec1 = cur.fetchall()
    print('\n')
    for row in rec1:
        print("id ",row[0])
        print("user ",row[1])
    print('\n')
def upd_usrscre(user, score, level):##
    try:
        connection = psycopg2.connect(    
            database="snakescore",
            user="postgres",
            password="aral2196",
            host="localhost",
            port="5432")

        cursor = connection.cursor()
 
        Uts = """ INSERT INTO users_score (username, score, level) VALUES (%s,%s,%s) """
        Ut = """ INSERT INTO users (username) VALUES (%s) """
        cursor.execute(Uts,(user, score, level))
        cursor.execute(Ut,(user,))
        connection.commit()
       

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
pygame.init() # инициализация библиотеки pygame 

tim = 0
#scorel = []
#lscorel = []
eatf = pygame.mixer.Sound('C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B031167\\tsis8\\1\\11.wav')#loading sound
WIDTH, HEIGHT = 800, 800 # начальные данные
RED = (255, 0, 0) # цвета
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (30,30,30)
BLOCK_SIZE = 80 # размер блока , пикселя
WHITE = (255, 255, 255)
RGR = (50,200,10)
maxl = WIDTH // BLOCK_SIZE
clock = pygame.time.Clock() # создание зарержки в игре те времени
my_font = pygame.font.SysFont('Comic Sans MS', 30) # для текста
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))#screen setting
text_new = my_font.render('New Game', False, (0, 255, 0))
text_table = my_font.render('Tables', False, (250, 255, 0))
nor = 0.8
def dot(a,b):#dot product
    return a[0]*b[0]+a[1]*b[0]
def lerp(a,b,t):#linearization
    return a + (b - a) * t
def qqurve(t):
    return  t * (t * (t * 6 - 15) + 10)
def noise(x,y,x1,y1,x2,y2,x3,y3,x4,y4,p1,p2,p3,p4):#Pearl noise
    t1 = dot((x1-x,y1-y),p1)
    t2 = dot((x2-x,y2-y),p2)
    t3 = dot((x3-x,y3-y),p3)
    t4 = dot((x4-x,y4-y),p4)
    qx = qqurve(x)
    qy = qqurve(y)
    ty1 = lerp(t1,t2,qx)#
    ty2 = lerp(t3,t4,qx)
    tr = lerp(ty1,ty2,qy)
    return(tr)
class PerlMap:
    def __init__(self, x, y):
        self.location = Point(x, y)
        self.map = deque([], maxlen=(WIDTH//BLOCK_SIZE)*(HEIGHT//BLOCK_SIZE))
        self.clearmap = deque([], maxlen=(WIDTH//BLOCK_SIZE)*(HEIGHT//BLOCK_SIZE))
        xminf = WIDTH//(4*BLOCK_SIZE)
        yminf = HEIGHT//(4*BLOCK_SIZE)
        for h in range(4):
            for n in range(4):   
                p1 = random.choice(((-1,0),(0,1),(1,0),(0,-1)))
                p2 = random.choice(((-1,0),(0,1),(1,0),(0,-1)))
                p3 = random.choice(((-1,0),(0,1),(1,0),(0,-1)))
                p4 = random.choice(((-1,0),(0,1),(1,0),(0,-1)))
                for i in range(h*xminf,(h+1)*xminf):
                    for j in range(n*yminf,(n+1)*yminf):
                        a= h*xminf , n*yminf   #i
                        b= (h+1)*xminf , n*yminf  #i+1
                        c= (h+1)*xminf , (n+1)*yminf #i+5
                        d= h*xminf  , (n+1)*yminf  #i+4  

                        weight = noise(i,j,a[0],a[1],b[0],b[1],c[0],c[1],d[0],d[1],p1,p2,p3,p4) /100
                        if weight > nor*100:
                            self.map.append(((i,j),1))   
                        else:
                            self.map.append(((i,j),0)) 
                            self.clearmap.append((i,j)) 
    
    def draw(self):
        for i in range(len(self.map)):
            k = 0
            if self.map[i][1] == 1:
                k = 5
            elif self.map[i][1] == 0:
                k = 0
            pygame.draw.rect(
                SCREEN,
                (50*k,50*k,50*k),
                pygame.Rect(
                    self.map[i][0][0] * BLOCK_SIZE,
                    self.map[i][0][1] * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )
    def checksnake(self,x,y):
        for i in self.map:
            if i[1] == 1:
                if i[0][0] == x and i[0][1] == y:
                    return True
    
    def relocate(self):
        pass
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Snake:#Snake class
    def __init__(self):
        
        self.body = [# snakes start body
            Point(
                x=WIDTH // BLOCK_SIZE // 2,#head
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]
    def draw(self):#draw method of snake

        head = self.body[0]
        pygame.draw.rect(#drawing head, draw rectangle on screen that sized with BLOCK_SIZE that in data
            SCREEN,
            RGR,#dark Green head
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:#drawing tail ,all body objects without head on screen with same method as we draw head but in for loop of body 
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )
    def move(self, dx, dy):# hit):#move method of snake
        if not (dx == 0 and dy == 0):#not hit:
            for idx in range(len(self.body) - 1, 0, -1): #moving snake from the last part of body(not head)
                self.body[idx].x = self.body[idx - 1].x 
                self.body[idx].y = self.body[idx - 1].y
         
        self.body[0].x += dx#moving head
        self.body[0].y += dy
        #teleport snake to other side when it crossing border
        if self.body[0].x >= WIDTH // BLOCK_SIZE:
            self.body[0].x = 0 
       
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        
        elif self.body[0].y >= HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0 
    def check_collision(self, food):#function of checking collision with food
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    def schecksnake(self,x,y):
        for i in self.body:
            if i.x == x and i.y == y:
                return True
    def check_selfcol(self):#function of checking collision with self body
        for i in range(len(self.body) - 1, 1, -1):
            if self.body[i].x == self.body[0].x and self.body[i].y == self.body[0].y:
                return True
        return False
    def relocate(self,mapp):
        fx,fy = random.choice(mapp.clearmap)
        self.body = [
            Point(
            x = fx,
            y = fy
            #x=random.randint(0, WIDTH // BLOCK_SIZE - 1),#head
            #y=random.randint(0, HEIGHT // BLOCK_SIZE - 1),
            )
            ,
            Point(
                x=self.body[0].x + 1,
                y=self.body[0].y,
            ),
        ]          
def draw_grid():#function of gird drawing on screen with white lines that drawn multiple times with for loop ,that will make gird with block size BLOCK_SIZE
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

class Food:#food class
    def __init__(self, x, y):
        self.location = Point(x, y)
        self.weight = 1
        self.rect = pygame.Rect(self.location.x,self.location.y,1,1)
    def draw(self):#draw method of food
        pygame.draw.rect(#drawing green rect on screen with block size
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
    def relocate(self,mapp):#relocate that will respawn food to other random position in screen with random weight , that also used to avoid food spawn on snake body
        self.weight = random.randint(1, 10)
        self.location.x,self.location.y = random.choice(mapp.clearmap)   
         
class Button:
    def __init__(self,x,y,wid,hei,col,text):
        self.x = x
        self.y = y
        self.color = col
        self.wid = wid
        self.hei = hei
        self.text = text
        self.rect = pygame.Rect(self.x,self.y,self.wid,self.hei)# need to chec collision with cursor
    def draw(self):
        SCREEN.blit(self.text, (self.x,self.y))
def main(): 
    nwgb = Button(WIDTH//2 -100,HEIGHT//2,300,50,(0,255,0),text_new)
    tblb = Button(WIDTH//2 -100,HEIGHT//2+ 300,300,50,(255,255,0),text_table)   
    mapp = PerlMap(5,5)
    running = True #running flag
    #start = False
    snake = Snake()  # создание змеи
    food = Food(5, 5)  # создание еды
    dx, dy = 0, 0;T = 3 # начальные данные в игре
    score = 0 ;level = 0
    over = 0 ;new = 0;table = 0# gameover flag and New game button flag
    dt = clock.tick();t = 0; #food timer 
    dafk = clock.tick();afk = 0;
    dl = 1
    while running:#game loop
        
        if T > 15:
            T = 15
        if mapp.checksnake(snake.body[0].x,snake.body[0].y - 1):
            if dy == -1 :
                dy = 0
        if mapp.checksnake(snake.body[0].x,snake.body[0].y + 1):
            if dy == 1 :
                dy = 0
        if mapp.checksnake(snake.body[0].x + 1,snake.body[0].y):
            if dx == 1 :
                dx = 0
        if mapp.checksnake(snake.body[0].x - 1,snake.body[0].y):
            if dx == -1 :
                dx = 0
        SCREEN.fill(BLACK)
        #mouse = pygame.mouse.get_pos()#
        for i in snake.body:#if food spawned on snake respawn it
            if i.x == food.location.x and i.y == food.location.y:
                food.relocate(mapp)
        for i in snake.body:#if food spawned on snake respawn it
            if i.x == food.location.x and i.y == food.location.y:
                snake.relocate(mapp)
        for j in mapp.map: 
            if j[1] == 1:
                if j[0][0] == food.location.x and j[0][1] == food.location.y:
                    food.relocate(mapp)
                if j[0][0] == snake.body[0].x and j[0][1] == snake.body[0].y:
                    snake.relocate(mapp)
        for event in pygame.event.get(): # обработка событии
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and over == 1:#NEW Game button check
                if tblb.rect.collidepoint(event.pos):
                    table = 1
                if nwgb.rect.collidepoint(event.pos):
                    new = 1
            if event.type == pygame.KEYDOWN:  # изменение скорости при нажатии на кнопки +
                if event.key == pygame.K_SPACE:
                    pause(user,score,level)
                if event.key == pygame.K_UP and dy == 0:
                    if mapp.checksnake(snake.body[0].x,snake.body[0].y - 1) :#or snake.schecksnake(snake.body[0].x,snake.body[0].y - 1):
                        if dy == -1 :
                            dy = 0
                    else:
                        dy = -1
                        dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    if mapp.checksnake(snake.body[0].x,snake.body[0].y + 1) :#or snake.schecksnake(snake.body[0].x,snake.body[0].y + 1):
                        if dy == 1 :
                            dy = 0
                    else:
                        dy = 1
                        dx = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    if mapp.checksnake(snake.body[0].x + 1,snake.body[0].y) :#or snake.schecksnake(snake.body[0].x + 1,snake.body[0].y):
                        if dx == 1 :
                            dx = 0
                    else:
                        dx = 1
                        dy = 0 
                elif event.key == pygame.K_LEFT  and dx == 0:
                    if mapp.checksnake(snake.body[0].x - 1,snake.body[0].y) :#or snake.schecksnake(snake.body[0].x - 1,snake.body[0].y):
                        if dx == -1 :
                            dx = 0
                    else:
                        dx = -1
                        dy = 0
        
        if over == 0:  
            t += dt#time running
            if t >= 10000:
                food.relocate(mapp)#перемещаем еду если время прошло
                t = 0 #обнуляем таймер
        if new == 1:#if button NEW GAME clicked reset game data to start
            dx, dy = 0, 0;T = 1
            score = 0;level = 0
            dl = 1
            t = 0; 
            snake.body.clear()
            snake.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            ]
            over = 0#startting new game
        if over == 0: #if game is not over
            if dx == 0 and dy == 0:
                afk += dafk#time running
                if afk >= 40000:
                    afk = 0 
                    over = 1
            tim = 0
            new = 0
            table = 0
            snake.move(dx, dy)  # вызов функции движения змеи
            if snake.check_collision(food):  # функция столкновения с едой
                pygame.mixer.Sound.play(eatf)#play sound when food collided with snake 
                score += food.weight 
                level = score//3
                if level>(score-food.weight)//3:#if level increased increase speed of snake and length of snake
                    dl = int(level-((score-food.weight)//3))
                    T += 1*dl#increasing speed of snake(game)
                    for i in range(dl):
                        if len(snake.body)<maxl - 2: #max length of snake limited by maxl
                            snake.body.append(      
                            Point(snake.body[-1].x, snake.body[-1].y)  # удлиннение змеи 
                            ) 
                            
                food.relocate(mapp)#food respawn if it collided with snake
                t = 0 #restart timer
            if snake.check_selfcol():  
                over = 1
            mapp.draw()
            draw_grid()
            snake.draw()# вывод функции для отрисовки змеи
            food.draw() # вывод функции для отрисовки еды
            text_score = my_font.render('Score :'+str(score), False, (0, 255, 0))
            SCREEN.blit(text_score, (20,20)) #вывод на экран очков
            text_level = my_font.render('Level :'+str(level), False, (0, 255, 0))
            SCREEN.blit(text_level, (WIDTH - 300,20))# вывод на экран уровня     
        elif over == 1:
            nwgb.draw()
            tblb.draw()
            tim += 1
            if tim == 1:
                
                
                upd_usrscre(user, score, level)
                """with open("C:\\Users\\User\\Desktop\\Программирование\\my\\pp2-22B031167\\tsis10\\rez.txt","a") as f: #"w+") as f:
                    f.write("S")
                    f.write("\n")
                    for i in range(len(lscorel)-1):
                        f.write(str(lscorel[i]) + " ")
                    f.write("\n")"""
            text_over = my_font.render('Game Over', False, (250, 0, 0))
            SCREEN.blit(text_over, (WIDTH//2 -100,HEIGHT//2 -100)) 
            if table == 1:
                print_table_userscores()
                print_users()
                table = 0
        pygame.display.flip() 
        clock.tick(T)  
        
if __name__ == '__main__': 
    print_table_userscores()
    print_users()
    main()
    
        