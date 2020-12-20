import numpy as np

def softmax(L):
    expL = np.exp(L)
    sumExpl = np.sum(expL)

    result = []
    for i in expL:
        result.append(i * 1.0/sumExpl)

    return result


if __name__ == "__main__":
    L = [5,6,7]

    print(softmax(L))
