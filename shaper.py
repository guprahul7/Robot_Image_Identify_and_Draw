from Myro import *
init("COM3")



def picture():
    configureBlob(y_low = 0, y_high = 30,
    # lower y max if there is no white part
    u_low = 0, u_high = 255, 
    v_low = 0, v_high = 255)        
    pic = takePicture("blob")
    return (pic)

def triangle():
    backward (1,2)
    turnBy(90)
    for a in range (3):
        forward(0.5,2)
        turnBy(120)
def rectangle():
    #backward (1,2)
    #turnBy(90)
    for a in range (4):
        forward(0.2,0.5)
        turnBy(90)      
def star():
    backward (1,2)
    turnBy(90)
    for a in range (5):
        forward(0.5,2)
        turnBy(144)  
        forward(0.5,2)
        turnBy(-72.5)  
 


def shapePicker(pic):

    
    import math

    #find left most pixel
    xvalue=0
    yvalue=0
    fin=False
    a={}
    while (fin==False):
        while (yvalue<getHeight(pic)):
            pixel = getPixel(pic, xvalue, yvalue) 
            if  (getRed(pixel)==255) or (getGreen(pixel)==255) or (getBlue(pixel)==255): 
                fin=True
                xvaluel=xvalue
                yvaluel=yvalue
            yvalue=yvalue+1
        yvalue=0
        xvalue=xvalue+1



    #find right most pixel
    xvalue=getWidth(pic)
    yvalue=1
    fin=False
    while (fin==False):
        while (yvalue<getHeight(pic) and fin==False):
            pixel = getPixel(pic, xvalue, yvalue) 
            if  ((getRed(pixel)==255) or (getGreen(pixel)==255) or (getBlue(pixel)==255)): 
                fin=True
                xvaluer=xvalue
                yvaluer=yvalue
            yvalue=yvalue+1
        yvalue=0
        xvalue=xvalue-1

      
    #find coordinates of uppermost boundary of the shape
    xvalue=xvaluel
    yvalue=0
    while (xvalue<=xvaluer):
        while (yvalue<getHeight(pic)):
            pixel = getPixel(pic, xvalue, yvalue)
            if (getRed(pixel)==255) and (getGreen(pixel)==255) and (getBlue(pixel)==255):  
                a[xvalue]=yvalue
                break;
            else:
                yvalue+=1       
        xvalue+=1
        yvalue=0
    #divide the upper boundary into four parts and calculate each relative slope, for every four pixels

    sector =(xvaluer-xvaluel)/2.608
    xvalue=xvaluel
    pslope=0
    count=0
    while (xvalue+4)<(sector+xvaluel):
        pslope+=(a[xvalue]-a[xvalue+4])/4
        xvalue+=4   
        count+=1
    slope1=pslope/count
    print(slope1)

    xvalue=int(xvaluel+sector)
    pslope=0
    count=0
    while (xvalue+4)<((xvaluel+xvaluer)/2):
        pslope+=(a[xvalue]-a[xvalue+4])/4
        xvalue+=4   
        count+=1
    slope2=pslope/count
    print(slope2)

    xvalue=int((xvaluel+xvaluer)/2)
    pslope=0
    count=0
    while (xvalue+4)<(xvaluel+sector*1.818):
        pslope+=(a[xvalue]-a[xvalue+4])/4
        xvalue+=4   
        count+=1
    slope3=pslope/count
    print(slope3)


    xvalue=int(xvaluel+(sector*1.608))
    pslope=0
    count=0
    while (xvalue+4)<(xvaluer):
        pslope+=(a[xvalue]-a[xvalue+4])/4
        xvalue+=4
        count+=1
    slope4=pslope/count
    print(slope4)

#compares the slopes and resolves the data into a shape
    if (abs(slope2))<0.2 and abs(slope3)<0.2:
        #shape="square"
        print("sq")
        square()
    elif ((slope2-slope3*-1)<0.2) and (slope2>1.35):
        #shape="triangle"
        print("tr")
        triangle()
    elif (abs(slope1)<0.2 and (abs(slope4<0.2)) and ((slope2-slope3*-1)<0.7)):
        #shape="star"
        print("st")
        star()
    else:
        #shape="blob"
        print("bl")
        from test import *
        blob()
    #return(shape)
    


#----------------actual code starts
print("start")
pic=picture()
show(pic)
#savePicture(pic,"testing1.jpg")
shapePicker(pic)











