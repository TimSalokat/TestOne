import pygame, sys

pygame.init()

size = window_width, window_height = 1200, 600
FPS = 20
black = (0,0,0)
green = (0, 255, 0)

ADD_NEW_FLAME_RATE = 25
cactus_img = pygame.image.load("TestMarioGame/sprites/cactus_bricks.png")
cactus_img_rect = cactus_img.get_rect()
cactus_img_rect.left = 0

fire_img = pygame.image.load("TestMarioGame/sprites/fire_bricks.png")
fire_img_rect = fire_img.get_rect()
fire_img_rect.left = 0

CLOCK = pygame.time.Clock()
font = pygame.font.SysFont("forte", 20)

canvas = pygame.display.set_mode(size)
pygame.display.set_caption("Mario Game")

class Topscore:
    def __init__(self):
        self.highscore = 0
    def top_score(self, score):
        if score > self.highscore:
            self.highscore = score
        return self.highscore

topscore = Topscore()

class Dragon:
    dragon_velocity = 10

    def __init__(self):
        self.dragon_img = pygame.image.load("TestMarioGame/sprites/dragon.png")
        self.dragon_img_rect = self.dragon_img.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = int(window_height/2)
        self.dragon_img_rect.right = window_width
        self.up = True
        self.down = False
    def update(self):
        canvas.blit(self.dragon_img, self.dragon_img_rect)
        if self.dragon_img_rect.top <= cactus_img_rect.bottom:
            self.up = False
            self.down = True
        elif self.dragon_img_rect.bottom >= fire_img_rect.top:
            self.top = True
            self.down = False
        
        if self.up:
            self.dragon_img_rect.top -= self.dragon_velocity
        elif self.down:
            self.dragon_img_rect.top += self.dragon_velocity

class Flames:
    flames_velocity = 20

    def __init__(self):
        self.flames = pygame.image.load("TestMarioGame/sprites/fireball.png")
        self.flames_img = pygame.transform.scale(self.flames, (20,20))
        self.flames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right = Dragon.dragon_img_rect.left
        self.flames_img_rect.top = Dragon.dragon_img_rect.top + 30

    def update(self):
        canvas.blit(self.flames_img, self.flames_img_rect)

        if self.flames_img_rect.left > 0:
            self.flames_img_rect.left -= self.flames_velocity

class Mario:
    velocity = 10
    def __init__(self):
        self.mario_img = pygame.image.load("TestMarioGame/sprites/mario.png")
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = int(window_height/2 -100)
        self.down = True
        self.up = False

    def update(self):
        canvas.blit(self.mario_img, self.mario_img_rect)
        if self.mario_img_rect.top <= cactus_img_rect.bottom:
            gameover()
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.mario_img_rect.bottom >= fire_img_rect.top:
            gameover()
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.up:
            self.mario_img_rect.top -= 10
        if self.down:
            self.mario_img_rect.bottom += 10

def gameover():
    topscore.top_score(SCORE)
    game_over_img = pygame.image.load("TestMarioGame/sprites/end.png")
    gameover_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (int(window_width/2), int(window_height/2))
    canvas.blit(game_over_img, gameover_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()

def start_game():
    canvas.fill(black)
    start_img = pygame.image.load("TestMarioGame/sprites/start.png")
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (int(window_width/2), int(window_height/2))
    canvas.blit(start_img, start_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()

def check_level(SCORE):
    global LEVEL
    if score in range (0, 10):
        cactus_img_rect.bottom = 50
        fire_img_rect.top = window_height -50
        LEVEL = 1
    elif SCORE in range (10, 20):
        cactus_img_rect.bottom = 100
        fire_img_rect.top = window_height -100
        LEVEL = 2
    elif SCORE in range(20, 30):
        cactus_img_rect.bottom = 150
        fire_img_rect.top = window_height -150
        LEVEL = 3
    elif SCORE in range(30, 40):
        cactus_img_rect.bottom = 200
        fire_img_rect.top = window_height -200
        LEVEL = 4
    
def game_loop():
    while True:
        global dragon
        dragon = Dragon
        dragon = Dragon()
        flames = Flames()
        mario = Mario()

        add_new_flame_counter = 0
        global SCORE
        SCORE = 0
        global HIGH_SCORE
        flames_list = []
        while True:
            canvas.fill(black)
            check_level(SCORE)
            dragon.update()
            add_new_flame_counter += 1

            if add_new_flame_counter == ADD_NEW_FLAME_RATE:
                add_new_flame_counter = 0
                new_flame = Flames()
                flames_list.append(new_flame)
            for f in flame_list:
                if f.flames_img_rect.left <= 0:
                    flames.list.remove(f)
                    SCORE += 1
                f.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mario.up = True
                        mario.down = False
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        mario.up = False
                        mario.down = True
                    elif event.key == pygame.K_DOWN:
                        mario.down = False
                        mario.up = True
            
            score_font = font.render("Score:" + str(SCORE), True, green)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, cactus_img_rect.bottom + int(score_font_rect.height/2))
            canvas.blit(score_font, score_font_rect)

            level_font = font.render("Level:" + str(LEVEL), True, green)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, cactus_img.rect.bottom + int(score_font_rect.height/2))
            canvas.blit(level_font, level_font_rect)

            top_score_font = font.render("Top Score:", str(topscore.high_score), True, green)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (500, cactus_img_rect.bottom + int(score_font_rect.height/2))
            canvas.blit(top_score_font, top_score_font_rect)

            canvas.blit(cactus_img, cactus_img_rect)
            canvas.blit(fire_img, fire_img_rect)
            mario.update()
            for f in flames_list:
                if f.flames_img_rect.colliderect(mario.mario_img_rect):
                    game_over()
                    if SCORE > mario.mario_score:
                        mario.mario_score = SCORE
            pygame.display.update()
            CLOCK.tick(FPS)

start_game()