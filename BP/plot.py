import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from scipy.signal import find_peaks, argrelmin

def normalize(data):
  nor_data = (data - np.min(data)) / (np.max(data) - np.min(data))
  return nor_data

#file path on one single patient
filename = "/"
data = pd.read_csv(filename).values
#adjust the column to correspond the signal
time = data[:, 0]
ecg = data[:, 1]
ecg_peaks = data[:,2]
ppg = data[:, 3]

#change the value of l to change the timeframe
#l = 2000 means it shows data from the first 2000 ms of measuring
l = 2000
ecg = ecg[:l]
ppg = ppg[:l]
ecg_peaks = ecg_peaks[:l]
time = time[:l]

nor_ecg = normalize(ecg)
nor_ppg = normalize(ppg)
ecg_p = []
ppg_peaks, _ = find_peaks(nor_ppg, distance = 150)


for i in range(len(time)):
  time[i] = datetime.strptime(time[i], "%Y-%m-%d %H:%M:%S.%f")
for i in range(len(time)):
  if ecg_peaks[i] == 1:
    ecg_p.append(i)

local_minima = []
for i in range(1, len(ppg_peaks)):
    segment = nor_ppg[ppg_peaks[i-1]:ppg_peaks[i]]
    min_idx = np.argmin(segment)
    local_minima.append(ppg_peaks[i-1] + min_idx)

print(local_minima)

plt.figure(figsize=(10,4))
plt.plot(nor_ecg, label='ECG Signal', color='b')
plt.plot(nor_ppg, label='PPG Signal 1', color='c')
plt.plot(ppg_peaks, nor_ppg[ppg_peaks], "x")
plt.plot(ecg_p, nor_ecg[ecg_p], "x")
plt.plot(local_minima, nor_ppg[local_minima], "o") 
plt.xlabel('Time (ms)')
plt.ylabel('Ampiltude')
plt.title('PPG Signal')
plt.grid()
plt.show()
