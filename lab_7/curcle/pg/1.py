import pygame as pg

pg.init()

# создаю экран
screen = pg.display.set_mode((800,800))
screen.fill((255,255,255))
x = y = 400
pg.display.flip() # обновляет экран

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit() # будет отслеживать нажатия и закрывать скрин
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        y -= 20
    if keys[pg.K_LEFT]:
        x -= 20
    if keys[pg.K_DOWN]:
        y += 20
    if keys[pg.K_RIGHT]:
        x += 20
    if x < 25 :
        x = 25
    if x > 800 - 25:
        x = 800 - 25
    if y < 25 :
        y = 25
    if y > 800 - 25:
        y = 800 - 25

    screen.fill((255,255,255)) # фон будет белым
    pg.draw.circle(surface=screen,color=(0,0,0), center=(x,y), radius=25)
    pg.display.flip()