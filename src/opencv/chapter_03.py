import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)
# img[200:300, 100:300] = 255, 0, 0
# draw a line
cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)

# draw a rewctangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 3)

# draw a circle
cv2.circle(img, (250, 250), 30, (255, 0, 0), 3)

# add text
cv2.putText(img, "OpenCV", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (150, 0, 150), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)
