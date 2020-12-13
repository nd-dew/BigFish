import pygame
from random import Random
# from Player import Player
# from Settings import Settings

# game = Settings()
#
# player = Player()
# player.show()

#this initializes pygame

pygame.init()

#creates the screen
screen = pygame.display.set_mode((500,500))

#title and icon
pygame.display.set_caption("Bigger Fish")
icon = pygame.image.load("clown-fish-icon.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("Sprite Sheets/tile037.png")
playerX = 250
playerY = 450
playerX_change = 0

def player(x,y):
     #this draws the image of the character into the screen
     screen.blit(playerImg, (x, y)) #draw

#game loop
running = True
while running:
    screen.fill((127, 210, 223))  # Background color RGB

    for event in pygame.event.get(): # manages all the triggered events
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  #CHECKS THAT ANY KEYSTROKE IS PRESSED (KEYUP IS RELEASING THE KEY)
            #print("KEYDOWN")
            if event.key == pygame.K_LEFT:  #NOW I CHECK IF IT WAS LEFT KEY
                #print("KEY LEFT")
                playerX_change -= 0.05
                playerImg = pygame.image.load("Sprite Sheets/tile036.png")
            if event.key == pygame.K_RIGHT:
                #print("KEY RIGHT")
                playerX_change += 0.05
                playerImg = pygame.image.load("Sprite Sheets/tile038.png")
        if event.type == pygame.KEYUP:
            #print("KEYUP")
            playerX_change = 0
            playerImg = pygame.image.load("Sprite Sheets/tile037.png")

    playerX += playerX_change

    #Player movement boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 460:
        playerX = 460

    player(playerX, playerY)
    pygame.display.update()  # mandatory to update screen