import pygame
import sys
import buttons
from pygame.constants import QUIT
import TitleSprite
import threading
import MapSprites
import Player
import json



## INIT CONSTANTS ##
pygame.init()
clock = pygame.time.Clock()

width = 1500
height = 1000

menuBackground = pygame.image.load("assets/menu/background.png")

background_colour = (0,0,0)
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
    "start": False,
    "speed": 6,
    "sprint": False
}

collided = False

textColorWhite = (255,255,255)
textColorBlack = (0,0,0)

buttonColor = (50,50,50)
buttonColorHighlighted = (100,100,100)

normalFont = pygame.font.Font("assets/gui/fonts/normal.ttf", 75)
titleFont = pygame.font.Font("assets/gui/fonts/title.ttf", 100)

quitText = titleFont.render('Quit' , True , textColorWhite) 
startText = titleFont.render('Start!' , True , textColorWhite) 

# Build display window
pygame.display.flip()

# Set loop variables
runningMenu = True
runningGame = False

# Create sprites and group them
all_title_sprites = pygame.sprite.Group()
titleSprite = TitleSprite.TitleSprite()
all_title_sprites.add(titleSprite)

while runningMenu:
    # Get mouse position, update display and title sprites
    mouse = pygame.mouse.get_pos() 
    gameDisplay.blit(menuBackground,(0,0))
    all_title_sprites.update()
        
    # Sets tick speed and draws display
    clock.tick(60)
    all_title_sprites.draw(gameDisplay)

    # Detects quit
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            runningMenu = False
    
    # Runs buttons
    if buttons.menuQuitButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,quitText,ev) == False:
            runningMenu = False

    if buttons.menuStartButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,startText,ev) == True:
        ## INITS GAME ##
        runningGame = True
        map = MapSprites.Map()
        player = Player.Player()

        overlayImg = pygame.transform.scale(pygame.image.load("assets/gui/overlay.png"),(width,height))

        ####################
        ## MAIN GAME LOOP ##
        ####################
        while runningGame:
            # Sets background to bacl to prevent blit stacking on map edges
            gameDisplay.fill(background_colour)

            # Sets game tick speed and timer
            clock.tick(60)

            # Reset temporary variables

            actions["action1"] = False
            actions["action2"] = False

            
            # Scans events
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    # Quits game
                    runningMenu = False
                    runningGame = False
                
                
                if ev.type == pygame.KEYDOWN:
                    # IF A NEW KEY IS PRESSED (THIS WILL NOT PLAY IS A KEY IS SIMPLY HELD DOWN)
                    keys = pygame.key.get_pressed()
                    
                    # Scans all non moving keys
                    if keys[pygame.K_ESCAPE]:
                        runningGame = False
                    if keys[pygame.K_s]:
                        actions["down"] = True
                    if keys[pygame.K_a]:
                        actions["left"] = True
                    if keys[pygame.K_d]:
                        actions["right"] = True
                    if keys[pygame.K_w]:
                        actions["up"] = True
                    if keys[pygame.K_q]:
                        actions["action1"] = True
                    if keys[pygame.K_e]:
                        actions["action2"] = True
                    if keys[pygame.K_LSHIFT]:
                        actions["speed"] = 10
                        actions["sprint"] = True

                    # Checks for a collision before choosing if move is made


            
                if ev.type == pygame.KEYUP:
                    # PLAYS IF A KEY IS RELEASED, AND ONLY ONCE ON ITS RELEASE
                    # If a key is released, it rewrites itself from the "actions" dictionary
                    if ev.key == pygame.K_w:
                        actions["up"] = False
                    if ev.key == pygame.K_s:
                        actions["down"] = False
                    if ev.key == pygame.K_a:
                        actions["left"] = False
                    if ev.key == pygame.K_d:
                        actions["right"] = False
                    if ev.key == pygame.K_q:
                        actions["action1"] = False
                    if ev.key == pygame.K_e:
                        actions["action2"] = False
                    if ev.key == pygame.K_LSHIFT:
                        actions["speed"] = 6
                        actions["sprint"] = False
            
            
            ## UPDATES ALL SPRITES AND RUNS ALL SPRITE TICK FUNCTIONS
            map.update()
            map.movement(actions)
            player.update(actions)

            playerStats = player.getPlayerStats()
            

            ## DRAWS GAME SCREEN
            map.draw(gameDisplay)
            player.draw(gameDisplay)




            pygame.display.update() 
            
        
    
    

    pygame.display.update() 
