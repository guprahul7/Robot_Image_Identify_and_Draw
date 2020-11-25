from Myro import *
import math
#init("sim")

def changesize():
    F = 1
    newx = int(X/F)
    newy = int(Y/F)
    newPic = makePicture(newx, newy)
    for x in range(1,newx):
        for y in range(1,newy):
            setPixel(newPic, x, y, getPixel(myPic, x*F, y*F))
    return newPic
    
def getpix(img,x,y):
	pixel = getPixel(img, x, y) 
	r,g,b=getRGB(pixel)
	return (r+g+b)/3
 
SX= [[-1,0,1],[-2,0,2],[-1,0,1]]

SY = [[1,2,1],[0,0,0],[-1,-2,-1]]
		   
def sobel():
    for x in range(1,X-1):
        for y in range(1,Y-1):
            #print (SX[0][0],getpix(newPic,x-1,y-1)," ",SX[0][1],getpix(newPic,x,y-1)," ",SX[0][2], getpix(newPic,x+1,y-1)," ",SX[1][0], getpix(newPic,x-1,y)," ",SX[1][1],getpix(newPic,x,y)," ",SX[1][2],getpix(newPic,x+1,y)," ",SX[2][0], getpix(newPic,x-1,y+1), " ",SX[2][1], getpix(newPic,x,y+1)," ",SX[2][2],getpix(newPic,x+1,y+1))
            px = (SX[0][0] * getpix(newPic,x-1,y-1)) + (SX[0][1] * getpix(newPic,x,y-1)) + (SX[0][2] * getpix(newPic,x+1,y-1)) + (SX[1][0] * getpix(newPic,x-1,y))   + (SX[1][1] * getpix(newPic,x,y))   + (SX[1][2] * getpix(newPic,x+1,y)) + (SX[2][0] * getpix(newPic,x-1,y+1)) + (SX[2][1] * getpix(newPic,x,y+1)) + (SX[2][2] * getpix(newPic,x+1,y+1))
            py = (SY[0][0] * getpix(newPic,x-1,y-1)) + (SY[0][1] * getpix(newPic,x,y-1)) + (SY[0][2] * getpix(newPic,x+1,y-1)) + (SY[1][0] * getpix(newPic,x-1,y))   + (SY[1][1] * getpix(newPic,x,y)) + (SY[1][2] * getpix(newPic,x+1,y)) + (SY[2][0] * getpix(newPic,x-1,y+1)) + (SY[2][1] * getpix(newPic,x,y+1)) + (SY[2][2] * getpix(newPic,x+1,y+1))
            #print(px,py)
            val = math.sqrt((px * px) + (py * py))
            #print("Pixel:", x, y, px,py,val)
            if val > 80:
                setColor(getPixel(copyPic,x,y), makeColor(0,0,0))
            else:
                setColor(getPixel(copyPic,x,y), makeColor(255, 255, 255))
	
myPic = makePicture("Hexagon.jpg")
show(myPic)
X = getWidth(myPic)
Y = getHeight(myPic)
newPic=changesize()
global copyPic
copyPic = copyPicture(newPic)
X = getWidth(newPic)
Y = getHeight(newPic)
sobel()
X = getWidth(copyPic)
Y = getHeight(copyPic)
show(copyPic, "After")
