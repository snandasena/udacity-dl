import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


# Prepare object pointes
nx = 8
ny = 6

# Make a list of calibration images
fname = '../images/calibration_test.png'
img = cv2.imread(fname)

# convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find the chessboard corners
ret , corners = cv2.findChessboardCorners(gray_img, (nx, ny), None)

# If found, draw corners
if ret:
    cv2.drawChessboardCorners(img, (nx,ny), corners, ret)
    cv2.imshow("Test window", img)

    cv2.waitKey(0)
