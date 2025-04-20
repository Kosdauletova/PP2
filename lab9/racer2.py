import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

#настройки фрэймов
FPS = 60
clock = pygame.time.Clock()

#цвета
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#настройки окна
W, H = 400, 600
SPEED = 5               
SCORE = 0              
COINS = 0              
SPEED_INCREASE_THRESHOLD = 5  

#Game Over text
font = pygame.font.Font("font_user.ttf", 60)
font_small = pygame.font.Font("font_user.ttf", 20)
game_over = font.render("Game Over", True, BLACK)

#загрузка изображения монеток
coin_icon = pygame.image.load("im/Coin.png")
coin_icon = pygame.transform.scale(coin_icon, (coin_icon.get_width() // 15, coin_icon.get_height() // 10))

#фон
bg = pygame.image.load("im/AnimatedStreet.png")

#игровое окно
SC = pygame.display.set_mode((W, H))
pygame.display.set_caption("My game")


#враг
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("im/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > H:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

#игрок
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("im/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 1 and pressed_key[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < W and pressed_key[K_RIGHT]:
            self.rect.move_ip(5, 0)

#монеточки
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("im/Coin.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 12, self.image.get_height() // 12))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)
        self.value = random.choice([1, 2, 3])  #рандомный вес

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > H:
            self.reset_position()

    def reset_position(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, W - 40), 0)
        self.value = random.choice([1, 2, 3])  
        


P1 = Player()
E1 = Enemy()

#группы
enemies = pygame.sprite.Group(E1)
coins_group = pygame.sprite.Group()
for _ in range(3):  #спавн монеточек
    coins_group.add(Coin())

all_sprites = pygame.sprite.Group(P1, E1, *coins_group)

#увеличивать скорость
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 4000)


# MAIN GAME LOOP


while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #рисуем фон и счетчик монет
    SC.blit(bg, (0, 0))
    SC.blit(coin_icon, (10, 35))
    coins_v = font_small.render(f"X{str(COINS)}", True, BLACK)
    SC.blit(coins_v, (50, 50))

    #рисуем спрайты
    for entity in all_sprites:
        SC.blit(entity.image, entity.rect)
        entity.move()

    #чекинг столкновения с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('im/crash.wav').play()
        time.sleep(0.5)

        SC.fill(RED)
        SC.blit(game_over, (30, 250))
        result = font_small.render(f"Your result: {COINS}", True, BLACK)
        SC.blit(result, (120, 350))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()


#чекинг столкновения с монетами
    collected = pygame.sprite.spritecollide(P1, coins_group, dokill=False)
    for coin in collected:
        COINS += coin.value  
        coin.reset_position()

        #увеличивать скорость после каких то коинов
        if COINS % SPEED_INCREASE_THRESHOLD == 0:
            SPEED += 2


    pygame.display.update()
    clock.tick(FPS)