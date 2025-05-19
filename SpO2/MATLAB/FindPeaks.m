%find peaks and their indexes
function [peak, index] = FindPeaks(inputPPG,threshold_low,threshold_high)
%threshold value is used to remove extreme peak values. 
%For red light, threshold_low = 40000, threshold_high = 50000
%For infra-red light, threshold_low = 50000, threshold_high = 60000

size_in = size(inputPPG);
index = zeros(1,max(size_in));
peak = zeros(1,max(size_in));
p_data = 1;
inputPPG_diff = diff(inputPPG);
inputPPG_diff_MA = MovingAverageFilter(inputPPG_diff, 20); %Calculate moving average of differetiation with window size of 20
markPeak = diff(sign(inputPPG_diff_MA));%mark points of peaks 

for i=2:max(size_in)-8      %start from 2 otherwise i-1 could be 0
    if (markPeak(i+6)==-2) &&  (inputPPG(i) < threshold_high) && (inputPPG(i) > threshold_low)
        index(p_data) = i;
        peak(p_data) = inputPPG(i);
    end
    p_data = p_data + 1;
end

%remove 0 in vectors
index = index(index>0);
peak = peak(peak>0);


end