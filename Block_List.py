import sys
import pygame
import random

class blockset:
    def __init__(self):
        self.blocks = []
        self.hitlist = []

    def addblock(self,block):
        self.blocks.append(block)

    def impact(self,block):
        self.hitlist.append(block)
    
    def removeblock(self):
        for n in self.hitlist:
            while n in self.blocks:
                self.blocks.remove(n)
        self.hitlist.clear()
    
    def getblocks(self):
        return self.blocks

    def hitplayer(self,playerx,playery,playerwidth,playerheight):
        for n in self.blocks:
            rightbound= n.x + n.width
            bottombound = n.y + n.height
            if bottombound > (playery+playerheight):
                if rightbound > playerx and (rightbound < (playerx + playerwidth) or n.x < (playerx + playerwidth)):
                    return True
                if n.x < (playerx + playerwidth) and (n.x > playerx or rightbound < (playerx + playerwidth)):
                    return True
                else: return False
            else: return False
                

