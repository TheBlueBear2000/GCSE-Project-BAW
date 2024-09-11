import pygame
import sys
from pygame.constants import QUIT

pygame.init()

def menuQuitButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,quitText,ev):
    if ev.type == pygame.MOUSEBUTTONDOWN:
            if width/2-140 <= mouse[0] <= width/2+140 and height/2+80 <= mouse[1] <= height/2+160: 
                    return False

    if width/2-140 <= mouse[0] <= width/2+140 and height/2+80 <= mouse[1] <= height/2+160: 
        pygame.draw.rect(gameDisplay,buttonColorHighlighted,[width/2-140,height/2+90,280,80]) 
    else: 
        pygame.draw.rect(gameDisplay,buttonColor,[width/2-140,height/2+90,280,80]) 

    gameDisplay.blit(quitText,(width/2-82,height/2+80)) 
    return True

def menuStartButton(height,width,mouse,buttonColor,gameDisplay,buttonColorHighlighted,startText,ev):
    if (ev.type == pygame.MOUSEBUTTONDOWN) & (width/2-140 <= mouse[0] <= width/2+140 and height/2-40 <= mouse[1] <= height/2+40):
        return True

    if width/2-140 <= mouse[0] <= width/2+140 and height/2-40 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(gameDisplay,buttonColorHighlighted,[width/2-140,height/2-40,280,80]) 
    else: 
        pygame.draw.rect(gameDisplay,buttonColor,[width/2-140,height/2-40,280,80]) 

    gameDisplay.blit(startText,(width/2-100,height/2-53)) 
    return False
