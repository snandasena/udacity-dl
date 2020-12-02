import cv2
import numpy as np

# Read an image
img = cv2.imread("../../images/test.jpg")

# grayscale using opencv
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", img_gray)

# blur using opencv
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
cv2.imshow("Blur Image", img_blur)

# Canny edge detect
img_canny = cv2.Canny(img_gray, 100, 200)
cv2.imshow("Canny Image", img_canny)

# Dialation
kernal = np.ones((5, 5), np.uint8)
img_dialation = cv2.dilate(img_canny, kernal, iterations=1)
cv2.imshow("Dialation Image",img_dialation)

# Eroded
img_erode = cv2.erode(img_dialation, kernal, iterations=1)
cv2.imshow("Erode Image", img_erode)

cv2.waitKey(0)
