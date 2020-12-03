import pickle
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read in the saved camera matrix and distortion coefficients
# These are the arrays you calculated using cv2.calibrateCamera()
dist_pickle = pickle.load( open( "../calibration_wide/wide_dist_pickle.p", "rb" ) )
mtx = dist_pickle["mtx"]
dist = dist_pickle["dist"]

img = cv2.imread("../calibration_wide/test_image2.png")
nx = 8
ny = 6

cv2.imshow("Original", img)
cv2.waitKey(1000)

def corners_unwrap(img, nx, ny, mtx, dist):

    # Undistort using mtx and dist
    undst = cv2.undistort(img, mtx, dist, None, mtx)
    # coverting to grayscale
    gray = cv2.cvtColor(undst, cv2.COLOR_BGR2GRAY)
    # find chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
    print(ret)
    M = None
    warped = np.copy(img)
    if ret:
        cv2.drawChessboardCorners(undst, (nx, ny), corners, ret)
        img_size = (img.shape[1], img.shape[0])
        
        src = np.float32([corners[0], corners[nx-1], corners[-1], corners[-nx]])
        offset = 100
        dst = np.float32([
                        [offset, offset], [img_size[0]-offset,offset],
                        [img_size[0]- offset, img_size[1] -offset],
                        [offset, img_size[1] - offset]])

        # given src and dst points, calculate the prespective transform matrix
        M = cv2.getPerspectiveTransform(src, dst)
        warped = cv2.warpPerspective(undst, M, img_size)
    
    return warped, M


top_down, perspective_m = corners_unwrap(img, nx, ny, mtx,dist)

cv2.imshow("Original", img)
cv2.imshow("Undistot", top_down)
cv2.waitKey(0)
