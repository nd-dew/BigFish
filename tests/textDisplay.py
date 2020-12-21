import pygame

pygame.init()
pygame.font.init() # you have to call this at the start,
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('"Not your ho no mo"- M.S.', False, (255, 255, 255), None)


screen = pygame.display.set_mode([600, 600])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    screen.fill([50,100,50])  # Redrawing the background each pass

    screen.blit(textsurface, (0, 0))
    pygame.display.update()

pygame.quit()