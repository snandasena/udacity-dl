import numpy as np

np.random.seed(42)


def step_func(t):
    if t >= 0:
        return 1

    return 0


def prediction(X, W, b):
    return step_func((np.matmul(X, W) + b)[0])


def perceptron_step(X, y, W, b, lrate=0.01):
    for i in range(len(X)):
        y_hat = prediction(X[i], W, b)

        if y[i] - y_hat == 1:

            W[0] += X[i][0] * lrate
            W[1] += X[i][1] * lrate
            b += lrate

        elif y[i] - y_hat == -1

            W[0] -= X[i][0] * lrate
            W[1] -= X[i][1] * lrate
            b -= lrate

    return W, b


def train(X, y, lrate=0.01, nepochs=25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])

    W = np.random.rand(2, 1)
    b = np.random.rand(1)[0] + x_max

    boundarey_lines = []
    for i in range(nepochs):
        W, b = perceptron_step(X, y, W, b, lrate)
        boundarey_lines.append((-W[0] / W[1], -b / W[1]))

    return boundarey_lines
