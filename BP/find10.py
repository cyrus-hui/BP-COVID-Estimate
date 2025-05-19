def find10(ecg_p, ppg_peaks):
  ecg_head = []
  ecg_tail = []
  ppg_head = []
  ppg_tail = []
  i = 1
  j = 1
  while len(ecg_head) < 10:
    curr_pat = ppg_peaks[i] - ecg_p[j]
    if ppg_peaks[i] > ecg_p[j]  > ppg_peaks[i - 1]:
      if 90 < curr_pat < 110:
        ecg_head.append(ecg_p[j])
        ppg_head.append(ppg_peaks[i])
      i = i + 1
      j = j + 1
    elif ppg_peaks[i] == ecg_p[j] or ppg_peaks[i - 1] == ecg_p[j]:
      i = i + 1
      j = j + 1
    elif ecg_p[j] < ppg_peaks[i - 1]:
      j = j + 1
    else:
      i = i + 1


  i = -2
  j = -2

  while len(ecg_tail) < 10:
    curr_pat = ppg_peaks[i] - ecg_p[j]
    if ppg_peaks[i] > ecg_p[j] > ppg_peaks[i - 1]:
      if 90 < curr_pat < 110:
        ecg_tail.append(ecg_p[j])
        ppg_tail.append(ppg_peaks[i])
      i = i - 1
      j = j - 1
    elif ppg_peaks[i] == ecg_p[j] or ppg_peaks[i - 1] == ecg_p[j]:
      i = i - 1
      j = j - 1
    elif ppg_peaks[i] < ecg_p[j]:
      j = j - 1
    else:
      i = i - 1
  
  return ecg_head, ecg_tail, ppg_head, ppg_tail
