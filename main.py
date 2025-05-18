import pandas as pd
from MovingAverageFilter import MovingAverageFilter
from FindPeaks import FindPeaks
from Find10TrueCycles import Find10TrueCycles
from RMSofAC import RMSofAC
import os

CASENUM = 31
R = []
folder_path = "/Users/cyrushui/Desktop/LURA/csv"
csv_files = os.listdir(folder_path)
csv_files.sort() 
for filename in csv_files:
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        data = pd.read_csv(file_path).values
        raw_PPGr = data[:, 0]
        raw_PPGir = data[:, 1]

        # Step 1. Calculating moving average of LED signals with window size of 15
        PPGr_MAF = MovingAverageFilter(raw_PPGr, 15)

        # Step 2. Finding peaks
        peak_r, index_r = FindPeaks(PPGr_MAF, 40000, 50000)

        # Step 3. Finding 10 true cycles by checking if 45 < PR < 200
        PPGr_cycle_head_value, PPGr_cycle_head_index, PPGr_cycle_foot_value, PPGr_cycle_foot_index = Find10TrueCycles(peak_r, index_r, 200, 45, 95)

        # Step 4. Calculating RMS of AC part
        size_cycles = len(PPGr_cycle_head_value)
        startpoint = size_cycles // 4
        rRMS = RMSofAC(raw_PPGr, index_r, PPGr_cycle_head_index, startpoint)
        irRMS = RMSofAC(raw_PPGir, index_r, PPGr_cycle_head_index, startpoint)

        R.append(rRMS / irRMS)

SpO2 = []
for i in range(len(R)):
    if 0.5 < R[i] < 2:
        SpO2.append(-47.60 * R[i] * R[i] + 130.93 * R[i] + 8.49)
    else:
        SpO2.append(SpO2[i - 1] if i > 0 else 0)

# Print the results or save them as needed
# print("SpO2 values:", SpO2)

for i in range(len(SpO2)):
    #print(f"{i + 69} --> {SpO2[i]:.2f}   [{(SpO2[i] - 69 - i):.2f}]")
    print(f"{(SpO2[i] - 69 - i):.2f}")





# file_path = "/Users/cyrushui/Desktop/LURA/csv/HR_80_SPO2_70.csv"
# data = pd.read_csv(file_path).values
# raw_PPGr = data[:, 0]
# raw_PPGir = data[:, 1]

# # Step 1. Calculating moving average of LED signals with window size of 15
# PPGr_MAF = MovingAverageFilter(raw_PPGr, 15)

# # Step 2. Finding peaks
# peak_r, index_r = FindPeaks(PPGr_MAF, 40000, 50000)

# # Step 3. Finding 10 true cycles by checking if 45 < PR < 200
# PPGr_cycle_head_value, PPGr_cycle_head_index, PPGr_cycle_foot_value, PPGr_cycle_foot_index = Find10TrueCycles(peak_r, index_r, 200, 45, 100)

# # Step 3.5 Find heart rate

# # hr = len(raw_PPGr) / len(peak_r)
# # hz = hr / 60
# # cycle = 125 / hz
# # print(hr, hz, cycle)

# # Step 4. Calculating RMS of AC part
# size_cycles = len(PPGr_cycle_head_value)
# startpoint = size_cycles // 4
# rRMS = RMSofAC(raw_PPGr, index_r, PPGr_cycle_head_index, startpoint)
# irRMS = RMSofAC(raw_PPGir, index_r, PPGr_cycle_head_index, startpoint)

# R.append(rRMS / irRMS)

# SpO2 = []
# for i in range(len(R)):
#     if 0.5 < R[i] < 2:
#         SpO2.append(-47.60 * R[i] * R[i] + 130.93 * R[i] + 8.49)
#     else:
#         SpO2.append(SpO2[i - 1] if i > 0 else 0)

# # Print the results or save them as needed
# print("SpO2 values:", SpO2)

