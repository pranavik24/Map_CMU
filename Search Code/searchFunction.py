import imageio.v3 as iio
import numpy as np
import io
from PIL import Image

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

mapGrid=iio.imread("filledin_cmu_pixelated.png")


numRows=135
numCols=173

costMapGrid= [[0 for i in range(numCols)] for j in range(numRows)]

colourDict={"#0001ff": "GHC",
           "#0002ff": "NSH",
            "#0003ff": "WEH",
            "#0004ff": "SC",
            "#0005ff": "HH",
            "#0006ff": "SH",
            "#0007ff": "ANSYS",
            "#0008ff": "PH",
            "#0009ff": "BH",
            "#0010ff": "HUNT",
            "#0011ff": "CFA",
            "#0012ff": "POS",
            "#0013ff": "HOA",
            "#0014ff": "MM",
            "#0015ff": "CUC",
            "#0016ff": "PCA",
            "#0017ff": "TEP",
            "#0018ff": "MI",
            "#0019ff": "DH",
            "#ffff01": "STE",
            "#ffff02": "MOE",
            "#ffff03": "MOR",
            "#ffff04": "MUD",
            "#ffff05": "WWG",
            "#ffff06": "RES",
            "#ffff07": "DON",
            "#ffff08": "HILL",
            "#01ffff": "STACKD",
            "#02ffff": "TRUE BURG",
            "#03ffff": "ENTROPY",
            "#04ffff": "ABP",
            "#05ffff": "TASTE OF INDIA",
            "#06ffff": "BUILD PIZZA",
            "#07ffff": "FORBES SUB",
            "#08ffff": "HUNAN",
            "#09ffff": "REV",
            "#11ffff": "DE FER",
            "#12ffff": "SCHATZ",
            "#13ffff": "EXCHANGE",
            "#14ffff": "EDGE",
            "#15ffff": "WILD BLUE",
            "#ff0000": 2,
            "#000000": 0,
            "#ffffff": 1}

for row in range(numRows):
    for col in range(numCols):
        pixel=mapGrid[row][col]
        red=pixel[0]
        green=pixel[1]
        blue=pixel[2]
        colourHex=rgb_to_hex(red,green,blue)
        costMapGrid[row][col]=colourDict[colourHex]

right = (0,1)
left= (0,-1)
down= (1,0)
up= (-1,0)
upright=(-1,1)
upleft=(-1,-1)
downright=(1,1)
downleft=(1,-1)

def canMove(row,col,dRow,dCol):
     if (row+dRow>-1 and col+dCol>-1 and 
         row+dRow<numRows and col+dCol < numCols and costMapGrid[row+dRow][col+dCol]!= 0):
          return True
     return False

def moveCost(row,col,dRow,dCol):
     if costMapGrid[row+dRow][col+dCol]== 0:
          cost=2
     else:   
          cost=1
     return cost

def heuristic(startRow,startCol,endRow,endCol):
     return max(abs(endRow-startRow), abs(endCol-startCol))

def closestMeal(currRow, currCol):
    mealList=["STACKD","TRUE BURG","ENTROPY","ABP",
              "TASTE OF INDIA","BUILD PIZZA","FORBES SUB",
              "HUNAN","REV","DE FER","SCHATZ","EXCHANGE","EDGE","WILD BLUE"]
    leastRest=None
    leastDist=-1
    for restaurant in mealList:
        row=find(restaurant)[0][0]
        col=find(restaurant)[0][1]
        if leastDist==-1:
            leastDist=heuristic(row,col,currRow,currCol)
            leastRest=restaurant
        elif heuristic(row,col,currRow,currCol)<leastDist:
            leastDist=heuristic(row,col,currRow,currCol)
            leastRest=restaurant
    return leastRest
        



def getNeighbors(cost, node):
    possibleLocations=[]
    possibleMoves=[right,left,up,down,upright,upleft,downright,downleft]
    for move in possibleMoves:
        if canMove(node[0],node[1],move[0],move[1]):
            possibleLocations.append((cost+moveCost(node[0],node[1],move[0],move[1]),
                                [node[0]+move[0], node[1]+move[1]]))
    return possibleLocations

def find(node):
    locnList=[]
    for row in range(numRows):
        for col in range(numCols):
            if costMapGrid[row][col]==node:
                locnList.append([row,col])
    return locnList

def addToFrontier(frontier,cost,path):
    for i in range(len(frontier)):
        oldCost=frontier[i][0]
        if cost<oldCost:
            frontier.insert(i, (cost, path))
            return
    frontier.append((cost,path))

def doSearch(startNode, stopNode):
    startLocn=find(startNode)
    stopLocn=find(stopNode)
    frontier=[(0,[startLocn[0]])] #tuple (cost, list of row-col tuples of each movement)
    explored=set()
    while frontier:
        movementCost, path = frontier.pop(0)
        if path[-1] in stopLocn:
            return path
        for newCost, newLocation in getNeighbors(movementCost, path[-1]):
            if tuple(newLocation) not in explored:
                explored.add(tuple(newLocation))
                cost=movementCost+newCost
                totalPath=path + [newLocation]
                addToFrontier(frontier,cost,totalPath)

           

# path=doSearch(startNode, stopNode)

# pixelGrid= iio.imread("cmu_map_small.png", pilmode="RGB")
# for locn in path:
#     row=locn[0]
#     col=locn[1]
#     pixelGrid[row][col]=[63,255,63]


# img = Image.fromarray(pixelGrid.astype(np.uint8) * 255, mode='RGB')
# img = img.save("route.png")