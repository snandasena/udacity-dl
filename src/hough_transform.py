# imports
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def imshow(img):
    cv2.imshow("test", img)
    cv2.waitKey(0)


# Read images using OpenCv
image = cv2.imread("../images/exit-ramp.jpg")
# imshow(image)

# grayscale the image
gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# imshow(gray_img)

# define kernal size and apply Gaussian smoothing
kernal_size = 5
blur_gray = cv2.GaussianBlur(gray_img, (kernal_size, kernal_size), 0)
# imshow(blur_gray)

# define parameter for Canny and apply
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# create a mask
mask = np.zeros_like(edges)
ignore_mask_color = 255

# defining four sided polygon to mask
imshape = image.shape
vertices = np.array([[(0, imshape[0]),
                      (450, 290),
                      (490, 290),
                      (imshape[1], imshape[0])]], dtype=np.int32)

cv2.fillPoly(mask, vertices, ignore_mask_color)
masked_edges = cv2.bitwise_and(edges, mask)

# define the Hough transform parameters

rho = 1
theta = np.pi / 180
threshold = 1
min_line_len = 5
max_line_gap = 1
line_image = np.copy(image) * 0

# Run Hough on edge detected image
lines = cv2.HoughLinesP(masked_edges,
                        rho,
                        theta,
                        threshold,
                        np.array([]),
                        min_line_len,
                        max_line_gap)

# Iterate over the output "lines" and draw and lines on a blank image
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10)

# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges))

# Draw the lines on the edge image
line_edges = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)

cv2.imshow("test window", line_edges)
cv2.waitKey(0)