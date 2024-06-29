import pygame
from random import choice


class Block:
    def __init__(self, _x, _y, color):
        self.x = _x
        self.y = _y
        self.color = color
        self.rect = pygame.Rect(_x, _y, 50, 50)
        self.text = ''

    def setText(self, text=''):
        self.text = text

    def draw(self, scr):
        pygame.draw.rect(scr, self.color, self.rect, 1, 0)  # рисуем квадрат
        font = pygame.font.SysFont('verdana', 25).render(self.text, True, 'white')  # создём шрифт для текста
        scr.blit(font, (self.rect.x + 15, self.rect.y + 5))


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

words = ["Дерево", "комп'ютер", "вода", "клавіатура", "поле", "стіл", "ігри", "небо", "сонечко", "земля", "світ", "мова", "склянка", "інтернет", "годинник"]
word = choice(words)
spisok = []

x = 50
for i in range(len(word)):
    spisok.append(Block(x, 50, "white"))
    spisok[i].setText('')
    x += 50

keys = ["А", "Б", "В", "Г", "Ґ", "Д", "Е", "Є", "Ж", "З", "И", "І", "Ї", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ь", "Ю", "Я"]
keyboard = []
x = 50
y = 400
for i in range(len(keys)):
    keyboard.append(Block(x, y, 'blue'))
    keyboard[i].setText(keys[i])
    x += 50
    if i > 0 and i % 11 == 0:
        x = 50
        y += 50

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    for s in spisok:
        s.draw(screen)

    for key in keyboard:
        key.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()


    clock.tick(60)  # limits FPS to 60

pygame.quit()