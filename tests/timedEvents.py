import pygame as pg

pg.init()
screen = pg.display.set_mode([600, 600])

clock = pg.time.Clock()
event_every_second = pg.USEREVENT + 1
pg.time.set_timer(event_every_second, 1000)

some_number=0
running = True
while running:
    # EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == event_every_second:
            some_number= (some_number+pg.time.get_ticks()) % 250
            screen.fill((some_number, 100, some_number))
            print("event")

    pg.display.update()

    # TIMER
    clock.tick(60)
pg.quit()