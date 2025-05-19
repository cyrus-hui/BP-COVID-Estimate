import numpy as np


def MovingAverageFilter(inputPPG, windowSize):
    window = np.zeros(windowSize)
    size_in = len(inputPPG)
    p_data = 0
    output = np.zeros(size_in)

    for i in range(size_in):
        window[p_data] = inputPPG[i]
        output[i] = np.sum(window) / windowSize
        p_data += 1
        if p_data >= windowSize:
            p_data = 0

    output[:windowSize] = inputPPG[:windowSize]
    # Keep the output constant when the number of input data is less than windowSize
    return output
