import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racer Game")


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


clock = pygame.time.Clock()

class Racer:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height - 60
        self.width = 50
        self.height = 80
        self.speed = 5
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREEN)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.width:
            self.x += self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))



class Coin:
    def __init__(self):
        self.x = random.randint(0, screen_width - 30)
        self.y = random.randint(-100, -40)
        self.width = 30
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 223, 0))  # Yellow for coins

    def move(self):
        self.y += 5
        if self.y > screen_height:
            self.y = random.randint(-100, -40)
            self.x = random.randint(0, screen_width - self.width)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


def game_loop():
    racer = Racer()
    coins = [Coin() for _ in range(5)]  # Create a few coins
    collected_coins = 0
    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        racer.move(keys)
        racer.draw()

        
        for coin in coins:
            coin.move()
            coin.draw()

            
            if (racer.x < coin.x + coin.width and
                racer.x + racer.width > coin.x and
                racer.y < coin.y + coin.height and
                racer.y + racer.height > coin.y):
                coin.y = random.randint(-100, -40)  # Reset coin
                coin.x = random.randint(0, screen_width - coin.width)
                collected_coins += 1

        
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Coins: {collected_coins}", True, WHITE)
        screen.blit(score_text, (screen_width - 150, 20))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()

