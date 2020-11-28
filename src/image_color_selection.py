import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
image = mpimg.imread("../images/test.jpg")

print("This image is: ", type(image))
print("Image shape", image.shape)

#
ysize = image.shape[0]
xsize = image.shape[1]

color_select = np.copy(image)

red_threshold = 0
green_threshold = 0
blue_threashold = 0

rgb_threashold = [red_threshold, green_threshold, blue_threashold]

thresholds = (image[:,:,0] < rgb_threashold[0]) \
            |(image[:,:,1] < rgb_threashold[1])\
            |(image[:,:,2] < rgb_threashold[2])

color_select[thresholds] = [0, 0, 0]

plt.imshow(color_select)
plt.show()
