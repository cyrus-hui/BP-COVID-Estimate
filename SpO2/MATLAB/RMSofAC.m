%calculating RMS of AC part and 
function RMS = RMSofAC ( inputPPG, index, cycle_head_index, startpoint )
%inputPPG : raw data after moving average.
%AvRMS : average of 10 RMS values.

RMS_AC = zeros(1, 10);
[row, col] = find( index ==  cycle_head_index(startpoint));
firstindex = index(col);

for i = 1:10
   data = inputPPG(firstindex + i - 1 : firstindex + i); % 1 true cycle
   dataAC = data - mean(data);
   RMS_AC(i) = rms(dataAC);
end

RMS = mean(RMS_AC);

end
