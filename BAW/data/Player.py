import pygame
from data import getDir

dir = getDir()

class Player(pygame.sprite.Sprite):
    def __init__(self,savedData):
        # Initiates the Sprite class taht is built into pygame
        pygame.sprite.Sprite.__init__(self)

        # Sets animation variables to be used in animation
        self.animation_tick = 0
        self.frame = 0
        self.animation_speed = 10

        # Loads players data

        self.inv = savedData["inv"]
        self.score = savedData["score"]
        self.hasRaft = savedData["hasRaft"]

        ## LOADS ALL IMAGES INTO ARRAYS FOR EASY ACCESS
        self.left = []
        self.right = []
        self.up = []
        self.down = []
        for i in range(4):
            img = pygame.transform.scale(pygame.image.load(dir + "assets/objects/sprites/player/sideways_" + str(i+1) + ".png"),(240,160))
            print("loaded player left asset " + str(i))
            self.left.append(img)
            self.image = self.left[i]
            self.rect = self.image.get_rect()
        for i in range(4):
            img = pygame.transform.flip(pygame.transform.scale(pygame.image.load(dir + "assets/objects/sprites/player/sideways_" + str(i+1) + ".png"),(240,160)), True, False)
            print("loaded player right asset " + str(i))
            self.right.append(img)
            self.image = self.right[i]
            self.rect = self.image.get_rect()
        for i in range(4):
            img = pygame.transform.scale(pygame.image.load(dir + "assets/objects/sprites/player/up_" + str(i+1) + ".png"),(240,160))
            print("loaded player up asset " + str(i))
            self.up.append(img)
            self.image = self.up[i]
            self.rect = self.image.get_rect()
        for i in range(4):
            img = pygame.transform.scale(pygame.image.load(dir + "assets/objects/sprites/player/down_" + str(i+1) + ".png"),(240,160))
            print("loaded player down asset " + str(i))
            self.down.append(img)
            self.image = self.down[i]
            self.rect = self.image.get_rect()

        # Sets the image to be static facing left and gets its data, and sets its location to the center of the screen
        self.image = self.left[0]
        self.rect = self.image.get_rect()
        self.rect.center = (1500/2,1000/2)

    def update(self, actions):

        # ANIMATIONS #
        
        # Sets the animation tick speed (FPS of the animation) depending on if the player is sprinting
        self.animation_speed = 18 - actions["speed"]

        # Adds 1 to the animation's game tick
        self.animation_tick += 1

        # If the game number ticks is the required ammount for a frame, it is reset and the frame is chosen and played, depending on the players current movement direction
        if self.animation_tick > self.animation_speed:
            self.animation_tick = 0

            if actions["up"] == False:
                for i in range(3):
                    if self.image == self.up[i]:
                        self.image = self.up[0]
            if actions["down"] == False:
                for i in range(3):
                    if self.image == self.down[i]:
                        self.image = self.down[0]
            if actions["right"] == False:
                for i in range(3):
                    if self.image == self.right[i]:
                        self.image = self.right[0]
            if actions["left"] == False:
                for i in range(3):
                    if self.image == self.left[i]:
                        self.image = self.left[0]

            if actions["left"] == True:
                self.frame += 1
                if self.frame > 3:
                    self.frame = 0
                self.image = self.left[self.frame]

            elif actions["right"] == True:
                self.frame += 1
                if self.frame > 3:
                    self.frame = 0
                self.image = self.right[self.frame]

            elif actions["up"] == True:
                self.frame += 1
                if self.frame > 3:
                    self.frame = 0
                self.image = self.up[self.frame]

            elif actions["down"] == True:
                self.frame += 1
                if self.frame > 3:
                    self.frame = 0
                self.image = self.down[self.frame]

    def draw(self,surface):
        # Draws the player to the screen
        surface.blit(self.image, (self.rect.x,self.rect.y))

    def addScore(self,score):
        self.score += score

    def getPlayerStats(self):
        # Gets all player statistics in the form of a dictionary, so that the rest of the program can easily access them
        return {
            "inv": self.inv,
            "score": self.score,
            "hasRaft": self.hasRaft
            }

    def invEdit(self,item,addOrRemove,itemX,itemY):
        if addOrRemove == 0:
            self.inv.append([item,itemX,itemY])


            if item == "raft":
                self.hasRaft = True
        
        elif addOrRemove == 1:
            for i in range(len(self.inv)):
                if i == item:
                    i.pop
                    break

        