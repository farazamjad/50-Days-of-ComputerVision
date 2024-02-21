#USAGE
#   command= python loading_images_with_openCV.py --input data/img1.png --output data/out.jpg
        
#import libraries
import argparse 
import cv2

#argument parsing
ap=argparse.ArgumentParser()
ap.add_argument('-i','--input',required=True,help='input path to image')
ap.add_argument('-o','--output',required=True,help='output path to image')

#converts to dict key:value
#{INPUT:DATA/MY.JPG}
args=vars(ap.parse_args())

#loading image using cv2.imread

image=cv2.imread(args['input'])
#grab spatial dimensions width,height and channels
(h,w,c)=image.shape[:3]

# 600 pixels x 400 pixels  normally
#  ^width    ^height   but in (h,w,c) we write like this as in matrix its rows x columns where rows=height and columns = width

print(f"width: {w} pixels")
print(f"height: {h} pixels")
print(f"channels: {c}")

# show image and wait for keypress
cv2.imshow("Jacket sticker",image)
cv2.waitKey(0)

#write new image, OpenCv handles converting image filetypes automatically)
cv2.imwrite(args['output'],image)

