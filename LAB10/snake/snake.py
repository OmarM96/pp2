import random, pygame, time, sys, os, platform
from tkinter import W
import psycopg2
from soupsieve import select
from config import host, user, password, db_name

def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""
░██████╗███╗░░██╗░█████╗░██╗░░██╗███████╗
██╔════╝████╗░██║██╔══██╗██║░██╔╝██╔════╝
╚█████╗░██╔██╗██║███████║█████═╝░█████╗░░
░╚═══██╗██║╚████║██╔══██║██╔═██╗░██╔══╝░░
██████╔╝██║░╚███║██║░░██║██║░╚██╗███████╗
╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝                                                                                                                            
         
""")   
banner()
def insert(NickName, Score, Level):
    NickName = NickName.strip()
    #print(PNumber)
    with conn.cursor() as cursor:
        try:
            cursor.execute(
            f"insert into SnakeBoard (nickname, score, level) values ('{NickName}','{Score}','{Level}')"
            )
            print ("[INFO] Insert was complete succesfully!")
        except Exception as ex:
            print(f"[INFO] Error, inserting is failed - {ex}")
def print_top():
    y = 170
    with conn.cursor() as cursor:
        cursor.execute(
            """
            select * from SnakeBoard
            order by score desc
            """
        )
        tmp = cursor.fetchall()
    tmp 
    for i,row in enumerate(tmp):
        if i == 5:
            break
        toptmp = pygame.font.SysFont("Verdana", 30).render(f"{i+1}. {row[0]} - {row[1]}", True, (255,255,255))
        screen.blit(toptmp, (130, y))
        y+=35

try:
    conn = psycopg2.connect(
        database=db_name, 
        user=user, 
        password=password, 
        host=host)   
    conn.autocommit = True #autocommit
    
    with conn.cursor() as cursor:
        cursor.execute(
            """
            create table SnakeBoard(
                NickName varchar(50) not null unique,
                score integer not null,
                level integer not null,
                primary key(NickName)
            )
            """
        )
    pygame.init()
    resolution = (500,500)
    screen = pygame.display.set_mode(resolution)
    gameover = pygame.font.SysFont("Verdana", 60).render("Game Over", True, (128, 128, 128))
    scoreadded = pygame.font.SysFont("Verdana", 20).render("Check you on scoreboard!", True, (128, 128, 128))

    def score_board():
        scores = pygame.font.SysFont("Verdana", 36).render("Score leaders:", True, (255,255,255))
        tab = pygame.font.SysFont("Verdana", 10).render("Press TAB to write a Nickname!", True, (255,255,255))
        print_top()        
        screen.blit(tab, (20,20))
        screen.blit(scores, (120,120))

    def print_nickname():
        nickname = pygame.font.SysFont("Verdana", 40).render(nickname_input, True, (255,255,255))
        screen.blit(nickname, (200, 350))

    def create_rect(width, height, border, color, border_color):
        surf = pygame.Surface((width+border*2, height+border*2), pygame.SRCALPHA)
        pygame.draw.rect(surf, color, (border, border, width, height), 0)
        for i in range(1, border):
            pygame.draw.rect(surf, border_color, (border-i, border-i, width+5, height+5), 1)
        return surf

    def game_over(NickName,score,level): # gameover of snake
        insert(NickName,score,level)
        screen.blit(gameover, (75, 190))
        screen.blit(scoreadded, (110,300))
        pygame.display.update()
        time.sleep(5)
        score_board()

    def game_end(): #exit from th game
        pygame.quit()
        sys.exit()
    class Snake:
        def __init__(self, x, y):
            self.score = 0
            self.is_alive = True
            self.level = 1
            self.size = 1
            self.food_size = 1
            self.elements = [[x, y]]  # [[x0, y0], [x1, y1], [x2, y2] ...] (i) -> (i - 1)
            self.radius = 10
            self.dx = 0  # Right/Left
            self.dy = 0  # Up/Down
            self.is_add = False
            self.speed = 30

        def draw(self):
            for element in self.elements:
                pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

        def add_to_snake(self,food_size=3):
            self.size += food_size
            for element in range(food_size):
                self.elements.append([0, 0])
            self.is_add = False
            if self.size % 5 == 0:
                self.speed += 10
        def walls(self):
            if self.level>1:
                return True

        def move(self, nickname):
            if self.is_add:
                self.add_to_snake(self.food_size)

            for i in range(self.size - 1, 0, -1):
                self.elements[i][0] = self.elements[i - 1][0]
                self.elements[i][1] = self.elements[i - 1][1]

            #to avoid to going out for infinity
            if self.level>1:
                if self.elements[0][0] >= 70 and self.elements[0][0] <= 170 and self.elements[0][1] >= 70 and self.elements[0][1] <= 170:
                    self.is_alive = False
                    game_over(nickname,self.score,self.level)            
                elif self.elements[0][0] >= 250 and self.elements[0][0] <= 350 and self.elements[0][1] >= 250 and self.elements[0][1] <= 350:
                    self.is_alive=False
                    game_over(nickname,self.score,self.level)            
            if (self.elements[0][0] == 20):
                self.is_alive=False
                game_over(nickname,self.score,self.level)            
            if (self.elements[0][0] == resolution[0]-20):
                self.is_alive=False
                game_over(nickname,self.score,self.level)            
            if (self.elements[0][1] == 20):
                self.is_alive=False
                game_over(nickname,self.score,self.level)            
            if(self.elements[0][1] == resolution[1]-20):
                self.is_alive=False
                game_over(nickname,self.score,self.level)            
            self.elements[0][0] += self.dx
            self.elements[0][1] += self.dy
            #print(self.elements[0])

        def eat(self, foodx, foody):
            x = self.elements[0][0]
            y = self.elements[0][1]
            if foodx-20 <= x <= foodx + 20 and foody-20 <= y <= foody + 20:
                return True
            return False
        

    border_res = (20,480)
    class Food:
        def __init__(self, food_size,is_exist=True,level=1):
            self.is_exist = is_exist
            self.food_size = food_size
            self.level = level
            self.x = random.randint(border_res[0],border_res[1])
            self.y = random.randint(border_res[0],border_res[1])

        def gen(self, score, elements):    
            self.x = random.randint(border_res[0],border_res[1])
            self.y = random.randint(border_res[0],border_res[1])
            
            for i in elements:
                if self.x == i[0] and self.y == i[1]:
                    print("It is work!")
                    self.x = random.randint(border_res[0],border_res[1])
                    self.y = random.randint(border_res[0],border_res[1])

            if score>22: #level 2 walls collision
                while (((self.x >= 60 and self.x <= 180 and self.y >= 60 and self.y <= 180) or (self.x >= 240 and self.x <= 360 and self.y >= 240 and self.y <= 360))):
                    self.x = random.randint(border_res[0],border_res[1])
                    self.y = random.randint(border_res[0],border_res[1])

        def draw(self):
            pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10+self.food_size, 10 + self.food_size))


    border = create_rect(485, 485, 10, (0, 0, 0),(255, 255, 255))
    snake1 = Snake(250, 250)
    food = Food(3)
    bonus = Food(7,False)

    #Good flow
    snake_frame_speed = 5
    FPS = 120

    d = 5

    clock = pygame.time.Clock()

    spawn_status = True

    spawn_bonus = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_bonus, 10000)

    start_pos = 250
    snake = [(start_pos,start_pos)]

    def scoreboard():
        global nickname_input
        running = True
        frame_counter = 0
        leaders = None
        with conn.cursor() as cursor:
            cursor.execute(
                """
                select * from SnakeBoard
                order by score
                """
            )
            leaders = cursor.fetchall()
        #print (leaders)
        time.sleep(2)
        need_input = False
        nickname_input = ""

        while running:
            frame_counter+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_end()
                if event.type == pygame.KEYDOWN and need_input:
                    if event.key == pygame.K_RETURN:
                        game(nickname_input)
                        nickname_input = ""
                    elif event.key == pygame.K_BACKSPACE:
                        nickname_input = nickname_input[:len(nickname_input)-1]
                    else:
                        if len(nickname_input)<10:
                            nickname_input += event.unicode
                    

            keys = pygame.key.get_pressed()

            if keys[pygame.K_TAB]:
                need_input = True
            #if len(snake1.elements)
            if frame_counter:
                screen.fill((0, 0, 0))
                screen.blit(border,(0,0))
                score_board()
                print_nickname()
                
            clock.tick(FPS)
            pygame.display.flip()
            
            
            
                
    def game(nickname):
        running = True
        frame_counter = 0
        while running:
            frame_counter+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_end()
                if event.type == spawn_bonus:
                    if bonus.is_exist:
                        bonus.is_exist = False
                    elif bonus.is_exist == False:
                        bonus.gen(snake1.level,snake1.elements)
                        bonus.is_exist=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    #if event.key == pygame.K_SPACE:
                    #     snake1.is_add = True
                    #     snake2.is_add = True
                    if event.key == pygame.K_RIGHT and snake1.dx != -d:
                        snake1.dx = d
                        snake1.dy = 0
                    if event.key == pygame.K_LEFT and snake1.dx != d:
                        snake1.dx = -d
                        snake1.dy = 0
                    if event.key == pygame.K_UP and snake1.dy != d:
                        snake1.dx = 0
                        snake1.dy = -d
                    if event.key == pygame.K_DOWN and snake1.dy != -d:
                        snake1.dx = 0
                        snake1.dy = d
            
            
            #if len(snake1.elements)
            if frame_counter:
                if snake1.eat(food.x, food.y):
                    snake1.is_add = True
                    snake1.food_size = food.food_size
                    snake1.score+=food.food_size
                    food.gen(snake1.score,snake1.elements)
                if snake1.eat(bonus.x, bonus.y):
                    snake1.is_add = True
                    snake1.food_size = bonus.food_size
                    bonus.is_exist = False
                    snake1.score+=bonus.food_size
                    bonus.gen(snake1.score,snake1.elements)
            if frame_counter%snake_frame_speed==0:
                if snake1.score > 30 and snake1.level == 1:
                    snake1.level +=1
                #print(snake1.size)
                screen.fill((0, 0, 0))
                screen.blit(border,(0,0))
                if (snake1.walls()):
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(70, 70, 100, 100)) # 70 - 170
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(250, 250, 100, 100)) #250 - 350
                snake1.move(nickname)    
                snake1.draw()
                food.draw()
                scores = pygame.font.SysFont("Verdana", 12).render("Score: "+str(snake1.score), True, (255,255,255))
                levels = pygame.font.SysFont("Verdana", 12).render("Level: "+str(snake1.level), True, (255,255,255))
                screen.blit(scores,(20,20))
                screen.blit(levels,(20,40))
                if bonus.is_exist:
                    bonus.draw()
                running = snake1.is_alive
                
            clock.tick(FPS)
            pygame.display.flip()


    def main():
        scoreboard()


    try:
        # Your try block code here
        # ...

        if __name__ == "__main__":
            main()

    except Exception as ex:
        print(f"An error occurred: {ex}")
