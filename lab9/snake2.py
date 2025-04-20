import pygame
import random
import time


pygame.init()

# Устанавливаем размеры экрана
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
tan = (210, 180, 140)
yellow = (255, 255, 0)
blue = (50, 153, 213)
purple = (128, 0, 128)

# Инициализация игры
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10  
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def score_level(score, level):
    value = score_font.render("Score: " + str(score) + " Level: " + str(level), True, black)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Класс для фруктов
class Fruit:
    def __init__(self, color, points, lifespan):
        self.color = color
        self.points = points
        self.lifespan = lifespan
        self.x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        self.creation_time = time.time()  # Запоминаем время создания фрукта

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, snake_block, snake_block])

    def is_expired(self):
        return time.time() - self.creation_time > self.lifespan

def gameLoop():
    game_over = False
    game_close = False

    # Инициализация змейки
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1

    score = 0
    level = 1

    global snake_speed

    fruits = []
    fruit_timer = 0

    while not game_over:
        while game_close:
            screen.fill(tan)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score_level(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(tan)

        # Генерация фруктов
        fruit_timer += 1
        if fruit_timer > 50:  # Каждые 50 кадров появляется новый фрукт
            fruit_timer = 0
            color = random.choice([red, yellow, blue, purple])
            points = random.choice([10, 20, 30])
            lifespan = random.choice([5, 8, 12])  # Время жизни фрукта в секундах
            fruits.append(Fruit(color, points, lifespan))

        # Отображаем все фрукты и проверяем их на истечение времени
        for fruit in fruits[:]:
            fruit.draw()
            if fruit.is_expired():  # Если фрукт "испорчен", удаляем его
                fruits.remove(fruit)

        # Рисуем змейку
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        score_level(score, level)

        pygame.display.update()

        # Проверка на столкновение с фруктами
        for fruit in fruits[:]:
            if x1 == fruit.x and y1 == fruit.y:
                fruits.remove(fruit)
                score += fruit.points
                Length_of_snake += 1
                if score % 40 == 0:  
                    level += 1
                    snake_speed += 2  
                    print(f"Level {level} reached!")
                
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
