import pygame
import sys
import buttons
from pygame.constants import QUIT
import time
import TitleSprite
import threading
import MapSprites


pygame.init()
clock = pygame.time.Clock()

height = 1000
width = 1500

timer = 0


menuBackground = pygame.image.load("assets/menu/background.png")

background_colour = (91,185,44)
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bonzo's Adventures in Wonderland")
gameDisplay.fill(background_colour)
gameDisplay.blit(menuBackground,(0,0))

actions = {
    "left": False,
    "right": False,
    "up": False,
    "down": False,
    "action1": False,
    "action2": False,
    "start": False
}


textColorWhite = (255,255,255)
textColorBlack = (0,0,0)

buttonColor = (50,50,50)
buttonColorHighlighted = (100,100,100)

menufont = pygame.font.SysFont('Corbel',75,True,False)

quitText = menufont.render('Quit' , True , textColorWhite) 
startText = menufont.render('Start!' , True , textColorWhite) 

pygame.display.flip()

runningMenu = True
runningGame = False

all_title_sprites = pygame.sprite.Group()
titleSprite = TitleSprite.TitleSprite()
all_title_sprites.add(titleSprite)

map = MapSprites.Map()
all_static_game_sprites = pygame.sprite.Group()
all_static_game_sprites.add(map)

while runningMenu:
    mouse = pygame.mouse.get_pos() 
    gameDisplay.blit(menuBackground,(0,0))
    all_title_sprites.update()
        
    
    clock.tick(60)
    all_title_sprites.draw(gameDisplay)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            runningMenu = False
        
    if buttons.menuQuitButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,quitText,ev) == False:
            runningMenu = False

    if buttons.menuStartButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,startText,ev) == True:
        runningGame = True
        while runningGame:
            

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    runningMenu = False
                    runningGame = False
                
                if ev.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    

                    if keys[pygame.K_ESCAPE]:
                        runningGame = False
                    if keys[pygame.K_w]:
                        actions["up"] = True
                    else:
                        actions["up"] = False
                    if keys[pygame.K_a]:
                        actions["left"] = True
                    else:
                        actions["left"] = False
                    if keys[pygame.K_d]:
                        actions["right"] = True
                    else:
                        actions["right"] = False
                    if keys[pygame.K_s]:
                        actions["down"] = True
                    else:
                        actions["down"] = False
                    if keys[pygame.K_q]:
                        actions["action1"] = True
                    else:
                        actions["action1"] = False
                    if keys[pygame.K_e]:
                        actions["action2"] = True
                    else:
                        actions["action2"] = False
                
            if 1 not in pygame.key.get_pressed():
                actions = {
                            "left": False,
                            "right": False,
                            "up": False,
                            "down": False,
                            "action1": False,
                            "action2": False,
                            "start": False
                        }
            map.update(actions)
            
            map.draw(gameDisplay)
            


            pygame.display.update() 
        
    
    

    pygame.display.update() 
