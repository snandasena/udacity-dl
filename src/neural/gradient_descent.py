import numpy as np

def sigmoid(x):

    return (1 / (1 + np.exp(-x)))


learnrate = 0.5
x = np.array([1,2])
y = np.array(0.5)

# initial weights
w = np.array([0.5, -0.5])

# calculate output of neural network
nn_output = sigmoid(np.dot(x,w))

# calculate error of neural network
error = y - nn_output

# calculate change of weigts
del_w = learnrate * error * nn_output * (1 - nn_output) * x

print("Neural network output: ", nn_output)
print("Amounf of error: ", error)
print("Change of weights: ", del_w)

