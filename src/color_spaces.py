import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('../images/test6.jpg')
thresh = (180, 255)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
binary = np.zeros_like(gray)
binary[(gray > thresh[0]) & (gray <= thresh[1])] = 1

plt.imshow(gray, cmap="gray")
plt.show()
plt.imshow(binary, cmap="gray")
plt.show()

R = image[:, :, 0]
plt.imshow(R)
plt.show()
G = image[:, :, 1]
plt.imshow(G)
plt.show()
B = image[:, :, 2]
plt.imshow(B)
plt.show()

thresh = (180, 255)
binary = np.zeros_like(R)
binary[(R >= thresh[0]) & (R <= thresh[1])] = 1
plt.imshow(binary, cmap="gray")
plt.show()

hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
H = hls[:, :, 0]
plt.imshow(H)
plt.show()

L = hls[:, :, 1]
plt.imshow(L)
plt.show()
S = hls[:, :, 2]
plt.imshow(S)
plt.show()

thresh = (90, 255)
binary = np.zeros_like(S)
binary[(S >= thresh[0]) & (S <= thresh[1])] = 1
plt.imshow(binary, cmap="gray")
plt.show()

thresh = (15, 100)
binary = np.zeros_like(H)
binary[(H >= thresh[0]) & (H <= thresh[1])] = 1
plt.imshow(binary, cmap="gray")
plt.show()

