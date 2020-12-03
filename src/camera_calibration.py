import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

# prepare objects points
objp = np.zeros((6*8, 3), np.float32)
objp[:,:2] = np.mgrid[0:8, 0:6].T.reshape(-1,2)

# Arrays to store object points and iamg points from all the images
objpoints = []
imgpoints = []

# make a list of calibration images
images = glob.glob('../calibration_wide/GO*.jpg')

for inx, fname in enumerate(images):
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (8,6), None)

    # if found, add object points, image points
    if ret:
        objpoints.append(objp)
        imgpoints.append(corners)

        # draw and display the corners
        cv2.drawChessboardCorners(img, (8,6),corners, ret)

        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()


