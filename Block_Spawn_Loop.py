import sys
import pygame
import random

class block:
    def __init__(self, color, width, height, xcord, ycord):
        #creates block class
        self.color = color
        self.width = width
        self.height = height
        self.x = xcord
        self.y = ycord

    def draw(self,screen):
        #draws a block
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))

    def fall(self,screen_height,speed):
        if self.y < (screen_height+10):
            #delete this block Move this block
           self.y += speed