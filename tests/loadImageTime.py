"""Run this file twice using one of commented surface options"""

import time
import pygame

pygame.init()

screen = pygame.display.set_mode([800, 800])  # screen is a tuple of width and height

# First option without convert
# surface = pygame.image.load('../resources/images/someFish540x540.png')

# Second option with convert
surface = pygame.image.load('../resources/images/someFish540x540.png').convert()

running = True

start = time.time()

i=0
while i < 10**3:
    i = i+1;
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False
    screen.blit(surface, [0, 0])
    pygame.display.update()

end = time.time()
print(start)
print(end)
print(end - start)
# import os
# print('../resources/images')
# files = [f for f in os.listdir('../resources/images')]
# for f in files:
#     print(f)
