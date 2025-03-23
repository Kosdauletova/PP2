import pygame


pygame.init()


WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Движущийся шар")

# Цвет
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Начальная позиция circle
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_radius = 25  # радиус мяча

# Скорость мячика
move_distance = 20


running = True
while running:
    screen.fill(WHITE)  # Очистка экрана (белый фон)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    
    # Двигаем мяч в зависимости от нажатой клавиши
    if keys[pygame.K_UP] and ball_y - ball_radius - move_distance >= 0:
        ball_y -= move_distance  # Двигаем вверх
    if keys[pygame.K_DOWN] and ball_y + ball_radius + move_distance <= HEIGHT:
        ball_y += move_distance  # Двигаем вниз
    if keys[pygame.K_LEFT] and ball_x - ball_radius - move_distance >= 0:
        ball_x -= move_distance  # Двигаем влево
    if keys[pygame.K_RIGHT] and ball_x + ball_radius + move_distance <= WIDTH:
        ball_x += move_distance  # Двигаем вправо

    # Рисуем мяч
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    # Обновляем экран
    pygame.display.update()

# Закрытие Pygame
pygame.quit()
