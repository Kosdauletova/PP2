import pygame
import os


pygame.init()


size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Music Player")


white = (255, 255, 255)
black = (0, 0, 0)


font = pygame.font.SysFont(None, 48)

pygame.mixer.init()


music_dir = r"C:\Users\орром\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\programming2\PP2\lab7_1\music_player_project\music_files"
music_files = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
music_files.sort()


if not music_files:
    print("No music files found! Exiting...")
    pygame.quit()
    exit()


current_music = 0
pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music]))


is_playing = False


play_icon = pygame.image.load(r"C:\Users\орром\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\programming2\PP2\lab7_1\music_player_project\icons\icons\play-icon.png").convert_alpha()
pause_icon = pygame.image.load(r"C:\Users\орром\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\programming2\PP2\lab7_1\music_player_project\icons\icons\pause_icon.png").convert_alpha()


next_button_image = pygame.image.load(r"C:\Users\орром\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\programming2\PP2\lab7_1\music_player_project\icons\icons\next_icon.png").convert_alpha()
prev_button_image = pygame.image.load(r"C:\Users\орром\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\programming2\PP2\lab7_1\music_player_project\icons\icons\previous_icon.png").convert_alpha()


button_size = (70, 70) 
next_button_image = pygame.transform.scale(next_button_image, button_size)
prev_button_image = pygame.transform.scale(prev_button_image, button_size)


def play_music():
    global is_playing
    pygame.mixer.music.play()
    is_playing = True

def pause_music():
    global is_playing
    pygame.mixer.music.pause()
    is_playing = False

def stop_music():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False

def next_music():
    global current_music, is_playing
    current_music = (current_music + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music]))
    pygame.mixer.music.play()
    is_playing = True

def prev_music():
    global current_music, is_playing
    current_music = (current_music - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music]))
    pygame.mixer.music.play()
    is_playing = True


clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pause_music()
                else:
                    play_music()
            elif event.key == pygame.K_ESCAPE:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_music()
            elif event.key == pygame.K_LEFT:
                prev_music()

 
    screen.fill(white)

    text = font.render(music_files[current_music], True, black)
    text_rect = text.get_rect(center=(width//2, height//2 - 80))
    screen.blit(text, text_rect)


    play_pause_icon = pause_icon if is_playing else play_icon
    play_pause_rect = play_pause_icon.get_rect(center=(width//2, height//2 + 50))
    screen.blit(play_pause_icon, play_pause_rect)


    prev_button_rect = prev_button_image.get_rect(center=(width//2 - 180, height//2 + 50))  # More spacing
    next_button_rect = next_button_image.get_rect(center=(width//2 + 180, height//2 + 50))  # More spacing

    screen.blit(prev_button_image, prev_button_rect)
    screen.blit(next_button_image, next_button_rect)


    pygame.display.flip()


    clock.tick(60)


pygame.quit()
