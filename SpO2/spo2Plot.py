import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from scipy.signal import find_peaks

def normalize(data):
  nor_data = (data - np.min(data)) / (np.max(data) - np.min(data))
  return nor_data

filename = "/"
data = pd.read_csv(filename).values
raw_r = data[:, 0]
raw_ir = data[:, 1]

l = 1000
raw_r = raw_r[:l]
raw_ir = raw_ir[:l]

r_peaks, _ = find_peaks(raw_r, distance = 50) 
ir_peaks, _ = find_peaks(raw_ir, distance = 50)

# ecg_r = normalize(raw_r)
# ecg_ir = normalize(raw_ir)

plt.figure(figsize=(10,4))
plt.plot(raw_r, label='PPG Red', color='b')
plt.plot(raw_ir, label='PPG Inf', color='c')
plt.plot(r_peaks, raw_r[r_peaks], "x")
plt.plot(ir_peaks, raw_ir[ir_peaks], "x" )
plt.xlabel('Time')
plt.ylabel('Ampiltude')
plt.title('ECG')
plt.grid()
plt.show()
