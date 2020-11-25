from Myro import *
import math
init("sim")

class num:
    def __init__ (self,c):
        self.c=c

def changesize():
    F = 8
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

def blur():
    for x in range(1,X-1):
        for y in range(1,Y-1):
            n1 = getpix(newPic,x, y)
            n2 = getpix(newPic,x, y-1)
            n3 = getpix(newPic,x-1, y)
            n4 = getpix(newPic,x+1, y)
            n5 = getpix(newPic,x, y+1)
            v = (n1+n2+n3+n4+n5)/5
            setColor(getPixel(copyPic,x,y), makeColor(v,v,v))
            #print (v)
           
def sobel(img):
    for x in range(1,X-1):
        for y in range(1,Y-1):
            #print (SX[0][0],getpix(newPic,x-1,y-1)," ",SX[0][1],getpix(newPic,x,y-1)," ",SX[0][2], getpix(newPic,x+1,y-1)," ",SX[1][0], getpix(newPic,x-1,y)," ",SX[1][1],getpix(newPic,x,y)," ",SX[1][2],getpix(newPic,x+1,y)," ",SX[2][0], getpix(newPic,x-1,y+1), " ",SX[2][1], getpix(newPic,x,y+1)," ",SX[2][2],getpix(newPic,x+1,y+1))
            px = (SX[0][0] * getpix(img,x-1,y-1)) + (SX[0][1] * getpix(img,x,y-1)) + (SX[0][2] * getpix(img,x+1,y-1)) + (SX[1][0] * getpix(img,x-1,y))   + (SX[1][1] * getpix(img,x,y))   + (SX[1][2] * getpix(img,x+1,y)) + (SX[2][0] * getpix(img,x-1,y+1)) + (SX[2][1] * getpix(img,x,y+1)) + (SX[2][2] * getpix(img,x+1,y+1))
            py = (SY[0][0] * getpix(img,x-1,y-1)) + (SY[0][1] * getpix(img,x,y-1)) + (SY[0][2] * getpix(img,x+1,y-1)) + (SY[1][0] * getpix(img,x-1,y))   + (SY[1][1] * getpix(img,x,y)) + (SY[1][2] * getpix(img,x+1,y)) + (SY[2][0] * getpix(img,x-1,y+1)) + (SY[2][1] * getpix(img,x,y+1)) + (SY[2][2] * getpix(img,x+1,y+1))
            #print(px,py)
            val = math.sqrt((px * px) + (py * py))
            #print("Pixel:", x, y, px,py,val)
            if val > 500:
                setColor(getPixel(copyPic,x,y), makeColor(0,0,0))
            else:
                setColor(getPixel(copyPic,x,y), makeColor(255, 255, 255))

def startpoint():
    global m,n
    for m in range(0,X):
        n=Y
        while (n>0):
            if (getpix(copyPic,m,n)==0):
                break
            n-=1
        if (getpix(copyPic,m,n)==0 or getpix(copyPic,m,n+1)==0):
            break

def changepix(x,y):
    #print(x,y,getpix(copyPic,x,y))
    if (getpix(copyPic,x,y)>100):
        return 0
    else:
        count.c+=1
       # print(count.c)
        return 1

def getmin(s):
    dict={0:abs(s-0),30:abs(s-30),45:abs(s-45),60:abs(s-60),90:abs(s-90)}
    return min(dict, key=dict.get)
         
def FW():
    forward(0.4,0.3)
    
def R30():
    turnRight(2,0.3)
    FW()

def R45():
    turnRight(2,0.6)
    FW()
    
def R60():
    turnRight(2,0.9)
    FW()
    
def R90():
    turnRight(2,1.2)
    FW()

def L90():
    turnLeft(2,1.2)
    FW()
    
    
