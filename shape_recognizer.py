from Myro import *
pic = makePicture("star.jpg")   
show(pic) 

#find bottom right pixel of shape
for pixel in getPixels(pic):
    if  (getRed(pixel)<255) and (getGreen(pixel)<255) and (getBlue(pixel)<255): 
        xvalue=getX(pixel)
        yvalue=getY(pixel)
#print (xvalue)
#print (yvalue)

#tests if blob
if (xvalue==0 or xvalue==1):
    print("blob")
    quit()

#traces bottom right pixel left until it reaches a white pixel    
xvaluend=xvalue-1
pixel = getPixel(pic, xvaluend, yvalue)
while (getRed(pixel)<255) and (getGreen(pixel)<255) and (getBlue(pixel)<255):
    xvaluend=xvaluend-1
    pixel = getPixel(pic, xvaluend, yvalue)
#print(xvaluend)

#picks between triangle, square, or star
if (xvalue-xvaluend)>3:
    pixel = getPixel(pic, xvalue,yvalue-3)
    if (getRed(pixel)<255) and (getGreen(pixel)<255) and (getBlue(pixel)<255):
        print("square")
    else:
        print("triangle")  
else:
   print("star")