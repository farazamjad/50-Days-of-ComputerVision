import argparse

ap=argparse.ArgumentParser()
ap.add_argument('-n','--name',required=True,help='Name of the user')
args=vars(ap.parse_args())
print(args)
print(f"Hi there {args['name']}, it's nice to meet you!")



#Count shapes from image

# import argparse
# import cv2
# import imutils

# ap=argparse.ArgumentParser()
# ap.add_argument('-i', '--input',required=True,help='input path to image')
# ap.add_argument('-o', '--output',required=True,help='output path to image')
# args=vars(ap.parse_args())
# print(args)

# image=cv2.imread(args['input'])

# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# blur=cv2.GaussianBlur(gray,(5,5),0)
# thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]

# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# # loop over the contours and draw them on the input image
# for c in cnts:
# 	cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
# # display the total number of shapes on the image
# text = "I found {} total shapes".format(len(cnts))
# cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
# 		(0, 0, 255), 2)
# # write the output image to disk
# cv2.imwrite(args["output"], image)