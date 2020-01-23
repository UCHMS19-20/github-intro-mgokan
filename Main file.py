import sys
import pygame
import random

# Initialize pygame so it runs in the background and manages things
pygame.init()


WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
BLACK=(0,0,0)
screen_width=500
screen_height=400
player_height = 25
player_width = 50
xspot= 100
yspot=screen_height-player_height
# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode((screen_width,screen_height),0,32)

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        screen.fill(BLACK)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xspot -= 10
            if event.key == pygame.K_RIGHT:
                xspot += 10
    pygame.draw.rect(screen,BLUE,(xspot,yspot,player_width,player_height))
        # Check to see if the current event is a QUIT event
    if event.type == pygame.QUIT:
        # If so, exit the program
        sys.exit()
    pygame.display.update()