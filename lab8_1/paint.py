import pygame
import sys


pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Программа для рисования")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
VIOLET = (238, 130, 238)
PINK = (255, 105, 180)

COLOR_CHOICES = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, VIOLET, PINK, BLACK]
current_color = BLACK


brush_size = 5
drawing = False
shape_mode = 'line'  
start_x, start_y = 0, 0

#функции для рисования форм
def draw_rect(surface, color, start_pos, end_pos):
    pygame.draw.rect(surface, color, pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)

def draw_circle(surface, color, start_pos, end_pos):
    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
    pygame.draw.circle(surface, color, start_pos, radius, 2)

def erase(surface, start_pos, end_pos):
    pygame.draw.rect(surface, WHITE, pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))

def draw_line(surface, color, start_pos, end_pos):
    pygame.draw.line(surface, color, start_pos, end_pos, brush_size)


def clear_screen(surface):
    surface.fill(WHITE)

#основной цикл игры
def main():
    global drawing, start_x, start_y, shape_mode, current_color

    
    drawing_surface = pygame.Surface((width, height))
    drawing_surface.fill(WHITE)
    screen.fill(WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_color = RED
                elif event.key == pygame.K_2:
                    current_color = ORANGE
                elif event.key == pygame.K_3:
                    current_color = YELLOW
                elif event.key == pygame.K_4:
                    current_color = GREEN
                elif event.key == pygame.K_5:
                    current_color = CYAN
                elif event.key == pygame.K_6:
                    current_color = BLUE
                elif event.key == pygame.K_7:
                    current_color = VIOLET
                elif event.key == pygame.K_8:
                    current_color = PINK
                elif event.key == pygame.K_9:
                    current_color = BLACK
                elif event.key == pygame.K_0:
                    current_color = WHITE  #ластик
                elif event.key == pygame.K_c:
                    shape_mode = 'circle'
                elif event.key == pygame.K_r:
                    shape_mode = 'rect'
                elif event.key == pygame.K_x:
                    clear_screen(drawing_surface)  #очистка экрана

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    drawing = True
                    start_x, start_y = event.pos

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    if shape_mode == 'rect':
                        draw_rect(drawing_surface, current_color, (start_x, start_y), event.pos)
                    elif shape_mode == 'circle':
                        draw_circle(drawing_surface, current_color, (start_x, start_y), event.pos)
                    elif shape_mode == 'line':
                        draw_line(drawing_surface, current_color, (start_x, start_y), event.pos)

            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    if shape_mode == 'line':
                        draw_line(drawing_surface, current_color, (start_x, start_y), event.pos)
                        start_x, start_y = event.pos
                    elif shape_mode == 'rect':
                        #просто рисуем прямоугольник, пока мышь двигается
                        screen.fill(WHITE)
                        screen.blit(drawing_surface, (0, 0))
                        draw_rect(screen, current_color, (start_x, start_y), event.pos)
                    elif shape_mode == 'circle':
                        #просто рисуем круг, пока мышь двигается
                        screen.fill(WHITE)
                        screen.blit(drawing_surface, (0, 0))
                        draw_circle(screen, current_color, (start_x, start_y), event.pos)
                    elif current_color == WHITE:  #ластик
                        erase(drawing_surface, (start_x, start_y), event.pos)
                        start_x, start_y = event.pos

        
        screen.fill(WHITE)  
        screen.blit(drawing_surface, (0, 0))  

        
        pygame.display.update()


if __name__ == "__main__":
    main()
