import pygame
import json


dir = "../" # When running from terminal of package
dir = "BAW v0.7/" # When running from IDE

with open((dir + "config.json"),"r") as file:
    cfgData = json.load(file)


def getAllData():
    return cfgData

def getDir():
    dir = "../" # When running from terminal of package
    dir = "BAW v0.7/" # When running from IDE
    return dir

def getScreenSize():
    return cfgData["screenData"]["size"]