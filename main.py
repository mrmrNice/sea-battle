import pygame
pygame.init()

screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

kybiki = []
for x in range(0,500,50):
    for y in range(0,500,50):
        r = pygame.Rect( x + 50, y + 50,50,50)
        kybiki.append(r)
kybiki2 = []
for x in range(0,500,50):
    for y in range(0,500,50):
        r = pygame.Rect(x + 600,y + 50,50,50)
        kybiki2.append(r)

while running:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for k in kybiki:
        pygame.draw.rect(screen,'white',k,5)
    for k in kybiki2:
        pygame.draw.rect(screen,'white',k,5)

    pygame.display.update()

    clock.tick(60)
pygame.quit()