def North(x,y,deg):
    setColor(getPixel(linePic,x,y), makeColor(255,0,0))
    show(linePic)
    count.c=0
    s = changepix(x,y-1)*0+changepix(x,y-2)*0+changepix(x+1,y-2)*30+changepix(x+1,y-1)*45+changepix(x+2,y-2)*45+changepix(x+2,y-1)*60+changepix(x+1,y)*90+changepix(x+2,y)*90
    if (count.c==0):
        if (changepix(x-1,y-2)==1):
            FW()
            North(x-1,y-2,deg)    
        elif (changepix(x+1,y-1)==1):
            FW()
            North(x+1,y-2,deg)
        elif (changepix(x-1,y)==1):
            L90()
            West(x-1,y,deg)
    s = s/count.c
    print(x,y,deg,s)
    if (s>=deg):
        s=getmin(s)
        deg=s 
        if (s==30):
            R30()
            NE(x+1,y-1,deg) 
        elif (s==45):
            R45()
            NE(x+1,y-1,deg)
        elif (s==60):
            R60()
            NE(x+1,y-1,deg)
        elif (s==90):
            R90()
            East(x+1,y,deg)
        stop()
    else:
        FW()    
        if (changepix(x,y-1)==1):
            North(x,y-1,deg)
        elif (changepix(x-1,y-2)==1):
            North(x-1,y-2,deg)
        elif (changepix(x+1,y-2)==1):
            North(x+1,y-2,deg)
        elif (changepix(x+1,y-1)==1):
            North(x+1,y-2,deg)
        elif (changepix(x-1,y-1)==1):
            North(x-1,y-1,deg)
            
def East(x,y,deg):
    setColor(getPixel(linePic,x,y), makeColor(255,0,0))
    show(linePic)
    count.c=0
    s = changepix(x+1,y)*0+changepix(x+2,y)*0+changepix(x+2,y+1)*30+changepix(x+1,y+1)*45+changepix(x+2,y+2)*45+changepix(x+1,y+2)*60+changepix(x,y+1)*90+changepix(x,y+2)*90
    if (count.c==0):
        if (changepix(x+2,y-1)==1):
            FW()
            East(x+2,y-1,deg)   
        elif (changepix(x+1,y+1)==1):
            FW()
            East(x+1,y+1,deg) 
        elif (changepix(x,y-1)==1):
            L90()
            North(x,y-1,deg)
    s = s/count.c
    print(x,y,deg,s)
    if (s>=deg):
        s=getmin(s)
        deg=s
        if (s==30):
            R30()
            SE(x+1,y+1,deg)
        elif (s==45):
            R45()
            SE(x+1,y+1,deg)
        elif (s==60):
            R60()
            SE(x+1,y+1,deg)
        elif (s==90):
            R90()
            South(x,y+1,deg)
        stop()
    else: 
        FW()
        if (changepix(x+1,y)==1):
            East(x+1,y,deg)
        elif (changepix(x+2,y-1)==1):
            East(x+2,y-1,deg)
        elif (changepix(x+2,y+1)==1):
            East(x+2,y+1,deg)
        elif (changepix(x+1,y+1)==1):
            East(x+1,y+1,deg)
        elif (changepix(x+1,y-1)==1):
            East(x+1,y-1,deg)
                

def South(x,y,deg): 
    setColor(getPixel(linePic,x,y), makeColor(255,0,0))
    show(linePic)
    count.c=0
    s = changepix(x,y+1)*0+changepix(x,y+2)*0+changepix(x-1,y+2)*30+changepix(x-1,y+1)*45+changepix(x-2,y+2)*45+changepix(x-2,y+1)*60+changepix(x-1,y)*90+changepix(x-2,y)*90
    if (count.c==0):
        if (changepix(x+1,y+2)==1):
            FW()
            South(x+1,y+2,deg)
        elif (changepix(x-1,y+1)==1):
            FW()
            South(x-1,y+1,deg)
        elif (changepix(x+1,y)==1):
            L90()
            East(x+1,y,deg)
    s = s/count.c
    print(x,y,deg,s)
    if (s>=deg):
        s=getmin(s)
        deg=s
        if (s==30):
            R30()
            SW(x-1,y+1,deg)
        elif (s==45):
            R45()
            SW(x-1,y+1,deg) 
        elif (s==60):
            R60()
            SW(x-1,y+1,deg)
        elif (s==90):
            R90()
            West(x-1,y,deg)
        stop()
    else :
        FW()
        if (changepix(x,y+1)==1):
            South(x,y+1,deg)
        elif (changepix(x+1,y+2)==1):
            South(x+1,y+2,deg)
        elif (changepix(x-1,y+2)==1):
            South(x-1,y+2,deg)
        elif (changepix(x-1,y+1)==1):
            South(x-1,y+1,deg)
        elif (changepix(x+1,y+1)==1):
            South(x+1,y+1,deg)
        
