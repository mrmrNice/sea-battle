import pygame
pygame.init()

class Section:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def draw(self, scr):
        pygame.draw.rect(scr, 'white', self.rect, 3)

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
        r =Section(x + 600,y + 50)
        kybiki2.append(r)

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


