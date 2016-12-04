from math import *

numTilings = 4
numTiles = 81
    
def tilecode(in1,in2):
    # write your tilecoder here (5 lines or so)
    in1 += 1.2
    in2 += 0.07
    offsetX = (1.7/8)/numTilings
    offsetY = (0.14/8)/numTilings
    tileIndices = [-1]*numTilings

    for tiling in range (numTilings) :
    	
        x = floor((in1)/(1.7)*8)
    	y = floor((in2 )/(0.14)*8)
    	tileIndices[tiling] = int(x + y*9 + 81*tiling)
        in1 += offsetX
        in2 += offsetY

    return tileIndices


    	
def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

#printTileCoderIndices(0.1,0.06)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)
    
