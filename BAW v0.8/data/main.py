import pygame
import buttons
from pygame.constants import QUIT
import TitleSprite
import MapSprites
import tile_generation
import Player
import gui
import os
import sys
import data

# Finds directory path #
dir = data.getDir()

## INIT CONSTANTS ##
pygame.init()
clock = pygame.time.Clock()

clockspeed = data.getAllData()["screenData"]["clockSpeed"]

width = data.getAllData()["screenData"]["size"][0]
height = data.getAllData()["screenData"]["size"][1]

menuBackground = pygame.transform.scale(pygame.image.load(dir + "assets/menu/background.png"),(1500,1000))

background_colour = (0,0,0)
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bonzo's Adventures in Wonderland")
gameDisplay.fill(background_colour)
gameDisplay.blit(menuBackground,(0,0))


textColorWhite = (255,255,255)
textColorBlack = (0,0,0)

buttonColor = (50,50,50)
buttonColorHighlighted = (100,100,100)

normalFont = pygame.font.Font(dir + "assets/gui/fonts/normal.ttf", 75)
titleFont = pygame.font.Font(dir + "assets/gui/fonts/title.ttf", 100)

leaderboardText = titleFont.render('Scores' , True , textColorWhite) 
quitText = titleFont.render('Quit' , True , textColorWhite) 
startText = titleFont.render('Start!' , True , textColorWhite) 

# Build display window
pygame.display.flip()

# Set loop variables
runningMenu = True
runningSaveSelect = True
runningGame = False
runningGameOver = False
runningLeaderboard = False



# Create sprites and group them
all_title_sprites = pygame.sprite.Group()
titleSprite = TitleSprite.TitleSprite()
all_title_sprites.add(titleSprite)

# Creates all savegame buttons
savegame0 = buttons.saveGame(0)
savegame1 = buttons.saveGame(1)
savegame2 = buttons.saveGame(2)
savegame3 = buttons.saveGame(3)
savegames = pygame.sprite.Group()
savegamesByScore = pygame.sprite.Group()
savegames.add(savegame0,savegame1,savegame2,savegame3)

scores = []

for save in savegames:
    scores.append(save.score)
scores = sorted(scores)
scores.reverse()

for i in range(len(scores)):
    for save in savegames:
        if save.score == scores[i]:
            savegamesByScore.add(save)

savesIndex = 0
for save in savegamesByScore:
    save.position(savesIndex)
    savesIndex += 1

