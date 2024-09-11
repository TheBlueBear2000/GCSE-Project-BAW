import pygame
import json

dir = "../" # When running from terminal of package
dir = "games/pythongames/BAW Versions/BAW v0.8/" # When running from IDE

with open((dir + "config.json"),"r") as file:
    cfgData = json.load(file)

def getAllData():
    return cfgData

def getDir():
    return dir

def getScreenSize():
    return cfgData["screenData"]["size"]