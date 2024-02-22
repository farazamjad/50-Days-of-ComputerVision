#USAGE: python Day2/basic_drawing.py

#import libraries
import numpy as np
import cv2

#intializing empty canvas with 600x600 pixels and 3 channels(RGB) and black background
canvas=np.zeros((600,600,3),dtype='uint8')

#draw red line from top-right corner to bottom-left corner of canvas

red=(0,0,255)
cv2.line(canvas,(0,600),(600,0),red)
cv2.imshow("Red Line on Canvas",canvas)


#draw 3 pixel thick green line from top-left corner to bottom-right corner of canvas
green=(0,255,0)
cv2.line(canvas,(0,0),(600,600),green,3)
cv2.imshow("3 pixel thick Green Line on Canvas",canvas)


#draw a green 100x100 pixel square starting at 100x100  and ending at 200x200
cv2.rectangle(canvas,(100,100),(200,200),green,)
cv2.imshow("Green Square",canvas)

#draw a red square with 5 pixel thickness
cv2.rectangle(canvas,(400,100),(500,200),red,5)
cv2.imshow("Red Square",canvas)

#draw blue rectangle with 10 pixel thickness
blue=(255,0,0)
cv2.rectangle(canvas,(100,500),(500,575),blue,10)
cv2.imshow("Blue Rectangle",canvas)

# canvas=np.zeros((600,600,3),dtype='uint8')
#cX=shape[1] as in matrix y * x
(cX,cY)=(canvas.shape[1]//2,canvas.shape[0]//2)
white = (255,255,255)
cv2.circle(canvas,(cX,cY),100,white)
cv2.imshow("white circle",canvas)

#bulls eye with circle
canvas=np.zeros((600,600,3),dtype='uint8')
(cX,cY)=(canvas.shape[1]//2,canvas.shape[0]//2)
white = (255,255,255)
for r in range(0,300,25):
    cv2.circle(canvas,(cX,cY),r,white)

canvas=np.zeros((600,600,3),dtype='uint8')
#drawing random 25 circles
for i in range(0,25):
    #generate random radius between 5 to 200
    radius=np.random.randint(5,high=500)
    #generate random 3 values of (b,g,r) and converting from np array to list  
    color=np.random.randint(0,high=256,size=(3,)).tolist()
    #random center point
    pt=np.random.randint(0,high=500,size=(2,))
    #-1 shows that the circle should be filled 
    cv2.circle(canvas,tuple(pt),radius,color,-1)
cv2.imshow("Random Circle",canvas)
cv2.waitKey(0)
