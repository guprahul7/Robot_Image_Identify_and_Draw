from Myro import *
init("COM3")

"""
pic=makePicture("triangle.jpg")
pic=takePicture()
show(pic)
"""

configureBlob(y_low = 0, y_high = 50,
# make a black figure on paper to white figure on computer
u_low = 0, u_high = 255, 
v_low = 0, v_high = 255)


pic=takePicture('blob')
show(pic)
savePicture(pic, "blobpic1.jpg")
"""
pic=makePicture("testpic.jpg")
pic=
"""
white = makeColor(255,255,255)
black = makeColor(0,0,0)
X=int(getWidth(pic))
Y=int(getHeight(pic))

listT=[]
listB=[]
listR=[]
listL=[]
#--------------------------------top

x=1
y=1
while x < X:
    y=1
    while y< Y:
        pixel=getPixel(pic,x,y)
        nextPixel=getPixel (pic, x, y+1)
        if getColor(pixel) == white and getColor(nextPixel)==black: 
            #print(x,y)
            listT.append((x,y+1))
        y+=1
    x+=1
#print(listT)


#-------------------------------- bottom
x=X
y=Y
while x >1:
    y=Y
    while y>1:
        pixel=getPixel(pic,x,y)
        nextPixel=getPixel (pic, x, y-1)
        if getColor(pixel) == white and getColor(nextPixel)==black: 
            #print(x,y)
            listB.append((x,y-1))
        y-=1
    x-=1
#print(listB)

#--------------------------------right

x=X
y=1
while y<Y :
    x=X
    while x>1:
        pixel=getPixel(pic,x,y)
        nextPixel=getPixel (pic, x-1, y)
        if getColor(pixel) == white and getColor(nextPixel)==black: 
            #print(x,y)
            listR.append((x-1,y))
        x-=1
    y+=1
#print(listR)

#---------------------------------left
x=1
y=Y

while y >1 :
    x=1
    while x<X:
        pixel=getPixel(pic,x,y)
        nextPixel=getPixel (pic, x+1, y)
        if getColor(pixel) == white and getColor(nextPixel)==black: 
            #print(x,y)
            listL.append((x+1,y))
        x+=1
    y-=1
#print(listL)



listF=[]

"""
listT.sort(key=lambda row: row[0])
listB.sort(key=lambda row: row[0])
listR.sort(key=lambda row: row[0])
listL.sort(key=lambda row: row[0])
listF.append(listT[0])
listF.append(listT[-1])
listF.append(listB[0])
listF.append(listB[-1])
listF.append(listR[0])
listF.append(listR[-1])
listF.append(listL[0])
listF.append(listL[-1])
#print(list[0])
#print(max(list))
listT.sort(key=lambda row: row[0])
listB.sort(key=lambda row: row[0])
listR.sort(key=lambda row: row[0])
listL.sort(key=lambda row: row[0])
"""

listF.append(listT[0])
listF.append(listT[-1])
listF.append(listB[0])
listF.append(listB[-1])
listF.append(listR[0])
listF.append(listR[-1])
listF.append(listL[0])
listF.append(listL[-1])
#print(list)
#print(list[0])
#print(max(list))
print(listF)
listF=dict.fromkeys(listF).keys()
print(listF)
#print(len(listF))

listF.sort(key=lambda row: row[0])
list1=[]
e2=listF[2]
e3=listF[3]
list1.append(e2)
list1.append(e3)
#print(list1)

list1_1=[]
list1_1.append(e2)
list1_1.append(e3)
print(list1_1)

list111=[]
for (x,y) in list1_1:
    list111.append(x)

print(list111)
print(list111[0])
print(list111[1])
a=int(list111[0])-int(list111[1])
if abs(a) <40 :
    print("rectangle")
else: print("triangle")

