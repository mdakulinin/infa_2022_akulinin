import pygame
from pygame.draw import *
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIME = (127, 255, 42)
SKIN = (233, 198, 175)
ORANGE = (255, 102, 0)
BLUE = (128, 179, 255)
BROWN = (51, 38, 28)
PURPLE = (212, 42, 255)
YELLOW = (255, 212, 42)
GRAY = (190, 200, 183)
GREEN = (0, 128, 0)

coords = [255, 284, 228, 226, 292, 230, 276, 246, 261, 183, 327, 204, 313, 216, 310, 151, 367, 181, 348, 195, 356, 132, 406, 171, 389, 180, 412, 119, 452, 168, 437, 177, 472, 123, 500, 179, 489, 185, 522, 129, 554, 184, 535, 187, 592, 157, 589, 222, 576, 203, 639, 188, 621, 251, 611, 231, 676, 228, 645, 286] #координаты волос

FPS = 30
sc = pygame.display.set_mode((1800, 768))

rect(sc, WHITE, (0, 0, 1800, 768)) #белый фон
circle(sc, ORANGE, (454, 768), 238) #тело
circle(sc, SKIN, (450, 398), 225) #лицо
circle(sc, BLACK, (450, 398), 226, 1)
polygon(sc, BROWN, [[430, 415], [470, 415], [450, 450]]) #нос
polygon(sc, RED, [[325, 465], [570, 465], [452, 544]]) #рот
circle(sc, BLUE, (375, 360), 50) #глаза
circle(sc, BLACK, (375, 360), 51, 1)
circle(sc, BLUE, (523, 360), 50)
circle(sc, BLACK, (523, 360), 51, 1)
circle(sc, BLACK, (375, 367), 13)
circle(sc, BLACK, (523, 367), 13)
polygon(sc, SKIN, [[236, 563], [204, 575], [70, 126], [103, 118]]) #руки
polygon(sc, SKIN, [[669, 564], [702, 572], [857, 123], [823, 119]])
sh1 = [[183, 675], [173, 577], [245, 540], [310, 605], [273, 688]] #плечи
polygon(sc, ORANGE, sh1)
line(sc, BLACK, sh1[0], sh1[1])
line(sc, BLACK, sh1[1], sh1[2])
line(sc, BLACK, sh1[2], sh1[3])
line(sc, BLACK, sh1[3], sh1[4])
line(sc, BLACK, sh1[4], sh1[0])
sh2 = [[633, 692], [595, 617], [650, 540], [725, 567], [720, 667]]
polygon(sc, ORANGE, sh2)
line(sc, BLACK, sh2[0], sh2[1])
line(sc, BLACK, sh2[1], sh2[2])
line(sc, BLACK, sh2[2], sh2[3])
line(sc, BLACK, sh2[3], sh2[4])
line(sc, BLACK, sh2[4], sh2[0])
circle(sc, SKIN, (80, 90), 40) #ладони
circle(sc, WHITE, (80, 90), 41, 1)
circle(sc, SKIN, (850, 90), 40)
circle(sc, WHITE, (850, 90), 41, 1)

#волосы
for i in range(10):
    x1 = coords[i * 6 + 0]
    y1 = coords[i * 6 + 1]
    x2 = coords[i * 6 + 2]
    y2 = coords[i * 6 + 3]
    x3 = coords[i * 6 + 4]
    y3 = coords[i * 6 + 5]
    polygon(sc, PURPLE, [[x1, y1], [x2, y2], [x3, y3]])
    line(sc, BLACK, [x1, y1], [x2, y2])
    line(sc, BLACK, [x2, y2], [x3, y3])
    line(sc, BLACK, [x3, y3], [x1, y1])
    

#координаты волос                    
coords1 = []
for i in range(len(coords)):
    if i % 2 == 0:
        coords1.append(coords[i] + 900)
    else:
        coords1.append(coords[i])

circle(sc, GREEN, (1354, 768), 238) #тело
circle(sc, SKIN, (1350, 398), 225) #лицо
circle(sc, BLACK, (1350, 398), 226, 1) 
polygon(sc, BROWN, [[1330, 415], [1370, 415], [1350, 450]]) #нос
polygon(sc, RED, [[1225, 465], [1470, 465], [1352, 544]]) #рот
circle(sc, GRAY, (1275, 360), 50) #глаза
circle(sc, BLACK, (1275, 360), 51, 1)
circle(sc, GRAY, (1423, 360), 50)
circle(sc, BLACK, (1423, 360), 51, 1)
circle(sc, BLACK, (1275, 367), 13)
circle(sc, BLACK, (1423, 367), 13)
polygon(sc, SKIN, [[1136, 563], [1104, 575], [970, 126], [1003, 118]]) #руки
polygon(sc, SKIN, [[1569, 564], [1602, 572], [1757, 123], [1723, 119]])
sh1 = [[1083, 675], [1073, 577], [1145, 540], [1210, 605], [1173, 688]] #плечи
polygon(sc, GREEN, sh1)
line(sc, BLACK, sh1[0], sh1[1])
line(sc, BLACK, sh1[1], sh1[2])
line(sc, BLACK, sh1[2], sh1[3])
line(sc, BLACK, sh1[3], sh1[4])
line(sc, BLACK, sh1[4], sh1[0])
sh2 = [[1533, 692], [1495, 617], [1550, 540], [1625, 567], [1620, 667]]
polygon(sc, GREEN, sh2)
line(sc, BLACK, sh2[0], sh2[1])
line(sc, BLACK, sh2[1], sh2[2])
line(sc, BLACK, sh2[2], sh2[3])
line(sc, BLACK, sh2[3], sh2[4])
line(sc, BLACK, sh2[4], sh2[0])
circle(sc, SKIN, (980, 90), 40) #ладони
circle(sc, WHITE, (980, 90), 41, 1)
circle(sc, SKIN, (1750, 90), 40)
circle(sc, WHITE, (1750, 90), 41, 1)
rect(sc, BLACK, (0, 0, 1800, 90)) #табличка
rect(sc, LIME, (2, 2, 1846, 85))

#волосы
for i in range(10):
    x1 = coords1[i * 6 + 0]
    y1 = coords1[i * 6 + 1]
    x2 = coords1[i * 6 + 2]
    y2 = coords1[i * 6 + 3]
    x3 = coords1[i * 6 + 4]
    y3 = coords1[i * 6 + 5]
    polygon(sc, YELLOW, [[x1, y1], [x2, y2], [x3, y3]])
    line(sc, BLACK, [x1, y1], [x2, y2])
    line(sc, BLACK, [x2, y2], [x3, y3])
    line(sc, BLACK, [x3, y3], [x1, y1])
    
#шрифт
pygame.font.init()
f = pygame.font.Font(None, 127)
text = f.render('PYTHON is REALLY AMAZING', True, BLACK)
sc.blit(text, (200, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()