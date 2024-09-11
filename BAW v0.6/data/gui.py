import pygame

class run(object):
    def __init__(self,savedData):
        self.largeFont = pygame.font.Font("assets/gui/fonts/normal.ttf", 125)
        self.countdownMin = savedData[0]
        self.countdownSec = savedData[1]
        self.countdownTick = savedData[2]
        self.textColorWhite = (255,255,255)
        self.textColorBlack = (0,0,0)
        
        
    def update(self,display,playerstats):
        ## TIMER ##
        if self.countdownSec < 10:
            self.timerStr = self.largeFont.render((str(self.countdownMin) + ":0" + str(self.countdownSec)) , True , self.textColorWhite)
        else:
            self.timerStr = self.largeFont.render((str(self.countdownMin) + ":" + str(self.countdownSec)) , True , self.textColorWhite)
        self.countdownTick += 1
        if self.countdownTick >= 20:
            self.countdownTick = 0
            self.countdownSec -= 1
            if self.countdownSec < 0:
                self.countdownSec = 59
                self.countdownMin -= 1

        display.blit(self.timerStr,(100,75))

        ## SCORE ##
        
        self.scoreStr = self.largeFont.render(("Score: " + str(playerstats["score"])), True , self.textColorWhite)

        display.blit(self.scoreStr,(800,75))

    def getTimer(self):
        return [self.countdownMin,self.countdownSec,self.countdownTick]

    def isTimerFinished(self):
        if self.countdownSec == 0:
            if self.countdownMin == 0:
                return True
            else:
                return False
        else:
            return False

    def finalScore(self,playerstats,display):
        self.scoreStr = self.largeFont.render(("Final Score is: " + str(playerstats["score"])), True , self.textColorWhite)

        self.score_image_rect = self.scoreStr.get_rect()
        self.score_image_rect.center = (1500/2,1000/2)
        display.blit(self.scoreStr,self.score_image_rect)


