# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 1080
HEIGHT = 1080
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
pygame.mixer.music.load('uku.mp3')
pygame.mixer.music.play()
#while pygame.mixer.music.get_busy():
    #continue
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    pygame.mixer.music.get_busy()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Обновление

    # Рендеринг
    screen.fill(WHITE)
    ship = pygame.image.load("wa.bmp")
    ship_top = screen.get_height() - ship.get_height()
    ship_left = screen.get_width() / 2 - ship.get_width() / 2
    screen.blit(ship, (ship_left, ship_top))
    start_button = pygame.draw.rect(screen, (RED), (250, 160, 100, 50));

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()