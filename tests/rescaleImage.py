import pygame as pg

pg.init()
screen = pg.display.set_mode([600, 600])
fish_surface= pg.image.load('../resources/images/someFish540x540.png').convert()

fish_surface_rescaled= pg.transform.scale(fish_surface, [300,300])
fish_surface_rescaled2= pg.transform.scale(fish_surface, [600,600])

running=True
i=0
while running:
    i+=1

    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
           running=False

    screen.fill((0, 0, 0))
    if i < 10e2:
        screen.blit(fish_surface, [0, 0])
    elif i > 10e2:
        screen.blit(fish_surface_rescaled, [0,0])
        if i > 2*10e2:
            i=0

    pg.display.update()

pg.quit()
