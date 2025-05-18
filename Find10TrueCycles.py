import numpy as np


def Find10TrueCycles(peak, index, bpm_threshold_h, bpm_threshold_l, f):
    size_in = len(peak)
    cycle_head_value = np.zeros(size_in)
    cycle_head_index = np.zeros(size_in)
    cycle_foot_value = np.zeros(size_in)
    cycle_foot_index = np.zeros(size_in)

    index_threshold_l = (f * 60) / bpm_threshold_h
    index_threshold_h = (f * 60) / bpm_threshold_l

    a = np.zeros(size_in)
    p_data = 0

    for i in range(5, size_in - 11, 11):
        for j in range(1, 11):
            index_difference = index[i + j] - index[i + j - 1]
            b = (index_difference < index_threshold_h) and (index_difference > index_threshold_l)
            a[i] += b

        if a[i] == 10:
            cycle_head_index[p_data] = index[i]
            cycle_head_value[p_data] = peak[i]
            cycle_foot_index[p_data] = index[i + 10]
            cycle_foot_value[p_data] = peak[i + 10]
            p_data += 1

    cycle_head_index = cycle_head_index[cycle_head_index > 0]
    cycle_head_value = cycle_head_value[cycle_head_value > 0]
    cycle_foot_index = cycle_foot_index[cycle_foot_index > 0]
    cycle_foot_value = cycle_foot_value[cycle_foot_value > 0]

    return cycle_head_value, cycle_head_index, cycle_foot_value, cycle_foot_index
