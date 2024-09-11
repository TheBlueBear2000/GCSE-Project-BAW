import pygame
import random
import data
import Player

width, height = data.getScreenSize()[0],data.getScreenSize()[1]
playerSize = (200, 150)

playerRect = pygame.Rect(((width - playerSize[0]) / 2 , (height - playerSize[1]) / 2 ) , (playerSize[0] , playerSize[1]))

def hitbox(type,rect):
    # If the tile has no hitbox, it will never collide anyway
    if type == "none": 
        return False
    
    # If the tile is off the screen it defaults to False
    elif rect.x < 0 or rect.x > width or rect.y < 0 or rect.y > height:
        return False

    # Normal hitbox checks if any corner of the tile to see if it is within a player sized area of the center of the screen
    elif type == "normal":
        if rect.colliderect(playerRect):
            return True
        else:
            return False

    # Normal hitbox checks between the middle and the corner of the tile to see if it is within a player sized area of the center of the screen
    elif type == "small":
        if ((rect.x + (rect.width/4)) < (width - playerSize[0]) / 2 or rect.x + rect.width - (rect.width/4) > (width + playerSize[0]) / 2
            or rect.y + (rect.height/4) < (height - playerSize[1]) / 2 or rect.y + rect.height - (rect.height/4) > (height + playerSize[1]) / 2):
            return False
        else:
            return True
    
    


class tile(pygame.sprite.Sprite):
    def __init__(self, x, y, surface, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x,y
        self.rect.center = (self.rect.x,self.rect.y)
        self.xCoord,self.yCoord = self.rect.x + 40, self.rect.y + 40
        surface.blit(self.image, (self.rect.x,self.rect.y))
        self.animatable, self.updatable = False, False

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
        
    def movement(self, actions,map_sprites,player):
        # Movement #
        if actions["up"] == True:
            self.rect.y += actions["speed"]
        if actions["left"] == True:
            self.rect.x += actions["speed"]
        if actions["right"] == True:
            self.rect.x -= actions["speed"]
        if actions["down"] == True:
            self.rect.y -= actions["speed"]




class collidable(tile):
    def __init__(self, x, y, surface, image):
        tile.__init__(self, x, y, surface, image)
        
    def movement(self, actions, map_sprites, player):
        super().movement(actions,map_sprites,player)

        if hitbox(self.hitbox,self.rect) and self.unconditional:
            for sprite in map_sprites:
                if actions["up"] == True:
                    sprite.rect.y -= actions["speed"]
                if actions["left"] == True:
                    sprite.rect.x -= actions["speed"]
                if actions["right"] == True:
                    sprite.rect.x += actions["speed"]
                if actions["down"] == True:
                    sprite.rect.y += actions["speed"]

class item(tile):
    def __init__(self, id, x, y, surface, image):
        tile.__init__(self, x, y, surface, image)
        self.itemID = id
        self.updatable = True
    
    def update(self,actions,player):
        if actions["action2"]:
                # If the second action button (pickup) is being pressed, test to see if the player is coliding with the tile
                if hitbox(self.hitbox,self.rect):
                    # If they are, add the item to the players inventory and kill sprite
                    player.invEdit(self.itemID, 0, self.csvX, self.csvY)
                    player.addScore(random.randint(self.scoreRange[0],self.scoreRange[1]))
                    self.kill()
    
