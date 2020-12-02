import cv2
import numpy as np

# Read an image
img = cv2.imread("../../images/exit-ramp.jpg")
print(img.shape)
cv2.imshow("Original Image", img)

# Resize an iamge
img_resized = cv2.resize(img, (400, 300))
cv2.imshow("Resized Image", img_resized)
print(img_resized.shape)

img_croped = img[100:400, 400:500]
cv2.imshow("Croped Image", img_croped)

cv2.waitKey(0)
