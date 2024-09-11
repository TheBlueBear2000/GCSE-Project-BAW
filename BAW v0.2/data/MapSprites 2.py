from typing import ClassVar
import pygame
import csv
import os
import json
from PIL import Image
import random

pygame.init()

class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Loads and creates image & rect
        self.image = pygame.transform.scale(pygame.image.load("assets/objects/squares/map.png"),(10000,8000))
        self.rect = self.image.get_rect()
        self.rect.center = (1500/2,1000/2)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        return

    def forceMove(self,x,y,relative):
        if relative:
            self.rect.x += x
            self.rect.y += y
        else:
            self.rect.x = x
            self.rect.y = y
    
    def saveCoords(self):
        self.saveX = self.rect.x
        self.saveY = self.rect.y

    def rewind(self):
        self.forceMove(self.saveX,self.saveY,False)

    def movement(self,actions):
        # Movement #
        if actions["up"] == True:
            self.rect.y += actions["speed"]
        if actions["left"] == True:
            self.rect.x += actions["speed"]
        if actions["right"] == True:
            self.rect.x -= actions["speed"]
        if actions["down"] == True:
            self.rect.y -= actions["speed"]

    def getXCoord(self):
        return self.rect.x
    def getYCoord(self):
        return self.rect.y




#######################################################################################################################################################################################################################################

                                             ## SOLIDS ##                                                                                                                                                                                            

#######################################################################################################################################################################################################################################


        

class Water(pygame.sprite.Sprite):
    def __init__(self,x,y,surface):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 0
        self.i = 0
        self.images = []
        for i in range(3):
            img = pygame.transform.scale(pygame.image.load("assets/objects/squares/water_" + str(i+1) + ".png"),(80,80))
            #print("loaded water asset " + str(i))
            self.images.append(img)
            self.image = self.images[i]
            self.rect = self.image.get_rect()
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.rect.center = (self.rect.x,self.rect.y)
        self.xCoord,self.yCoord = self.rect.x + 40, self.rect.y + 40
        #print("new water tile has following data: " + str(self.rect.center) + " and all sprites assets have been loaded")
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def update(self,actions,player):
        return

    def forceMove(self,x,y,relative):
        if relative:
            self.rect.x += x
            self.rect.y += y
        else:
            self.rect.x = x
            self.rect.y = y
    
    def saveCoords(self):
        self.saveX = self.rect.x
        self.saveY = self.rect.y

    def rewind(self):
        self.forceMove(self.saveX,self.saveY,False)
        
    def movement(self, actions, map_sprites, player):
        # Movement #
        if actions["up"] == True:
            self.rect.y += actions["speed"]
        if actions["left"] == True:
            self.rect.x += actions["speed"]
        if actions["right"] == True:
            self.rect.x -= actions["speed"]
        if actions["down"] == True:
            self.rect.y -= actions["speed"]

        if not player.getPlayerStats()["hasRaft"]:
            if (((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top left corner for collision
            or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top right corner for collision
            or ((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80)) # Check bottom left corner for collision
            or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80))): # Check bottom right corner for collision
                for sprite in map_sprites:
                    if actions["up"] == True:
                        sprite.rect.y -= actions["speed"]
                    if actions["left"] == True:
                        sprite.rect.x -= actions["speed"]
                    if actions["right"] == True:
                        sprite.rect.x += actions["speed"]
                    if actions["down"] == True:
                        sprite.rect.y += actions["speed"]
        
    def animations(self):
        # Animations #
        self.timer += 1
        if self.timer > 15:
            self.timer = 0
            self.i += 1
            if self.i > 2:
                self.i = 0
            self.image = self.images[self.i]








