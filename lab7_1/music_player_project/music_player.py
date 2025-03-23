import pygame
import os


pygame.init()


WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простой музыкальный плеер")

#наш путь к папке с музыкой
music_folder = r"C:\Users\орром\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\pp2\pygame\lab7\music_player_project\music_files"
music_files = [f for f in os.listdir(music_folder) if f.endswith(('.mp3', '.wav'))]
current_track_index = 0

#это для воспроизведения музыки
pygame.mixer.init()


is_playing = False
is_stopped = False

#функция для воспроизведения музыки
def play_music():
    global is_playing, is_stopped
    if not is_playing:
        track_path = os.path.join(music_folder, music_files[current_track_index])
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()
        is_playing = True
        is_stopped = False
        print(f"Воспроизводится: {music_files[current_track_index]}")

#функция для стоп музыки
def stop_music():
    global is_playing, is_stopped
    pygame.mixer.music.stop()
    is_playing = False
    is_stopped = True
    print("Музыка остановлена")

#функция для перехода к следующему треку
def next_music():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    print(f"Следующий трек: {music_files[current_track_index]}")
    stop_music()
    play_music()

#функция для перехода к предыдущему треку
def previous_music():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    print(f"Предыдущий трек: {music_files[current_track_index]}")
    stop_music()
    play_music()


running = True
while running:
    screen.fill((255, 255, 255))  #очистим
    pygame.display.update()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # P — воспроизведение
                if is_stopped:
                    play_music()
            elif event.key == pygame.K_s:  # S — стоп
                stop_music()
            elif event.key == pygame.K_n:  # N — следующий трек
                next_music()
            elif event.key == pygame.K_b:  # B — предыдущий трек
                previous_music()


pygame.quit()
