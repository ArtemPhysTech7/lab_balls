import pygame
from classes import Ball, Square, strike
pygame.init()

FPS = 45
screen = pygame.display.set_mode((900, 500))  # размер экрана


pygame.display.update()
clock = pygame.time.Clock()
finished = False

all_sprite = pygame.sprite.Group()
balls = pygame.sprite.Group()  # создаем 5 экземпляров класса Ball и 5 Square
squares = pygame.sprite.Group()

for i in range(5):
    s = Square()
    squares.add(s)
    all_sprite.add(s)

for i in range(5):
    b = Ball()
    balls.add(b)
    all_sprite.add(b)


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # если нажать на крестик, то игра завершится
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:  # если пользователь нажимает левую кнопку мыши, то проверяется попал ли игрок по цели
            if event.button == 1:
                for i in all_sprite:
                    if i in balls:
                        if strike('b', event.pos[0], event.pos[1], i.coordinate()):
                            i.kill()
                            b = Ball()
                            balls.add(b)
                            all_sprite.add(b)
                    elif i in squares:
                        if strike('s', event.pos[0], event.pos[1], i.coordinate()):
                            i.kill()
                            s = Square()
                            squares.add(s)
                            all_sprite.add(s)

    all_sprite.update()
    pygame.display.update()
    screen.fill((0, 0, 0))
    all_sprite.draw(screen)
    pygame.display.flip()
