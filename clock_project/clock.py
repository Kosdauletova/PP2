import pygame
import time
from datetime import datetime


pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Часы с руками Микки")

#Загрузим изображение микки
clock_image = pygame.image.load("images/clock_face.png")  # Изображение циферблата
left_hand_image = pygame.image.load("images/left_hand.png")  # Левая рука (секундная стрелка)
right_hand_image = pygame.image.load("images/right_hand.png")  # Правая рука (минутная стрелка)


clock_rect = clock_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
left_hand_rect = left_hand_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
right_hand_rect = right_hand_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

#Время обновления
FPS = 60
clock = pygame.time.Clock()


running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(clock_image, clock_rect)  #Отображаем изображение микки

    
    current_time = datetime.now()
    seconds = current_time.second
    minutes = current_time.minute

    #угол для секундной стрелки (левая рука)
    left_angle = 6 * seconds  # 360° / 60 секунд = 6° на каждую секунду
    #угол для минутной стрелки (правая рука)
    right_angle = 6 * minutes  # 360° / 60 минут = 6° на каждую минуту

    #вращение ручек
    rotated_left_hand = pygame.transform.rotate(left_hand_image, -left_angle)
    rotated_right_hand = pygame.transform.rotate(right_hand_image, -right_angle)

    
    rotated_left_rect = rotated_left_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    rotated_right_rect = rotated_right_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    #ручки
    screen.blit(rotated_left_hand, rotated_left_rect)
    screen.blit(rotated_right_hand, rotated_right_rect)

    
    pygame.display.flip()

