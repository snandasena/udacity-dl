import cv2
import numpy as np
import matplotlib.pyplot as plt 
# Read an image
img = cv2.imread('../images/curved-lane.jpg')

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply sobel x
sobel_x = cv2.Sobel(gray, cv2.CV_64F,1,0,ksize=13)
#cv2.imshow("Sobel X", sobel_x)
#cv2.waitKey(1000)

sobel_y = cv2.Sobel(gray, cv2.CV_64F,0,1,ksize=5)
#cv2.imshow("Sobel Y", sobel_y)
#cv2.waitKey(1000)

abs_sobel_x = np.absolute(sobel_x)
#cv2.imshow("Absolute Sobel X",abs_sobel_x)
#cv2.waitKey(1000)

scaled_sobel_x = np.uint8(255*abs_sobel_x/np.max(abs_sobel_x))
#cv2.imshow("Scaled Sobel X", scaled_sobel_x)
#cv2.waitKey(1000)

# Create binary thresold to select pixels based on gradient strenth
thresh_mn = 20
thresh_mx = 100

(thresh, img_bw) = cv2.threshold(
        scaled_sobel_x, 
        thresh_mn, 
        thresh_mx, 
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow("CV2 Binary", img_bw)
cv2.waitKey(0)

