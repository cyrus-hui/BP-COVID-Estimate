import numpy as np

def RMSofAC(inputPPG, index, cycle_head_index, startpoint):
    RMS_AC = np.zeros(10)

    col = np.where(index == cycle_head_index[startpoint])[0][0]
    firstindex = index[col]
    
    for i in range(10):
        data = inputPPG[int(firstindex) + i: int(firstindex) + i + col * 2]  # 1 true cycle
        dataAC = data - np.mean(data)
        RMS_AC[i] = np.sqrt(np.mean(np.square(dataAC)))
    RMS = np.mean(RMS_AC)
    return RMS
