import sys
import pygame
import random
from Block_Spawn_Loop import block
from Block_List import blockset

# Initialize pygame so it runs in the background and manages things
pygame.init()

#variables
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
falltick = pygame.USEREVENT + 1
spawntick = pygame.USEREVENT + 2
blocklist = blockset()
fall_speed = 700
spawn_speed = 4000
#Various Tickers
pygame.time.set_timer(falltick, fall_speed)
pygame.time.set_timer(spawntick, spawn_speed)
#Function to draw all the obstacle blocks
def draw_all():
        for n in blocklist.getblocks():
            n.draw(screen)
# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode((screen_width,screen_height),0,32)
#add a first block
blocklist.addblock(block(RED, 75,50,random.randint(0,screen_width-75),0))


# Main loop. Your game would go inside this loop
while True:
    #timer which increases difficulty which didnt work
    #if pygame.time.get_ticks() > 30000:
       # fall_speed = 500
       # spawn_speed = 4500
   # elif pygame.time.get_ticks() > 20000:
       # fall_speed = 1000
       # spawn_speed = 5000
  #  elif pygame.time.get_ticks() > 10000:
        #fall_speed = 1500
       # spawn_speed = 6000
   # else:
       # fall_speed = 2000
       # spawn_speed = 7000
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        screen.fill(BLACK)
        #move the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if xspot > 0:
                    xspot -= 10
            if event.key == pygame.K_RIGHT:
                if xspot < (screen_width - player_width):
                    xspot += 10
        #move the blocks down
        if event.type == falltick:
            for n in blocklist.getblocks():
                n.fall(screen_height,20)
                if n.y > (screen_height-30):
                    blocklist.impact(n)
            blocklist.removeblock()
            if blocklist.hitplayer(xspot,yspot,player_width,player_height) == True:
                sys.exit()

    
        if event.type == spawntick:
           blocklist.addblock(block(RED, 75,50,random.randint(0,screen_width-75),0))
           draw_all()
            

    #Create the Player
    pygame.draw.rect(screen,BLUE,(xspot,yspot,player_width,player_height))
    #Create the first block
    draw_all()
    pygame.display.update()