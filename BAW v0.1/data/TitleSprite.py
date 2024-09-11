import pygame
import time
import random

pygame.init()

frame = 0
cycle = 0
animation = 0

class TitleSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        height = 1000
        width = 1500
        self.frame = 0
        self.cycle = 0
        self.timer = 0
        self.images = []
        for i in range(5):
            img = pygame.transform.scale(pygame.image.load("assets/menu/title_sprite_" + str(i+1) + ".png"),(480,320))
            print("loaded asset " + str(i))
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.rect.center = (width/2-250,height/2-180)
        

    def update(self):        


        ##ANIMATION##
        self.timer += 1
        if self.timer > 15:
            self.timer = 0
            if self.cycle == 0:
                self.animation = random.randint(0,2)

            if self.animation == 0:
                self.image = self.images[0]
                if self.cycle < random.randint(8,32):
                    self.cycle += 1
                else:
                    self.cycle = 0
                
            elif self.animation == 1:
                if self.cycle < 6:
                    if self.frame == 0:
                        self.image = self.images[1]
                        self.frame += 1
                    else:
                        self.image = self.images[2]
                        self.frame = 0
                    self.cycle += 1
                else:
                    self.cycle = 0

            elif self.animation == 2:
                if self.cycle < 4:
                    if self.frame == 0:
                        self.image = self.images[3]
                        self.frame += 1
                    else:
                        self.image = self.images[4]
                        self.frame = 0
                    self.cycle += 1
                else:
                    self.cycle = 0
                
        