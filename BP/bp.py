import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from scipy.signal import find_peaks
import os
from find10 import find10

def normalize(data):
  nor_data = (data - np.min(data)) / (np.max(data) - np.min(data))
  return nor_data

pat_record = []
pat_start = []
pat_end = []

#replace string with the folder path
filename = "/"
data = pd.read_csv(filename).values
#adjust the column of the csv to correspond each signals
record = data[:, 0]
bp_sys_start = data[:, 6]
bp_sys_end = data[:, 7]
bp_dia_start = data[:, 8]
bp_dia_end = data[:, 9]

#replace string with the folder path
folder_path = "/"
csv_files = os.listdir(folder_path)
csv_files.sort()
for filename in csv_files:
    if filename.endswith('.csv'):
        
        file_path = os.path.join(folder_path, filename)
        data = pd.read_csv(file_path).values
        time = data[:, 0]
        ecg = data[:, 1]
        ecg_peaks = data[:,2]
        ppg = data[:, 3]

        filename = filename [:-4]
        pat_record.append(filename)

        nor_ecg = normalize(ecg)
        nor_ppg = normalize(ppg)
        ecg_p = []
        ppg_peaks, _ = find_peaks(nor_ppg, distance = 150)

        for i in range(len(time)):
          time[i] = datetime.strptime(time[i], "%Y-%m-%d %H:%M:%S.%f")
        for i in range(len(time)):
          if ecg_peaks[i] == 1:
            ecg_p.append(i)
        
        ecg_head, ecg_tail, ppg_head, ppg_tail = find10(ecg_p, ppg_peaks)

        pat_head = []
        pat_tail = []
        for i in range(10):
          pat_head.append((ppg_head[i] - ecg_head[i]) * 2)
          pat_tail.append((ppg_tail[i] - ecg_tail[i]) * 2) 
        pat_head_avg = np.average(pat_head)
        pat_tail_avg = np.average(pat_tail)
        
        pat_start.append(pat_head_avg)
        pat_end.append(pat_tail_avg)



