# Import the Myro libraries
from Myro import *

# Windows users: set IsMac to False
IsMac = False

# Mac users: replace 08ED with your Fluke ID
#init_mac = '/dev/tty.Fluke2-08ED-Fluke2'

# Windows users: replace COM3 with your COM ID
init_win = 'COM256'

# Initialize Fluke2 board
init(init_mac if IsMac else init_win)

def picture_position():
    while True:        
        translate(.5)
        left = getObstacle(0)
        center = getObstacle(1)
        right = getObstacle(2)
        
        if 4500 <= left and 4500 <= center and 4500 <= right: #straight approach
            stop()
            backward(.5,3)
            break
        
        elif left >=  4500 and right <= 4500: #angled approach (left sensor activated first)
            stop()
            while True:
                right = getObstacle(2)
                rotate(-.5)
                if right >= 4500:
                    stop()
                    backward(.5,3)
                    break
            break
        
        elif left <=  4500 and right >= 4500: #right sensor activated first
            stop()
            while True:
                left = getObstacle(0)
                rotate(-.5)
                if left >= 4500:
                    stop()
                    backward(.5,3)
                    break
            break
        
        
    
