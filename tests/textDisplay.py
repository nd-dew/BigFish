import pygame

pygame.init()
# pygame.font.init() # you have to call this at the start,
myfont = pygame.font.SysFont('Comic Sans MS', 30)
string= '"Not your ho no mo"- M S .'
splitted= string.split()
i=0
currently_showed=''
textsurface = myfont.render(currently_showed, False, (255, 255, 255), None)


addTEXT= pygame.USEREVENT+1
pygame.time.set_timer(pygame.USEREVENT+1, 100)

screen = pygame.display.set_mode([600, 600])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type ==addTEXT:
            currently_showed += ' '
            currently_showed += splitted[i]

            currently_showed= '' if currently_showed[-1] == '.' else currently_showed
            i = (i + 1 + len(splitted)) % len(splitted)
            textsurface = myfont.render(currently_showed, False, (255, 255, 255), None)


    screen.fill([50,100,50])  # Redrawing the background each pass

    screen.blit(textsurface, (0, 0))
    pygame.display.update()

pygame.quit()