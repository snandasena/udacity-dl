import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread("../images/test.jpg")

print("This image is: ", type(image))
print("Image shape", image.shape)
