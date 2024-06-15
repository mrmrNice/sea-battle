import pygame
from ships import *
import random
pygame.init()

class Section:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = 'white'

    def draw(self, scr):
        pygame.draw.rect(scr, self.color, self.rect, 3)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

kybiki = []
for x in range(0,500,50):
    for y in range(0,500,50):
        r = Section( x + 50, y + 50)
        kybiki.append(r)

kybiki2 = []
for x in range(0,500,50):
    for y in range(0,500,50):
        r = Section(x + 600,y + 50)
        kybiki2.append(r)

ship1 = QuarterShip()
s = random.choice(kybiki)
index = kybiki.index(s)
sections = []
for i in range(ship1.section):
    sections.append(kybiki[index + i])

ship1.setShip(sections)

while running:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for k in kybiki:
        k.draw(screen)
    for k in kybiki2:
        k.draw(screen)

    pygame.display.update()

    clock.tick(60)
pygame.quit()


