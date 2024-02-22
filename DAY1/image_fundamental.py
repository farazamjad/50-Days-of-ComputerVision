# !USAGE= python DAY1/image_fundamental.py --image 'DAY1/data/img2.jpeg'
#import libraries
import argparse
import cv2

#construct argument parser and parse the arguments
ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',type=str,default='data/my.jpg')
args=vars(ap.parse_args())
#load the image
image=cv2.imread(args['image'])
#extract height and width
(h,w)=image.shape[:2]
print(h,w)

#show orignal image to screen
cv2.imshow("Orignal Image",image)
#cv2.waitKey(0)

#Images are simply numpy arrays and the origin is (0,0) located at top-left corner
(b,g,r)=image[0,0]
#RGB normally but we use BGR as OpenCV uses this format

print(f"Pixel at (0,0) - Red :{r},Green:{g},Blue:{b}")

#x=50 y=20 in matrix format its hxw thats why the cordinates are inverted
(b,g,r)=image[20,50]
print(f"Pixel at (50,20) - Red :{r},Green:{g},Blue:{b}")

(b,g,r)=image[330,800]
print(f"Pixel at (50,20) - Red :{r},Green:{g},Blue:{b}")

#update pixel value at x=50 y=20 and set it to red
image[20,50]=(0, 0 , 255)
#             ^  ^     ^
#             b  g      r
(b,g,r)=image[20,50]
print(f"Pixel at (50,20) - Red :{r},Green:{g},Blue:{b}")
#we can use numpy arrays for cropping and changing pixel values from selected region
#calculating center coordinates of image
(cX,cY)=(w//2,h//2)
print(cX,cY)

#top left corner of image
#image[startY:endY,startX:endX]
top_l=image[0:cY,0:cX]
cv2.imshow("Top Left Corner",top_l)

#top right corner of image
top_r=image[0:cY,cX:w]
cv2.imshow("Top Right Corner",top_r)

#bottom left corner of image
bot_l=image[cY:h,0:cX]
cv2.imshow("Bottom Left Corner",bot_l)
#bottom right corner of image
bot_r=image[cY:h,cX:w]
cv2.imshow("Bottom Right Corner",bot_r)

#updating top left corner to red
image[0:cY,cX:w]=(0,0,255)
cv2.imshow("Updated Top left corner",image)
cv2.waitKey(0)