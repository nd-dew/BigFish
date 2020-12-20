import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
pygame.quit()