import pygame
pygame.init()

#цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)
VIOLET = (238, 130, 238)
CYAN = (0, 255, 255)

#начальные настройки
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

#начало
game_over = False
prev, cur = None, None
screen.fill(WHITE)
current_color = PINK
mode = 'draw'

font = pygame.font.SysFont(None, 24)

#панель инструментов
def draw_toolbar():
    pygame.draw.rect(screen, BLACK, (0, 0, WINDOW_WIDTH, 80))  # Toolbar

    #иконки цветов
    colors = [PINK, VIOLET, CYAN, BLACK]
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i * 50, 5, 40, 30))

    #иконки фигурок 
    pygame.draw.rect(screen, WHITE, (210, 5, 40, 30))  # Eraser
    pygame.draw.rect(screen, WHITE, (260, 5, 40, 30))  # Rhombus
    pygame.draw.rect(screen, WHITE, (310, 5, 40, 30))  # Circle
    pygame.draw.rect(screen, WHITE, (360, 5, 40, 30))  # Square
    pygame.draw.rect(screen, WHITE, (410, 5, 40, 30))  # Right Triangle
    pygame.draw.rect(screen, WHITE, (460, 5, 40, 30))  # Equilateral Triangle

    #вывод на экран
    screen.blit(font.render("E", True, BLACK), (220, 10))  # Eraser
    screen.blit(font.render("R", True, BLACK), (270, 10))  # Rhombus
    screen.blit(font.render("C", True, BLACK), (320, 10))  # Circle
    screen.blit(font.render("S", True, BLACK), (370, 10))  # Square
    screen.blit(font.render("T", True, BLACK), (420, 10))  # Right Triangle
    screen.blit(font.render("Q", True, BLACK), (470, 10))  # Equilateral Triangle

#основа
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        #клики панели инстурментов
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y < 40:  #первая строка
                if 10 <= x < 50:
                    current_color, mode = PINK, 'draw'
                elif 60 <= x < 100:
                    current_color, mode = VIOLET, 'draw'
                elif 110 <= x < 150:
                    current_color, mode = CYAN, 'draw'
                elif 160 <= x < 200:
                    current_color, mode = BLACK, 'draw'
                elif 210 <= x < 250:
                    current_color, mode = WHITE, 'erase'
                elif 260 <= x < 300: 
                    mode = 'rhombus'
                elif 310 <= x < 350:
                    mode = 'circle'
                elif 360 <= x < 400:
                    mode = 'square'
                elif 410 <= x < 450:
                    mode = 'right_tri'
                elif 460 <= x < 500:
                    mode = 'eq_tri'
            else:
                prev = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if prev:
                cur = event.pos
                x1, y1 = prev
                x2, y2 = cur

                if mode == 'circle':
                    radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
                    pygame.draw.circle(screen, current_color, (x1, y1), radius, 1)

                elif mode == 'square':
                    size = min(abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(screen, current_color, (x1, y1, size, size), 1)

                elif mode == 'right_tri':
                    points = [(x1, y1), (x2, y2), (x1, y2)]
                    pygame.draw.polygon(screen, current_color, points, 1)

                elif mode == 'eq_tri':
                    side = abs(x2 - x1)
                    height = (3 ** 0.5 / 2) * side
                    if y2 < y1:
                        top = (x1 + side / 2, y1 - height)
                        left = (x1, y1)
                        right = (x1 + side, y1)
                    else:
                        top = (x1 + side / 2, y1 + height)
                        left = (x1, y1)
                        right = (x1 + side, y1)
                    pygame.draw.polygon(screen, current_color, [left, right, top], 1)

                elif mode == 'rhombus':
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2
                    dx = abs(x2 - x1) // 2
                    dy = abs(y2 - y1) // 2
                    top = (cx, cy - dy)
                    bottom = (cx, cy + dy)
                    left = (cx - dx, cy)
                    right = (cx + dx, cy)
                    pygame.draw.polygon(screen, current_color, [top, right, bottom, left], 1)

                prev = None

        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] and prev and mode in ['draw', 'erase']:
                cur = pygame.mouse.get_pos()
                pygame.draw.line(screen, current_color, prev, cur, 3)
                prev = cur

    draw_toolbar()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
