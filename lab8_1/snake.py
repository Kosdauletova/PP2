import pygame
import random
import time


pygame.init()

#установка начальных настроек
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# установка цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
tan = (210, 180, 140)

#контрим частоту кадров 
clock = pygame.time.Clock()
snake_block = 10 #размер блока змейки
snake_speed = 10  #скорость змеи
font_style = pygame.font.SysFont("bahnschrift", 25) #стиль шрифта
score_font = pygame.font.SysFont("comicsansms", 35) 

#Эта функция отображает текст на экране. Она используется для вывода сообщения о проигрыше.
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

#Отображает текущий счет и уровень на экране.
def score_level(score, level):
    value = score_font.render("Score: " + str(score) + " Level: " + str(level), True, black)
    screen.blit(value, [0, 0])

#Отображает змею. Она рисует прямоугольники для каждого блока змеи.
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_over = False
    game_close = False

# Начальная позиция змейки
    x1 = width / 2
    y1 = height / 2

# Начальные изменения позиции
    x1_change = 0
    y1_change = 0

    snake_List = [] #список, который хранит все сегменты змеи
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0 #координаты пищи
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    score = 0 #отслеживаем счет и уровень
    level = 1

    global snake_speed

    while not game_over: #пока ты не проиграл

        while game_close: #если проигрыш
            screen.fill(tan)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score_level(score, level)
            pygame.display.update()

            #Обработка событий после проигрыша
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: #выход из игры
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: #перезапуск
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #если закроют окно
                game_over = True
            if event.type == pygame.KEYDOWN:
                #управление змейкой
                if event.key == pygame.K_LEFT: #налево
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: #направо
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP: #вверх
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN: #вниз
                    y1_change = snake_block
                    x1_change = 0

        #Проверка на столкновение с границей экрана
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change #Обновление позиции головы змейки
        y1 += y1_change
        screen.fill(tan)
        pygame.draw.rect(screen, black, [foodx, foody, snake_block, snake_block])
        snake_Head = [] #Формируем новый элемент головы змейки и добавляем в список змейки
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        #Проверка на столкновение с телом змейки
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        #Отображаем змейку и текущий счет с уровнем
        our_snake(snake_block, snake_List)
        score_level(score, level)

        pygame.display.update()

         #Если змея съела еду
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 10

            #Если счет делится на 40, увеличиваем уровень и скорость змейки
            if score % 40 == 0:  
                level += 1
                snake_speed += 2  
                print(f"Level {level} reached!")
                
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
