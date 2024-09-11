import pygame
import json
from pygame.constants import QUIT
from datetime import datetime
import data

dir = data.getDir()

pygame.init()

def menuLeaderboardButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,leaderboardText,ev):
    # If the mouse is down within the area of the button, return that the button has been pressed
    if ev.type == pygame.MOUSEBUTTONDOWN:
            if width/2-185 <= mouse[0] <= width/2+185 and height/2+80 <= mouse[1] <= height/2+160: 
                    return False

    # If the mouse is over the button, color the button, otherwise simply draw it
    if width/2-185 <= mouse[0] <= width/2+185 and height/2+80 <= mouse[1] <= height/2+160: 
        pygame.draw.rect(gameDisplay,buttonColorHighlighted,[width/2-185,height/2+90,370,80]) 
    else: 
        pygame.draw.rect(gameDisplay,buttonColor,[width/2-185,height/2+90,370,80]) 

    gameDisplay.blit(leaderboardText,(width/2-175,height/2+77)) 
    return True 

def menuQuitButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,quitText,ev):
    # If the mouse is down within the area of the button, return that the button has been pressed
    if ev.type == pygame.MOUSEBUTTONDOWN:
            if width/2-140 <= mouse[0] <= width/2+140 and height/2+210 <= mouse[1] <= height/2+290: 
                    return False

    # If the mouse is over the button, color the button, otherwise simply draw it
    if width/2-140 <= mouse[0] <= width/2+140 and height/2+210 <= mouse[1] <= height/2+290: 
        pygame.draw.rect(gameDisplay,buttonColorHighlighted,[width/2-140,height/2+220,280,80]) 
    else: 
        pygame.draw.rect(gameDisplay,buttonColor,[width/2-140,height/2+220,280,80]) 

    gameDisplay.blit(quitText,(width/2-110,height/2+207)) 
    return True

def menuStartButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,startText,ev):
    if (ev.type == pygame.MOUSEBUTTONDOWN) & (width/2-165 <= mouse[0] <= width/2+165 and height/2-40 <= mouse[1] <= height/2+40):
        return True

    if width/2-165 <= mouse[0] <= width/2+165 and height/2-40 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(gameDisplay,buttonColorHighlighted,[width/2-165,height/2-40,330,80]) 
    else: 
        pygame.draw.rect(gameDisplay,buttonColor,[width/2-165,height/2-40,330,80]) 

    gameDisplay.blit(startText,(width/2-155,height/2-53)) 
    return False