while runningMenu:
    # Get mouse position, update display and title sprites
    mouse = pygame.mouse.get_pos() 
    gameDisplay.blit(menuBackground,(0,0))
    all_title_sprites.update()
        
    # Sets tick speed and draws display
    clock.tick(clockspeed)
    all_title_sprites.draw(gameDisplay)

    # Detects quit
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            runningMenu = False
    
    # Runs buttons
    if buttons.menuQuitButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,quitText,ev) == False:
        runningMenu = False

    if buttons.menuLeaderboardButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,leaderboardText,ev) == False:
        print("runningButton")
        savegameNamesToScores = []
        for savegame in savegames:
            savegameNamesToScores.append([savegame.getSave()["playerdata"]["score"], savegame.getSave()["name"]])
        savegameNamesToScores.sort(reverse=True)
        runningLeaderboard = True

        while runningLeaderboard:
            #print("runningStart")
            gameDisplay.blit(menuBackground,(0,0))

            textImage = pygame.font.Font(dir + "assets/gui/fonts/title.ttf", 150).render("Scores" , True , textColorBlack)
            textRect = textImage.get_rect()
            gameDisplay.blit(textImage,(width/2 - textRect.width/2 + 5, 215)) 

            textImage = pygame.font.Font(dir + "assets/gui/fonts/title.ttf", 150).render("Scores" , True , textColorWhite)
            textRect = textImage.get_rect()
            gameDisplay.blit(textImage,(width/2 - textRect.width/2, 210)) 



            for i in range(len(savegameNamesToScores)):
                textImage = pygame.font.Font(dir + "assets/gui/fonts/title.ttf", 100).render((savegameNamesToScores[i][1] + " : " + str(savegameNamesToScores[i][0])) , True , textColorBlack)
                textRect = textImage.get_rect()
                gameDisplay.blit(textImage,(width/2 - textRect.width/2 + 5, 355 + i * 90)) 

            for i in range(len(savegameNamesToScores)):
                textImage = pygame.font.Font(dir + "assets/gui/fonts/title.ttf", 100).render((savegameNamesToScores[i][1] + " : " + str(savegameNamesToScores[i][0])) , True , textColorWhite)
                textRect = textImage.get_rect()
                gameDisplay.blit(textImage,(width/2 - textRect.width/2, 350 + i * 90)) 


            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    runningMenu = False
                    runningSaveSelect = False
                    runningLeaderboard = False
                if ev.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        runningLeaderboard = False
            #print("runningEnd")
            pygame.display.update()




    if buttons.menuStartButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,startText,ev) == True:
        runningSaveSelect = True
        while runningSaveSelect:
            clock.tick(clockspeed)
            gameDisplay.blit(menuBackground,(0,0))

            # Detects quit
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    runningMenu = False
                    runningSaveSelect = False

                if ev.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        runningSaveSelect = False

            
                for savegame in savegames:    
                    if savegame.start(ev,gameDisplay):

                        actions = {
                            "left": False,
                            "right": False,
                            "up": False,
                            "down": False,
                            "action1": False,
                            "action2": False,
                            "start": False,
                            "speed": 13,
                            "sprint": False
                        }

                        ## GETS SAVEGAME DATA ##
                        data = savegame.getSave()
                        savedPlayerData = data["playerdata"]
                    
                        ## INITS GAME ##
                        runningGame = True

                        overlay_gui = gui.run(savedPlayerData["countdown"])
                        map = MapSprites.Map(savedPlayerData["coordinates"])
                        player = Player.Player(savedPlayerData)


                        generation = tile_generation.run(gameDisplay,savedPlayerData)
                        all_static_game_sprites = generation.getGroups()[0]
                        animatable_game_sprites = generation.getGroups()[1]
                        updatable_game_sprites = generation.getGroups()[2]

                        map_sprites = pygame.sprite.Group()
                        map_sprites.add(all_static_game_sprites)
                        map_sprites.add(map)

                        overlayImg = pygame.transform.scale(pygame.image.load(dir + "assets/gui/overlay.png"),(width,height))

                        ####################
                        ## MAIN GAME LOOP ##
                        ####################
                        while runningGame:
                            

                            # Sets background to black to prevent blit stacking on map edges (see version 1.0, its hilarious)
                            gameDisplay.fill(background_colour)

                            # Sets game tick speed and timer
                            clock.tick(clockspeed)

                            # Reset temporary button variables

                            actions["action1"] = False
                            actions["action2"] = False

                            
                            # Scans events
                            for ev in pygame.event.get():
                                if ev.type == pygame.QUIT:
                                    # Quits game
                                    runningMenu = False
                                    runningSaveSelect = False
                                    runningGame = False
                                
                                if ev.type == pygame.KEYDOWN:
                                    # IF A NEW KEY IS PRESSED (THIS WILL NOT PLAY IS A KEY IS SIMPLY HELD DOWN)
                                    keys = pygame.key.get_pressed()
                                    
                                    # Scans all non moving keys
                                    if keys[pygame.K_ESCAPE]:
                                        ## SAVES ALL DATA ##

                                        if len(player.getPlayerStats()["inv"]) < 1:
                                            invArr = [["NULL", -1, -1]]
                                        else:
                                            invArr = player.getPlayerStats()["inv"]
                                        saveData = {
                                            "name": savegame.getSaveData()["name"],
                                            "timeSaved": savegame.getSaveData()["timeSaved"],
                                            "playerdata": {"inv": invArr,
                                                            "score": player.getPlayerStats()["score"],
                                                            "hasRaft":player.getPlayerStats()["hasRaft"],
                                                            "coordinates":map.getSavedData(),
                                                            "countdown":overlay_gui.getTimer()
                                                            }
                                        }
                                        savegame.save(saveData)

                                        runningSaveSelect = False
                                        runningGame = False



                                    if keys[pygame.K_s]:
                                        actions["down"] = True
                                        player.update(actions,map_sprites,force=True)
                                    if keys[pygame.K_a]:
                                        actions["left"] = True
                                        player.update(actions,map_sprites,force=True)
                                    if keys[pygame.K_d]:
                                        actions["right"] = True
                                        player.update(actions,map_sprites,force=True)
                                    if keys[pygame.K_w]:
                                        actions["up"] = True
                                        player.update(actions,map_sprites,force=True)
                                    if keys[pygame.K_q]:
                                        actions["action1"] = True
                                    if keys[pygame.K_e]:
                                        actions["action2"] = True
                                    if keys[pygame.K_LSHIFT]:
                                        actions["speed"] = 23

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
                                        actions["speed"] = 13
                            
                            
                            ## UPDATES ALL SPRITES AND RUNS ALL SPRITE TICK FUNCTIONS
                            map.update()
                            map.movement(actions,map_sprites)
                            updatable_game_sprites.update(actions,player)
                            for sprite in all_static_game_sprites:
                                sprite.movement(actions,map_sprites,player)
                            for sprite in animatable_game_sprites:
                                sprite.animations()
                            player.update(actions,map_sprites)

                            playerStats = player.getPlayerStats()
                            

                            ## DRAWS GAME SCREEN
                            map.draw(gameDisplay)
                            all_static_game_sprites.draw(gameDisplay)
                            player.draw(gameDisplay)



                            ## DRAWS STATS OVERLAY
                            gameDisplay.blit(overlayImg,(0,0))
                            overlay_gui.update(gameDisplay,playerStats)

                            timer = overlay_gui.getTimer()

                            if overlay_gui.isTimerFinished():
                                runningGameOver = True

                                if len(player.getPlayerStats()["inv"]) < 1:
                                    invArr = [["NULL", -1, -1]]
                                else:
                                    invArr = player.getPlayerStats()["inv"]
                                saveData = {
                                    "name": savegame.getSaveData()["name"],
                                    "timeSaved": savegame.getSaveData()["timeSaved"],
                                    "playerdata": {"inv": invArr,
                                                    "score": player.getPlayerStats()["score"],
                                                    "hasRaft":player.getPlayerStats()["hasRaft"],
                                                    "coordinates":map.getSavedData(),
                                                    "countdown":overlay_gui.getTimer()
                                                    }
                                            }
                                savegame.save(saveData)
                                while runningGameOver:
                                    
                                    clock.tick(clockspeed)
                                    gameDisplay.blit(menuBackground,(0,0))
                                    overlay_gui.finalScore(playerStats,gameDisplay)

                                    for ev in pygame.event.get():
                                        if ev.type == pygame.QUIT:
                                            # Quits game
                                            runningMenu = False
                                            runningSaveSelect = False
                                            runningGame = False
                                            runningGameOver = False

                                        if ev.type == pygame.KEYDOWN:

                                            keys = pygame.key.get_pressed()
                                            if keys[pygame.K_ESCAPE]:
                                                runningGame = False
                                                runningGameOver = False
                                                
                                    pygame.display.update() 

                            screenshot = pygame.Surface((1179, 550))
                            screenshot.blit(gameDisplay,(-411, -250))
                            pygame.image.save(screenshot,dir + "assets/savegame_icons/savegame_icon_" + str(savegame.number) + ".png")

                            pygame.display.update() 

            for savegame in savegames:
                savegame.draw(gameDisplay)

            pygame.display.update()
        
    
    

    pygame.display.update() 
