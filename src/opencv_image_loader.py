import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

binary_warped = mpimg.imread("../images/warped-example.jpg")
# cv2.imshow("tmp", binary_warped)
# cv2.waitKey(0)

nonzero = binary_warped.nonzero()
nonzerox = nonzero[1]
nonzerox = np.array(nonzerox)
print(nonzerox)
nonzeroy = nonzero[0]

print(len(nonzerox))

histogram = np.sum(binary_warped[binary_warped.shape[0] // 2:, :], axis=0)
plt.plot(histogram)
plt.show()
# Create an output image to draw on and visualize the result
out_img = np.dstack((binary_warped, binary_warped, binary_warped))
# print(out_img)
cv2.imshow("temp", out_img)
cv2.waitKey(0)