class saveGame(pygame.sprite.Sprite):
    def __init__(self,number):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.transform.scale(pygame.image.load(dir + "assets/gui/savegame_card.png"),(600,450)),
                        pygame.transform.scale(pygame.image.load(dir + "assets/gui/savegame_play.png"),(600,450)),
                        pygame.transform.scale(pygame.image.load(dir + "assets/gui/savegame_editname.png"),(600,450)),
                        pygame.transform.scale(pygame.image.load(dir + "assets/gui/savegame_wipehover.png"),(600,450))]
        self.number = number
        
        self.image = self.images[0]
        
        self.rect = self.image.get_rect()

        self.data = self.getSave()

        self.score = self.data["playerdata"]["score"]

        print(self.data)
        self.name = self.data["name"]
        self.timeSaved = self.data["timeSaved"]

        self.normalFont = pygame.font.Font(dir + "assets/gui/fonts/normal.ttf", 22)
        self.largeFont = pygame.font.Font(dir + "assets/gui/fonts/normal.ttf", 100)

        self.text_box = pygame.transform.scale(pygame.image.load(dir + "assets/gui/text_box.png"),(1500,1000))
        self.tint = pygame.transform.scale(pygame.image.load(dir + "assets/gui/tint.png"),(1500,1000))

    def position(self,place):
        if place == 0:
            self.rect.center = (1500/4,1000/4)
        elif place == 1:
            self.rect.center = ((1500/4) * 3,1000/4)
        elif place == 2:
            self.rect.center = (1500/4,(1000/4) * 3)
        elif place == 3:
            self.rect.center = ((1500/4) * 3,(1000/4) * 3)

    def start(self,ev,display):
        mouse = pygame.mouse.get_pos() 
        self.data = self.getSave()
        self.name = self.data["name"]
        self.timeSaved = self.data["timeSaved"]

        if (self.rect.x <= mouse[0] <= self.rect.x + self.rect.width) and (self.rect.y <= mouse[1] <= self.rect.y + self.rect.height):
            self.image = self.images[1]
            if (self.rect.x + 45 <= mouse[0] <= self.rect.x + 300) and (self.rect.y + 360 <= mouse[1] <= self.rect.y + 405):
                self.image = self.images[2]
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    ## If player attempting to edit text ##
                    editingText = True
                    edit = ""

                    tick = 0

                    display.blit(self.tint,(0,0))

                    while editingText:

                        pygame.time.Clock().tick(60)


                        display.blit(self.text_box,(0,0))
                        editImg = self.largeFont.render(edit , True , (255,255,255))
                        imgRect = editImg.get_rect()
                        display.blit(editImg,((1500 - imgRect.width)/2, (1000 - imgRect.height)/2))

                        tick += 1
                        if tick < 20:
                            pygame.draw.rect(display,(255,255,255),((1500 + imgRect.width)/2 , (1000 - imgRect.height)/2, 10, imgRect.height))
                        if tick > 40:
                            tick = 0

                        for ev in pygame.event.get():
                            if ev.type == pygame.QUIT:
                                editingText = False
                            
                            elif ev.type == pygame.KEYDOWN:
                                keys = pygame.key.get_pressed()
                                if keys[pygame.K_RETURN]:
                                    if len(edit) > 0:
                                        self.name = edit
                                    editingText = False

                                elif keys[pygame.K_ESCAPE]:
                                    editingText = False

                                elif keys[pygame.K_BACKSPACE]:
                                    edit = edit[:-1]
                                
                                else:
                                    if len(edit) < 12:
                                        edit += ev.unicode

                        pygame.display.update()

                    data = self.getSave()
                    data["name"] = self.name
                    self.save(data)

                    return False

            elif (self.rect.x + 300 <= mouse[0] <= self.rect.x + 555) and (self.rect.y + 360 <= mouse[1] <= self.rect.y + 405):
                self.image = self.images[3]
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    data = {
                        "name": "Untitled Savegame",
                        "timeSaved": "Game Recently Wiped",
                        "playerdata":{
                            "inv": [["NULL", -1, -1]],
                            "score": 0,
                            "hasRaft": False,
                            "coordinates":[-4210,-3460],
                            "countdown":[5,0,0]
                        }
                    }
                    self.save(data)
                    return False
                return False



            
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                return True
            else:
                return False
            
        else:
            self.image = self.images[0]
            return False
    
    def draw(self,display):
        # Blit card image
        display.blit(self.image,self.rect)

        # Center and blit time text
        if self.image != self.images[3]:
            self.timeText = self.normalFont.render(self.timeSaved , True , (255,255,255))
            self.timetextrect = self.timeText.get_rect()
            self.timetextrect.center = (self.rect.x + self.rect.width/2 + 135, self.rect.y + self.rect.height/2 + 160)
            display.blit(self.timeText,self.timetextrect)
        
        else:
            self.timeText = self.normalFont.render("Wipe Savegame?" , True , (255,255,255))
            self.timetextrect = self.timeText.get_rect()
            self.timetextrect.center = (self.rect.x + self.rect.width/2 + 135, self.rect.y + self.rect.height/2 + 160)
            display.blit(self.timeText,self.timetextrect)

        # Center and blit name text
        self.nameText = self.normalFont.render(self.name , True , (255,255,255))
        self.nametextrect = self.nameText.get_rect()
        self.nametextrect.center = (self.rect.x + 165, self.rect.y + self.rect.height/2 + 160)
        display.blit(self.nameText,self.nametextrect)

    def getSave(self):
        with open(str(dir + "saves/savegame_" + str(self.number) + ".json"),"r") as file:
            obj = json.load(file)
            return obj
    
    def getSaveData(self):
        now = datetime.now()
        nowStr = now.strftime("%d/%m/%Y %H:%M")
        return {
            "name": self.name,
            "timeSaved": nowStr
        }
    
    def save(self,data):
        with open((dir + "saves/savegame_" + str(self.number) + ".json"),"w") as file:
            json.dump(data,file)
