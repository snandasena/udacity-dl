import cv2
import numpy as np

img = cv2.imread('../../images/test.jpg')
cv2.circle(img, (443, 342), 5, (0, 0, 255), -1)
cv2.circle(img, (155, 534), 5, (0, 0, 255), -1)
cv2.circle(img, (771, 528), 5, (0, 0, 255), -1)
cv2.circle(img, (502, 342), 5, (0, 0, 255), -1)
cv2.line(img, (443, 342), (502, 342), (0, 255, 0), 3)
cv2.line(img, (771, 528), (502, 342), (0, 255, 0), 3)
cv2.line(img, (771, 528), (155, 534), (0, 255, 0), 3)
cv2.line(img, (155, 534), (443, 342), (0, 255, 0), 3)


pst1 = np.float32([[443, 342], [155, 534], [771, 528], [502, 342]])
pst2 = np.float32([[0, 0], [0,960], [540,0], [ 540,960]])
print(img.shape[:2])
matrix = cv2.getPerspectiveTransform(pst1, pst2)
rest = cv2.warpPerspective(img, matrix, img.shape[:2])
cv2.imshow("temp", img)
# cv2.imshow("rest", rest)
cv2.waitKey(0)
