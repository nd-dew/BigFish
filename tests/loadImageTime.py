"""Run this file twice using one of commented surface options"""

import time
import pygame as pg

pg.init()

screen = pg.display.set_mode([800, 800])  # screen is a tuple of width and height

# First option without convert
# surface = pg.image.load('../resources/images/someFish540x540.png')

# Second option with convert
surface = pg.image.load('../resources/images/someFish540x540.png').convert()

running = True

start = time.time()

i=0
while i < 10**3:
    i = i+1;
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
            running = False
    screen.blit(surface, [0, 0])
    pg.display.update()

end = time.time()
print(start)
print(end)
print(end - start)
# import os
# print('../resources/images')
# files = [f for f in os.listdir('../resources/images')]
# for f in files:
#     print(f)
