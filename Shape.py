import numpy as np
import math
import cv2

def calculateDistance(x,y):  
    x1=x[0]
    x2=y[0]
    y1=x[1]
    y2=y[1]
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist  
def getShape (img):
    image = img
    blur = cv2.GaussianBlur(image, (3,3), 0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)[1]    
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    c = max(cnts, key=cv2.contourArea)

    left = tuple(c[c[:, :, 0].argmin()][0])
    right = tuple(c[c[:, :, 0].argmax()][0])
    top = tuple(c[c[:, :, 1].argmin()][0])
    bottom = tuple(c[c[:, :, 1].argmax()][0])

    topLeft = (left[0],top[1])
    topRight = (right[0],top[1])
    bottomLeft = (left[0],bottom[1])
    bottomRight = (right[0],bottom[1])

    pts = np.array([topLeft,topRight,bottomRight,bottomLeft],np.int32)
    image = cv2.polylines(image,[pts],True,(0,0,0))

    x = calculateDistance(topLeft,topRight)
    y= calculateDistance(topLeft,bottomLeft)
    
    return x/y