class Bush(pygame.sprite.Sprite):
    def __init__(self,x,y,surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("assets/objects/squares/bush.png"),(80,80))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.rect.center = (self.rect.x,self.rect.y)
        self.xCoord,self.yCoord = self.rect.x + 40, self.rect.y + 40
        print("new bush tile has following data: " + str(self.rect.center))
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def update(self,actions,player):
        return

    def forceMove(self,x,y,relative):
        if relative:
            self.rect.x += x
            self.rect.y += y
        else:
            self.rect.x = x
            self.rect.y = y
    
    def saveCoords(self):
        self.saveX = self.rect.x
        self.saveY = self.rect.y

    def rewind(self):
        self.forceMove(self.saveX,self.saveY,False)

    def animations(self):
        return
        
    def movement(self, actions, map_sprites, player):
        # Movement #
        if actions["up"] == True:
            self.rect.y += actions["speed"]
        if actions["left"] == True:
            self.rect.x += actions["speed"]
        if actions["right"] == True:
            self.rect.x -= actions["speed"]
        if actions["down"] == True:
            self.rect.y -= actions["speed"]

        if (((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top left corner for collision
        or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top right corner for collision
        or ((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80)) # Check bottom left corner for collision
        or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80))): # Check bottom right corner for collision
            for sprite in map_sprites:
                if actions["up"] == True:
                    sprite.rect.y -= actions["speed"]
                if actions["left"] == True:
                    sprite.rect.x -= actions["speed"]
                if actions["right"] == True:
                    sprite.rect.x += actions["speed"]
                if actions["down"] == True:
                    sprite.rect.y += actions["speed"]









class Fence(pygame.sprite.Sprite):
    def __init__(self,x,y,surface,up,down,left,right):
        pygame.sprite.Sprite.__init__(self)

        construction = pygame.image.load("assets/objects/squares/fence/fence_post.png")
        if up:
            construction.blit(pygame.image.load('assets/objects/squares/fence/fence_up.png'),(0,0))
        if down:
            construction.blit(pygame.image.load('assets/objects/squares/fence/fence_down.png'),(0,0))
        if left:
            construction.blit(pygame.image.load('assets/objects/squares/fence/fence_left.png'),(0,0))
        if right:
            construction.blit(pygame.image.load('assets/objects/squares/fence/fence_right.png'),(0,0))

        self.image = pygame.transform.scale(construction,(80,80))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.rect.center = (self.rect.x,self.rect.y)
        self.xCoord,self.yCoord = self.rect.x + 40, self.rect.y + 40
        print("new fence tile has following data: " + str(self.rect.center) + ", Up: " + str(up) + ", Down: " + str(down) + ", Left: " + str(left) + ", Right: " + str(right))
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def update(self,actions,player):
        return

    def forceMove(self,x,y,relative):
        if relative:
            self.rect.x += x
            self.rect.y += y
        else:
            self.rect.x = x
            self.rect.y = y
    
    def saveCoords(self):
        self.saveX = self.rect.x
        self.saveY = self.rect.y

    def rewind(self):
        self.forceMove(self.saveX,self.saveY,False)

    def animations(self):
        return
        
    def movement(self, actions, map_sprites, player):
        # Movement #
        if actions["up"] == True:
            self.rect.y += actions["speed"]
        if actions["left"] == True:
            self.rect.x += actions["speed"]
        if actions["right"] == True:
            self.rect.x -= actions["speed"]
        if actions["down"] == True:
            self.rect.y -= actions["speed"]

        if (((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top left corner for collision
        or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top right corner for collision
        or ((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80)) # Check bottom left corner for collision
        or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80))): # Check bottom right corner for collision
            for sprite in map_sprites:
                if actions["up"] == True:
                    sprite.rect.y -= actions["speed"]
                if actions["left"] == True:
                    sprite.rect.x -= actions["speed"]
                if actions["right"] == True:
                    sprite.rect.x += actions["speed"]
                if actions["down"] == True:
                    sprite.rect.y += actions["speed"]








