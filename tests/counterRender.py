import pygame

# Init font, counter
pygame.init()
screen = pygame.display.set_mode([600, 600])
screen_rect= screen.get_rect()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
counter=0
counter_img = myfont.render(str(counter), False, (255, 255, 255), None)
counter_rect= counter_img.get_rect()

# Create event to increment counter
yourCounter= pygame.USEREVENT + 1
pygame.time.set_timer(pygame.USEREVENT+1, 10)

# MAIN LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == yourCounter:
            counter_img = myfont.render(str(counter), False, (255, 255, 255), None)
            counter+=1


    screen.fill([50,100,50])  # Redrawing the background each pass
    counter_rect= counter_img.get_rect()
    counter_rect.bottomright= screen_rect.bottomright
    screen.blit(counter_img, counter_rect.topleft)
    pygame.display.update()

pygame.quit()