import pygame
from pygame.draw import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (64, 64, 64)

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, GRAY, (0, 0, 400, 400))
circle(screen, YELLOW, (200, 200), 100)
circle(screen, BLACK, (200, 200), 101, 1)
circle(screen, RED, (150, 180), 20)
circle(screen, BLACK, (150, 180), 21, 1)
circle(screen, BLACK, (150, 180), 10)
circle(screen, RED, (250, 180), 15)
circle(screen, BLACK, (250, 180), 16, 1)
circle(screen, BLACK, (250, 180), 10)
rect(screen, BLACK, (150, 250, 100, 20))
polygon(screen, BLACK, ([[98, 124], [103, 116], [182, 166], [177, 174]]))
polygon(screen, BLACK, ([[223, 174], [219, 166], [297, 136], [302, 144]]))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()