import pygame
import os
from PIL import Image
import random
import MapSprites_util as util
import data

dir = data.getDir()
width, height = data.getScreenSize()[0],data.getScreenSize()[1]

pygame.init()

class Map(pygame.sprite.Sprite):
    def __init__(self,savedData):
        pygame.sprite.Sprite.__init__(self)
        # Loads and creates image & rect
        self.image = pygame.transform.scale(pygame.image.load(dir + "assets/objects/squares/map.png"),(10000,8000))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = (savedData[0]) - 40, (savedData[1]) - 40

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def getSavedData(self):
        return [self.rect.x + 30, self.rect.y + 40]
            

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

    def movement(self,actions,map_sprites):
        # Movement #
        if actions["up"] == True:
            self.rect.y += actions["speed"]
        if actions["left"] == True:
            self.rect.x += actions["speed"]
        if actions["right"] == True:
            self.rect.x -= actions["speed"]
        if actions["down"] == True:
            self.rect.y -= actions["speed"]

        if (self.rect.x > 1500/2 - 120) or (self.rect.x + self.rect.width < 1500/2 + 120) or (self.rect.y > 1000/2 - 80) or (self.rect.y + self.rect.height < 1000/2 + 80):
            for sprite in map_sprites:
                if actions["up"] == True:
                    sprite.rect.y -= actions["speed"]
                if actions["left"] == True:
                    sprite.rect.x -= actions["speed"]
                if actions["right"] == True:
                    sprite.rect.x += actions["speed"]
                if actions["down"] == True:
                    sprite.rect.y += actions["speed"]

    def getXCoord(self):
        return self.rect.x
    def getYCoord(self):
        return self.rect.y




#######################################################################################################################################################################################################################################

                                             ## SOLIDS ##                                                                                                                                                                                            

#######################################################################################################################################################################################################################################


        

class Water(util.collidable):
    def __init__(self,x,y,surface):
        self.unconditional = False
        self.timer = 0
        self.i = 0
        self.images = []
        self.hitbox = "normal"
        for i in range(3):
            img = pygame.transform.scale(pygame.image.load(dir + "assets/objects/squares/water_" + str(i+1) + ".png"),(80,80))
            self.images.append(img)
            self.image = self.images[i]
        util.collidable.__init__(self,x,y,surface,self.images[0])
        self.animatable = True
        
    def movement(self, actions, map_sprites, player):
        # Movement #
        super().movement(actions, map_sprites, player)

        if not player.getPlayerStats()["hasRaft"]:
            if util.hitbox("normal",self.rect):
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








class Bush(util.collidable):
    def __init__(self,x,y,surface):
        util.collidable.__init__(self,x,y,surface,pygame.transform.scale(pygame.image.load(dir + "assets/objects/squares/bush.png"),(80,80)))
        print("new Bush tile has following data: " + str(self.rect.center))
        self.hitbox = "normal"
        self.unconditional = True











class Fence(util.collidable):
    def __init__(self,x,y,surface,up,down,left,right):

        construction = pygame.image.load(dir + "assets/objects/squares/fence/fence_post.png")
        if up:
            construction.blit(pygame.image.load(dir + 'assets/objects/squares/fence/fence_up.png'),(0,0))
        if down:
            construction.blit(pygame.image.load(dir + 'assets/objects/squares/fence/fence_down.png'),(0,0))
        if left:
            construction.blit(pygame.image.load(dir + 'assets/objects/squares/fence/fence_left.png'),(0,0))
        if right:
            construction.blit(pygame.image.load(dir + 'assets/objects/squares/fence/fence_right.png'),(0,0))

        construction = pygame.transform.scale(construction,(80,80))

        util.collidable.__init__(self,x,y,surface,construction)
        print("new fence tile has following data: " + str(self.rect.center) + ", Up: " + str(up) + ", Down: " + str(down) + ", Left: " + str(left) + ", Right: " + str(right))

        self.hitbox = "small"
        self.unconditional = True







class Wall(util.collidable):
    def __init__(self,x,y,surface,up,down,left,right):

        construction = pygame.image.load(dir + "assets/objects/squares/wall/wall_post.png")
        if up:
            construction.blit(pygame.image.load(dir + 'assets/objects/squares/wall/wall_up.png'),(0,0))
        if down:
            construction.blit(pygame.image.load(dir + 'assets/objects/squares/wall/wall_down.png'),(0,0))
        if left:
            construction.blit(pygame.image.load(dir + 'assets/objects/squares/wall/wall_left.png'),(0,0))
        if right:
            construction.blit(pygame.image.load(dir + 'assets/objects/squares/wall/wall_right.png'),(0,0))

        construction = pygame.transform.scale(construction,(80,80))

        util.collidable.__init__(self,x,y,surface,construction)
        print("new Wall tile has following data: " + str(self.rect.center) + ", Up: " + str(up) + ", Down: " + str(down) + ", Left: " + str(left) + ", Right: " + str(right))

        self.hitbox = "small"
        self.unconditional = True






                    
class Tree(util.collidable):
    def __init__(self,x,y,surface):
        self.images = [pygame.transform.scale(pygame.image.load(dir + "assets/objects/squares/tree_stump.png"),(240,240)),pygame.transform.scale(pygame.image.load("assets/objects/squares/tree_top.png"),(240,240))]
        
        util.collidable.__init__(self,x,y,surface,self.images[1])

        print("new Tree tile has following data: " + str(self.rect.center))

        self.hitbox = "none"
        self.unconditional = False
        self.updatable = True

    def update(self,actions,player):
        if self.rect.collidepoint((width/2,height/2)):
            self.image = self.images[0]
        else:
            self.image = self.images[1]







#######################################################################################################################################################################################################################################

                                             ## ITEMS ##                                                                                                                                                                                            

#######################################################################################################################################################################################################################################



class Raft(util.item):
    def __init__(self,x,y,surface,csvX,csvY):
        util.item.__init__(self,"raft" , x, y, surface, pygame.transform.scale(pygame.image.load(dir + "assets/objects/squares/items/raft.png"),(160,120)))
        print("new Raft tile has following data: " + str(self.rect.center))
        self.csvX,self.csvY = csvX,csvY
        self.scoreRange = (45,55)
        self.hitbox = "normal"



class Bone(util.item):
    def __init__(self,x,y,surface,csvX,csvY):
        util.item.__init__(self,"bone" , x, y, surface, pygame.transform.scale(pygame.image.load(dir + "assets/objects/squares/items/bone.png"),(80,80)))
        print("new Bone tile has following data: " + str(self.rect.center))
        self.csvX,self.csvY = csvX,csvY
        self.scoreRange = (15,25)
        self.hitbox = "normal"



class TennisBall(util.item):
    def __init__(self,x,y,surface,csvX,csvY):
        util.item.__init__(self,"tennis_ball" , x, y, surface, pygame.transform.scale(pygame.image.load(dir + "assets/objects/squares/items/tennis_ball.png"),(80,80)))
        print("new Tennis Ball tile has following data: " + str(self.rect.center))
        self.csvX,self.csvY = csvX,csvY
        self.scoreRange = (15,25)
        self.hitbox = "normal"


class Chest(util.item):
    def __init__(self,x,y,surface,csvX,csvY):
        util.item.__init__(self,"chest" , x, y, surface, pygame.transform.scale(pygame.image.load(dir + "assets/objects/squares/items/chest.png"),(80,80)))
        print("new Chest tile has following data: " + str(self.rect.center))
        self.csvX,self.csvY = csvX,csvY
        self.scoreRange = (45,55)
        self.hitbox = "normal"
