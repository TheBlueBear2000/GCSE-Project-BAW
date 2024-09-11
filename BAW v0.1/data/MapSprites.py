from typing import ClassVar
import pygame
import csv
import os
import json

pygame.init()

class Map(pygame.sprite.Sprite):
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        # Loads and creates image & rect
        self.image = pygame.transform.scale(pygame.image.load("assets/objects/squares/map.png"),(10000,8000))
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = (1500/2,1000/2)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, actions):
        if actions["up"] == True:
            self.rect.y += 4
        if actions["left"] == True:
            self.rect.x += 4
        if actions["right"] == True:
            self.rect.x -= 4
        if actions["down"] == True:
            self.rect.y -= 4
        