def West(x,y,deg):
    setColor(getPixel(linePic,x,y), makeColor(255,0,0))
    show(linePic)
    count.c=0
    s = changepix(x-1,y)*0+changepix(x-2,y)*0+changepix(x-2,y-1)*30+changepix(x-1,y-1)*45+changepix(x-2,y-2)*45+changepix(x-1,y-2)*60+changepix(x,y-1)*90+changepix(x,y-2)*90
    if (count.c==0):
        if (changepix(x-2,y+1)==1):
            FW()
            West(x-2,y+1,deg)
        elif (changepix(x-1,y-1)==1):
            FW()
            West(x-1,y-1,deg)
        elif (changepix(x,y+1)==1):
            L90()
            South(x,y+1,deg)
    s = s/count.c
    print(x,y,deg,s)
    if (s>=deg):
        s=getmin(s)
        deg=s
        if (s==30):
            R30()
            NW(x-1,y-1,deg)
        elif (s==45):
            R45()
            NW(x-1,y-1,deg)
        elif (s==60):
            R60()
            NW(x-1,y-1,deg)
        elif (s==0):
            R90()
            North(x,y-1,deg)
        stop()
    else:
        FW()
        if (changepix(x-1,y)==1):
            West(x-1,y,deg)
        elif (changepix(x-2,y+1)==1):
            West(x-2,y+1,deg)
        elif (changepix(x-2,y-1)==1):
            West(x-2,y-1,deg)
        elif (changepix(x-1,y-1)==1):
            West(x-1,y-1,deg)
        elif (changepix(x-1,y+1)==1):
            West(x-1,y+1,deg)
                       

def NE(x,y,deg):
    setColor(getPixel(linePic,x,y), makeColor(255,0,0))
    show(linePic)
    count.c=0
    s = changepix(x+1,y-1)*0+changepix(x+2,y-2)*0+changepix(x+2,y-1)*30+changepix(x+1,y)*45+changepix(x+2,y)*45+changepix(x+2,y+1)*60+changepix(x+1,y+1)*90+changepix(x+2,y+2)*90
    if (count.c==0):
        if (changepix(x+1,y-2)==1):
            FW()
            NE(x+1,y-2,deg)
        elif (changepix(x+1,y)==1):
            FW()
            NE(x+1,y,deg)
        elif (changepix(x-1,y-1)==1):
            L90()
            NW(x-1,y-1,deg)
    s = s/count.c
    if (s>=deg):
        s=getmin(s)
        deg=s
        if (s==30):
            R30()
            East(x+1,y,deg)
        elif (s==45):
            R45()
            East(x+1,y,deg)
        elif (s==60):
            R60()
            East(x+1,y,deg)
        elif (s==90):
            R90()
            SE(x+1,y+1,deg)
        stop()
    else:
        FW()
        if (changepix(x+1,y-1)==1):
            NE(x+1,y-1,deg)
        elif (changepix(x+1,y-2)==1):
            NE(x+1,y-2,deg)
        elif (changepix(x+2,y-1)==1):
            NE(x+2,y-1,deg)
        elif (changepix(x+1,y)==1):
            NE(x+1,y,deg)
        elif (changepix(x,y-1)==1):
            NE(x,y-1,deg)
        

def SE(x,y,deg):
    setColor(getPixel(linePic,x,y), makeColor(255,0,0))
    show(linePic)
    count.c=0
    s = changepix(x+1,y+1)*0+changepix(x+2,y+2)*0+changepix(x+1,y+2)*30+changepix(x,y+1)*45+changepix(x,y+2)*45+changepix(x-1,y+2)*60+changepix(x-1,y+1)*90+changepix(x-2,y+2)*90
    if (count.c==0):
        if (changepix(x+2,y+1)==1):
            FW()
            SE(x+2,y+1,deg)
        elif (changepix(x,y+1)==1):
            FW()
            SE(x,y+1,deg)
        elif (changepix(x+1,y-1)==1):
            L90()
            NE(x+1,y-1,deg)
    s = s/count.c
    print(x,y,deg,s)
    if (s>=deg):
        s=getmin(s)
        deg=s
        if (s==30):
            R30()
            South(x,y+1,deg)
        elif (s==45):
            R45()
            South(x,y+1,deg)
        elif (s==60):
            R60()
            South(x,y+1,deg)
        elif (s==90):
            R90()
            SW(x-1,y+1,deg)
        stop()
    else:
        FW()
        if (changepix(x+1,y+1)==1):
            SE(x+1,y+1,deg)
        elif (changepix(x+2,y+1)==1):
            SE(x+2,y+1,deg)
        elif (changepix(x+1,y+2)==1):
            SE(x+1,y+2,deg)
        elif (changepix(x,y+1)==1):
            SE(x,y+1,deg)
        elif (changepix(x+1,y)==1):
            SE(x+1,y,deg)
                
