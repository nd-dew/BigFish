import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])

clock = pygame.time.Clock()
event_every_second = pygame.USEREVENT + 1
pygame.time.set_timer(event_every_second, 1000)

some_number=0
running = True
while running:
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == event_every_second:
            some_number= (some_number+pygame.time.get_ticks()) % 250
            screen.fill((some_number, 100, some_number))
            print("event")

    pygame.display.update()

    # TIMER
    clock.tick(60)
pygame.quit()