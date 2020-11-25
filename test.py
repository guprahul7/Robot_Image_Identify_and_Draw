from Myro import *
robot="COM3"
init(robot)

'''
p=takePicture()
show(p)

'''
configureBlob(y_low = 0, y_high = 20,
# make a black figure on paper to white figure on computer
u_low = 0, u_high = 255, 
v_low = 0, v_high = 255)
b_pic=takePicture('blob')
show(b_pic)


white = makeColor(255,255,255)
black = makeColor(0,0,0)
x=1
y=1

while x < int(getWidth(b_pic)):
    y=1
    while y< int (getHeight(b_pic)):
        pixel=getPixel(b_pic,x,y)
        nextPixel=getPixel (b_pic, x, y+1)
        if getColor(pixel) == white and getColor(nextPixel)==black: 
            print(x,y)
        y+=1
    x+=1
        