def SW(x,y,deg):
    setColor(getPixel(linePic,x,y), makeColor(255,0,0))
    show(linePic)
    count.c=0
    s = changepix(x-1,y+1)*0+changepix(x-2,y+2)*0+changepix(x-2,y+1)*30+changepix(x-1,y)*45+changepix(x-2,y)*45+changepix(x-2,y-1)*60+changepix(x-1,y-1)*90+changepix(x-2,y-2)*90
    if (count.c==0):
        if (changepix(x-1,y+2)==1):
            FW()
            SW(x-1,y+2,deg)
        elif (changepix(x-1,y)==1):
            FW()
            SW(x-1,y,deg)
        elif (changepix(x+1,y+1)==1):
            L90()
            SE(x+1,y+1,deg)
    s = s/count.c  
    print(x,y,deg,s)
    if (s>=deg):
        s=getmin(s)
        deg=s
        if (s==30): 
            R30()
            West(x-1,y,deg)
        elif (s==45):
            R45()
            West(x-1,y,deg)
        elif (s==60):
            R60()
            West(x-1,y,deg)
        elif (s==90):
            R90()
            NW(x-1,y-1,deg)
        stop()
    else:
        FW()
        if (changepix(x-1,y+1)==1):
            SW(x-1,y+1,deg)        
        elif (changepix(x-1,y+2)==1):
            SW(x-1,y+2,deg)
        elif (changepix(x-2,y+1)==1):
            SW(x-2,y+1,deg)
        elif (changepix(x-1,y)==1):
            SW(x-1,y,deg)    
        elif (changepix(x,y+1)==1):
            SW(x,y+1,deg)
       
def NW(x,y,deg):
    setColor(getPixel(linePic,x,y), makeColor(255,0,0))
    show(linePic)
    count.c=0
    s = changepix(x-1,y-1)*0+changepix(x-2,y-2)*0+changepix(x-1,y-2)*30+changepix(x,y-1)*45+changepix(x,y-2)*45+changepix(x+1,y-2)*60+changepix(x+1,y-1)*90+changepix(x+2,y-2)*90
    if (count.c==0):
        if (changepix(x-2,y-1)==1):
            FW()
            NW(x-2,y-1,deg)
        elif (changepix(x,y-1)==1):
            FW()
            NW(x,y-1,deg)
        elif (changepix(x-1,y+1)==1):
            L90()
            SW(x-1,y-1,deg)
    s = s/count.c
    print(x,y,deg,s)
    if (s>=deg):
        s=getmin(s)     
        deg=s
        if (s==30): 
            R30()
            North(x,y-1,deg)        
        elif (s==45):
            R45()
            North(x,y-1,deg)
        elif (s==60):
            R60()
            North(x,y-1,deg)
        elif (s==90):
            R90()
            NE(x+1,y-1,deg)
        stop()
    else:
        FW()
        if (changepix(x-1,y-1)==1):
            NW(x-1,y-1,deg)
        elif (changepix(x-2,y-1)==1):
            NW(x-2,y-1,deg)
        elif (changepix(x-1,y-1)==1):
            NW(x-1,y-1,deg)
        elif (changepix(x,y-1)==1):
            NW(x,y-1,deg)
        elif (changepix(x-1,y)==1):
            NW(x-1,y,deg)
                
            
myPic = makePicture("blob.jpg")
X = getWidth(myPic)
Y = getHeight(myPic)

newPic=changesize()

global copyPic
copyPic = copyPicture(newPic)
X = getWidth(newPic)
Y = getHeight(newPic)

blur()

sobel(newPic)

X = getWidth(copyPic)
Y = getHeight(copyPic)

#for i in range(0,X):
#    for j in range(0,Y):
#        if getpix(copyPic,i,j)<100:
#           print(i,j)

global linePic
linePic = copyPicture(copyPic)

count=num(0)

startpoint()
print(m,n)

North(m,n,10)


        
