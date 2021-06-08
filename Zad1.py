import pygame, sys, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*PIXEL_SIZE)
            y_pos = int(block.y*PIXEL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, PIXEL_SIZE, PIXEL_SIZE)
            pygame.draw.rect(screen, (255, 0, 0), block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*PIXEL_SIZE), int(self.pos.y*PIXEL_SIZE), PIXEL_SIZE, PIXEL_SIZE)
        pygame.draw.rect(screen, (0, 0, 255), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, PIXEL_NUMBER - 1)
        self.y = random.randint(0, PIXEL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < PIXEL_NUMBER or not 0 <= self.snake.body[0].y < PIXEL_NUMBER:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        game_intro()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        spos_x = int(PIXEL_SIZE * PIXEL_NUMBER - 100)
        spos_y = int(PIXEL_SIZE * PIXEL_NUMBER - 100)
        score_rect = score_surface.get_rect(center=(spos_x, spos_y))
        screen.blit(score_surface, score_rect)


class Button:
    def __init__(self, color,x ,y, width, height, text: str):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw_text(self, screen, outline=None):
        pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4,self.height+4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        text = game_font.render(self.text, True, (0,0,0))
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isover(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos [1] < self.y + self.height:
                return True
        return False


class text:
    pass

pygame.init()
PIXEL_SIZE = 40
PIXEL_NUMBER = 20
SCREEN_WIDTH =PIXEL_SIZE*PIXEL_NUMBER
SCREEN_HEIGHT = PIXEL_SIZE*PIXEL_NUMBER
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
game_font = pygame.font.Font("font/kungfumaster.ttf", 25)
display = pygame.Surface((SCREEN_SIZE))
music = pygame.mixer.music.load("music/Electronic_Fantasy.ogg")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
click = False

btnstart = Button((255, 255, 255), 200, 150, 400, 100, "Start")
btnquit = Button((255,255,255), 200, 600, 400, 100, "exit")
btnrules = Button((255,255,255), 200, 300, 400, 100, "Rules")
btnback = Button((255,255,255), 200, 600, 400, 100, "Back")
btnhighscores = Button((255,255,255), 200, 450, 400, 100, "Highscores")

def redraw():
    screen.fill((0,0,0))
    btnstart.draw_text(screen, (255,0,0))
    btnquit.draw_text(screen, (255,0,0))
    btnrules.draw_text(screen, (255,0,0))
    btnhighscores.draw_text(screen, (255,0,0))


def redraw2():
    screen.fill((0,0,0))
    btnback.draw_text(screen, (255,0,0))


def redraw3():
    screen.fill((0,0,0))
    btnback.draw_text(screen, (255,0,0))

def game_intro():
    intro = True
    while intro:
        redraw()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnstart.isover(pos):
                    game_loop()
                if btnquit.isover(pos):
                    exit()
                if btnrules.isover(pos):
                    rules()
                if btnhighscores.isover(pos):
                    highscores()


        pygame.display.update()
        clock.tick(60)
        screen.fill((0,0,0))


def exit():
    pygame.quit()
    sys.exit()


def rules():
    rule = True
    while rule:
        redraw2()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnback.isover(pos):
                    game_intro()

        pygame.display.update()
        clock.tick(60)
        screen.fill((0,0,0))


def highscores():
    score = True
    while score:
        redraw3()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnback.isover(pos):
                    game_intro()

        pygame.display.update()
        clock.tick(60)
        screen.fill((0, 0, 0))


def game_loop():
    main_game = MAIN()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill((255,144,255))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)

game_intro()
