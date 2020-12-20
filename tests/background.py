import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])

# load bg image
bg= pygame.image.load('../resources/images/under_the_sea.png')
bg = pygame.transform.scale(bg, (600, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    screen.fill([0,55,55])
    # blit bg image
    screen.blit(bg,[0,0])

    #update screen
    pygame.display.update()


pygame.quit()