class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,surface,up,down,left,right):
        pygame.sprite.Sprite.__init__(self)

        construction = pygame.image.load("assets/objects/squares/wall/wall_post.png")
        if up:
            construction.blit(pygame.image.load('assets/objects/squares/wall/wall_up.png'),(0,0))
        if down:
            construction.blit(pygame.image.load('assets/objects/squares/wall/wall_down.png'),(0,0))
        if left:
            construction.blit(pygame.image.load('assets/objects/squares/wall/wall_left.png'),(0,0))
        if right:
            construction.blit(pygame.image.load('assets/objects/squares/wall/wall_right.png'),(0,0))

        self.image = pygame.transform.scale(construction,(80,80))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.rect.center = (self.rect.x,self.rect.y)
        self.xCoord,self.yCoord = self.rect.x + 40, self.rect.y + 40
        print("new wall tile has following data: " + str(self.rect.center) + ", Up: " + str(up) + ", Down: " + str(down) + ", Left: " + str(left) + ", Right: " + str(right))
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def update(self,actions,player):
        return

    def forceMove(self,x,y,relative):
        if relative:
            self.rect.x += x
            self.rect.y += y
        else:
            self.rect.x = x
            self.rect.y = y
    
    def saveCoords(self):
        self.saveX = self.rect.x
        self.saveY = self.rect.y

    def rewind(self):
        self.forceMove(self.saveX,self.saveY,False)

    def animations(self):
        return
        
    def movement(self, actions, map_sprites, player):
        # Movement #
        if actions["up"] == True:
            self.rect.y += actions["speed"]
        if actions["left"] == True:
            self.rect.x += actions["speed"]
        if actions["right"] == True:
            self.rect.x -= actions["speed"]
        if actions["down"] == True:
            self.rect.y -= actions["speed"]

        if (((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top left corner for collision
        or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top right corner for collision
        or ((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80)) # Check bottom left corner for collision
        or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80))): # Check bottom right corner for collision
            for sprite in map_sprites:
                if actions["up"] == True:
                    sprite.rect.y -= actions["speed"]
                if actions["left"] == True:
                    sprite.rect.x -= actions["speed"]
                if actions["right"] == True:
                    sprite.rect.x += actions["speed"]
                if actions["down"] == True:
                    sprite.rect.y += actions["speed"]






                    
class Tree(pygame.sprite.Sprite):
    def __init__(self,x,y,surface):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.transform.scale(pygame.image.load("assets/objects/squares/tree_stump.png"),(240,240)),pygame.transform.scale(pygame.image.load("assets/objects/squares/tree_top.png"),(240,240))]
        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.rect.center = (self.rect.x,self.rect.y)
        self.xCoord,self.yCoord = self.rect.x + 40, self.rect.y + 40
        print("new Raft tile has following data: " + str(self.rect.center))
        surface.blit(self.image, (self.rect.x,self.rect.y))

        self.itemID = "raft"

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def update(self,actions,player):
        if (((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top left corner for collision
        or ((self.rect.x + (self.rect.width/2) > 1500/2 - 120 and self.rect.x + (self.rect.width/2) < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top middle for collision
        or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y > 1000/2 - 80 and self.rect.y < 1000/2 + 80)) # Check top right corner for collision
        or ((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y + (self.rect.height/2) > 1000/2 - 80 and self.rect.y + (self.rect.height/2) < 1000/2 + 80)) # Check middle left for collision
        or ((self.rect.x + (self.rect.width/2) > 1500/2 - 120 and self.rect.x + (self.rect.width/2) < 1500/2 + 120) and (self.rect.y + (self.rect.height/2) > 1000/2 - 80 and self.rect.y + (self.rect.height/2) < 1000/2 + 80)) # Check middle middle for collision
        or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y + (self.rect.height/2) > 1000/2 - 80 and self.rect.y + (self.rect.height/2) < 1000/2 + 80)) # Check middle right for collision
        or ((self.rect.x > 1500/2 - 120 and self.rect.x < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80)) # Check bottom left corner for collision
        or ((self.rect.x + (self.rect.width/2) > 1500/2 - 120 and self.rect.x + (self.rect.width/2) < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80)) # Check bottom middle for collision
        or ((self.rect.x + self.rect.width > 1500/2 - 120 and self.rect.x + self.rect.width < 1500/2 + 120) and (self.rect.y + self.rect.height > 1000/2 - 80 and self.rect.y + self.rect.height < 1000/2 + 80))): # Check bottom right corner for collision
            self.image = self.images[0]
        else:
            self.image = self.images[1]
                

    def forceMove(self,x,y,relative):
        if relative:
            self.rect.x += x
            self.rect.y += y
        else:
            self.rect.x = x
            self.rect.y = y
    
    def saveCoords(self):
        self.saveX = self.rect.x
        self.saveY = self.rect.y

    def rewind(self):
        self.forceMove(self.saveX,self.saveY,False)
        
    def movement(self, actions, map_sprites, player):
        # Movement #
        if actions["up"] == True:
            self.rect.y += actions["speed"]
        if actions["left"] == True:
            self.rect.x += actions["speed"]
        if actions["right"] == True:
            self.rect.x -= actions["speed"]
        if actions["down"] == True:
            self.rect.y -= actions["speed"]

    def animations(self):
        return

