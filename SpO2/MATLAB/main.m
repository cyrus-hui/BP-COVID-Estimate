clear all

CASENUM = 31;

for CASEID = 1:CASENUM
    CASEID = CASEID - 1;

    fileSerial1 = (CASEID-mod(CASEID,10))/10 + 7;%case serials:01--31
    fileSerial2 = mod(CASEID,10); 
    fileName = ['F:/20221108PPG/csv/HR_80_SpO2_',num2str(fileSerial1),num2str(fileSerial2)]; 
    data = xlsread(fileName);
    raw_PPGr = data(:,1);
    raw_PPGir = data(:,2);
    
    % step 1. calculating moving average of LED signals with window size of 15
    % [output] = MovingAverageFilter(inputPPG,windowSize)
    PPGr_MAF = MovingAverageFilter(raw_PPGr, 15);
    
    % step 2. finding peaks 
    % [peak, index] = FindPeaks(inputPPG,threshold_low,threshold_high),
    % inputPPG here should be raw data after moving average.
    [peak_r, index_r] = FindPeaks(PPGr_MAF, 40000, 50000);
    
    % step 3. finding 10 true cycles by checking if 45<PR<200
    % [cycle_head_value, cycle_head_index, cycle_foot_value, cycle_foot_index ] = Find10TrueCycles(peak, index, bpm_threshold_h, bpm_threshold_l,f)
    [PPGr_cycle_head_value, PPGr_cycle_head_index, PPGr_cycle_foot_value, PPGr_cycle_foot_index ] = Find10TrueCycles(peak_r, index_r, 200, 45, 100);
    
    % step 4. calculating RMS of AC part 
    % [RMS_AC, AvRMS ] = RMSofAC ( inputPPG, index, cycle_head_index, startpoint )
    % inputPPG here should be raw data.
     size_cycles = size(PPGr_cycle_head_value);
     startpoint = floor(max(size_cycles)/4);
%    startpoint_1 = floor(max(size_cycles)*3/4);
     rRMS = RMSofAC ( raw_PPGr, index_r, PPGr_cycle_head_index, startpoint);
     irRMS = RMSofAC ( raw_PPGir, index_r, PPGr_cycle_head_index, startpoint);
%      rRMS_1 = RMSofAC ( raw_PPGr, index_r, PPGr_cycle_head_index, startpoint_1);
%      irRMS_1 = RMSofAC ( raw_PPGir, index_r, PPGr_cycle_head_index, startpoint_1);
     
     CASEID = CASEID + 1;
     R(CASEID) = rRMS/irRMS;
%     R_1(CASEID) = rRMS_1/irRMS_1;
end


for i = 1:max(size(R))
    if ( R(i) < 2 ) && ( R(i) > 0.5 )
     SpO2(i) = -47.60*R(i)*R(i) + 130.93*R(i) + 8.49;
    else R(i) = R(i - 1);
    end
end



