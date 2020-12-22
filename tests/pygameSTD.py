import pygame as pg

pg.init()
screen = pg.display.set_mode([600, 600])

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
pg.quit()