from PIL import Image
import csv
import os
import numpy

tileWidth = 8

mapSizeW,mapSizeH = 1000,800

coordX, coordY = 0,0

x, y = 0, 0

images = []
images.append(Image.open('grass.png'))
images.append(Image.open('dirt.png'))
images.append(Image.open('mud.png'))
images.append(Image.open('rock.png'))
images.append(Image.open('sand.png'))
images.append(Image.open('snow.png'))
images.append(Image.open('tree.png'))
images.append(Image.open('water_1.png'))

final = Image.new('RGBA', (mapSizeW,mapSizeH), (255, 255, 255, 255))

def read_csv(filename):
    numpy_array = numpy.loadtxt(filename, delimiter=",")
    map = numpy_array.tolist()
    return map

    #map = []
    #with open(os.path.join(filename)) as data:
    #        data = csv.reader(data, delimiter= ",")
    #        for row in data:
    #            map.append(list(row))
    #return map

mapData = read_csv('map_image.csv')

for row in mapData:
    coordX = 0
    for tile in row:
        if tile == 0:
            final.paste(images[7],(coordX,coordY))
        elif tile == 1:
            final.paste(images[0],(coordX,coordY))
        elif tile == 2:
            final.paste(images[3],(coordX,coordY))
        elif tile == 3:
            final.paste(images[1],(coordX,coordY))
        elif tile == 4:
            final.paste(images[2],(coordX,coordY))
        elif tile == 5:
            final.paste(images[4],(coordX,coordY))
        elif tile == 7:
            final.paste(images[6],(coordX,coordY))
        elif tile == 11:
            final.paste(images[5],(coordX,coordY))
        
        coordX += 8

    coordY += 8

final.save('out.png')