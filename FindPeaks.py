import numpy as np
from MovingAverageFilter import MovingAverageFilter


def FindPeaks(inputPPG, threshold_low, threshold_high):
    size_in = len(inputPPG)
    index = np.zeros(size_in)
    peak = np.zeros(size_in)
    p_data = 0
    inputPPG_diff = np.diff(inputPPG)
    inputPPG_diff_MA = MovingAverageFilter(inputPPG_diff, 20)  # Calculate moving average of differentiation with window size of 20
    markPeak = np.diff(np.sign(inputPPG_diff_MA))  # Mark points of peaks

    for i in range(1, size_in - 8):  # Start from 1 to avoid index error
        if (markPeak[i + 6] == -2) and (inputPPG[i] < threshold_high) and (inputPPG[i] > threshold_low):
            index[p_data] = i
            peak[p_data] = inputPPG[i]
            p_data += 1

    # Remove 0s in vectors
    index = index[index > 0]
    peak = peak[peak > 0]
    return peak, index
