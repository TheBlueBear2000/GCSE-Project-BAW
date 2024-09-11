class run(object):
    def __init__(self,surface):
        import pygame
        import numpy
        import MapSprites

        # Sets starting locations of the script (First number is the offset, sothat the tiles properly allign, the second number is the number of tiles multiplied by 80, which is the size of the tile)
        coordX = 30 - 4240
        coordY = 60 - 3520
        
        rownum = 0
        tilenum = 0

        # Defines a new sprite group
        self.tilesGroup = pygame.sprite.Group()

        def read_csv(filename):
            # Uses a built in NumPy function to convert the CSV file to a 2d array
            numpy_array = numpy.loadtxt(filename, delimiter=",")
            tiles = numpy_array.tolist()
            return tiles

        # Locates the csv file
        objectSpawningArr = read_csv('assets/objects/squares/map_tiles.csv')

        # Scans the 2d array, spawning any sprites when told to
        for row in objectSpawningArr:
            coordX = 30 - 4240
            tilenum = 0
            for tile in row:
                if tile == 0:
                    t = MapSprites.Water(coordX,coordY,surface)
                    self.tilesGroup.add(t)
                    t.add

                elif tile == 6:
                    t = MapSprites.Bush(coordX,coordY,surface)
                    self.tilesGroup.add(t)
                    t.add

                elif tile == 7:
                    t = MapSprites.Tree(coordX,coordY,surface)
                    self.tilesGroup.add(t)
                    t.add

                ############################
                ## LOCALY DEPENDENT TILES ##
                ############################

                # Fences

                elif tile == 8:
                    up,down,left,right = False,False,False,False
                    if rownum > 0:
                        print(str(objectSpawningArr[int(rownum - 1)][int(tilenum)]))
                        if objectSpawningArr[int(rownum - 1)][int(tilenum)] == 8:
                            up = True
                    if rownum < len(objectSpawningArr) - 1:
                        if objectSpawningArr[int(rownum + 1)][int(tilenum)] == 8:
                            down = True
                    if tilenum > 0:
                        if objectSpawningArr[int(rownum)][int(tilenum - 1)] == 8:
                            left = True
                    if tilenum < len(objectSpawningArr[rownum]) - 1:
                        if objectSpawningArr[int(rownum)][int(tilenum + 1)] == 8:
                            right = True
                    
                    t = MapSprites.Fence(coordX,coordY,surface,up,down,left,right)
                    self.tilesGroup.add(t)
                    t.add

                # Walls

                elif tile == 9:
                    up,down,left,right = False,False,False,False
                    if rownum > 0:
                        print(str(objectSpawningArr[int(rownum - 1)][int(tilenum)]))
                        if objectSpawningArr[int(rownum - 1)][int(tilenum)] == 9:
                            up = True
                    if rownum < len(objectSpawningArr) - 1:
                        if objectSpawningArr[int(rownum + 1)][int(tilenum)] == 9:
                            down = True
                    if tilenum > 0:
                        if objectSpawningArr[int(rownum)][int(tilenum - 1)] == 9:
                            left = True
                    if tilenum < len(objectSpawningArr[rownum]) - 1:
                        if objectSpawningArr[int(rownum)][int(tilenum + 1)] == 9:
                            right = True
                    
                    t = MapSprites.Wall(coordX,coordY,surface,up,down,left,right)
                    self.tilesGroup.add(t)
                    t.add


                ###########
                ## ITEMS ##
                ###########
                elif tile == 10:
                    t = MapSprites.Raft(coordX,coordY,surface)
                    self.tilesGroup.add(t)
                    t.add
                elif tile == 12:
                    t = MapSprites.Bone(coordX,coordY,surface)
                    self.tilesGroup.add(t)
                    t.add
                elif tile == 13:
                    t = MapSprites.TennisBall(coordX,coordY,surface)
                    self.tilesGroup.add(t)
                    t.add
                elif tile == 14:
                    t = MapSprites.Chest(coordX,coordY,surface)
                    self.tilesGroup.add(t)
                    t.add

                coordX += 80
                tilenum += 1
            coordY += 80
            rownum += 1

    def getGroup(self):
        # Returns the group with all new sprites in
        return self.tilesGroup
