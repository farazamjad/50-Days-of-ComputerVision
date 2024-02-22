#USAGE: python Day2/image_drawing.py --image Day2/messi.jpeg --output Day2/output.jpg

#library imports
import argparse
import cv2

#construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',type=str,default='Day2/messi.jpeg',help='path to input image file')
ap.add_argument('-o','--output',type=str,default='Day2/output.jpg',help='path to output image file')

args=vars(ap.parse_args())
#load image file
image=cv2.imread(args['image'])

#draw hollow circle around messi's face and filled circle on his eyes and rectlangle on his lips
cv2.circle(image,(220,290),100,(0,0,255),2)
cv2.circle(image,(210,277),10,(0,0,255),-1)
cv2.circle(image,(255,280),10,(0,0,255),-1)
cv2.rectangle(image,(198,320),(260,340),(0,0,255),-1)

#draw hollow circle around zidane's face and filled circle on his eyes and rectlangle on his lips
cv2.circle(image,(500,200),100,(0,0,255),2)
cv2.circle(image,(470,196),10,(0,0,255),-1)
cv2.circle(image,(520,190),10,(0,0,255),-1)
cv2.rectangle(image,(471,232),(535,259),(0,0,255),-1)

#show output image
cv2.imshow("output",image)
cv2.waitKey(0)

#save output image file
cv2.imwrite(args['output'],image)
