import pygame
import random
import time


pygame.init()


width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')


white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


clock = pygame.time.Clock()
snake_block = 10
snake_speed = 5  #начальная скорость змейки
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

#счет и уровень на экране
def score_level(score, level):
    value = score_font.render("Score: " + str(score) + " Level: " + str(level), True, black)
    screen.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

#еда
class Food:
    def __init__(self):
        self.x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        self.weight = random.randint(1, 3)  #случайный вес еды
        self.time_limit = time.time() + random.randint(5, 10)  #таймер для исчезновения еды 

    
    def is_expired(self):
        return time.time() > self.time_limit


def gameLoop():
    game_over = False
    game_close = False

    #координаты змейки
    x1 = width / 2
    y1 = height / 2

    
    x1_change = 0
    y1_change = 0

    snake_List = []  
    Length_of_snake = 1  #начальная длина змейки

    score = 0
    level = 1

    global snake_speed

    
    food = Food()

    while not game_over:

        while game_close:
            screen.fill(blue)
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

        #выход за пределы экрана
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)

        
        if not food.is_expired():  
            pygame.draw.rect(screen, black, [food.x, food.y, snake_block, snake_block])
        else:
            food = Food()  #если еда исчезла, делаем новую

        #отрисовка змейки
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

        #столкновение с едой
        if x1 == food.x and y1 == food.y:
            food = Food()  #генерация новой еды
            Length_of_snake += 1  #увеличение длины нашей змейки
            score += food.weight * 10  #очки в зависимости от веса еды

            if score % 40 == 0:  #увеличиваем уровень после каждых 40 оч
                level += 1
                snake_speed += 2  #увеличиваем скорость 
                print(f"Level {level} reached!")

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
