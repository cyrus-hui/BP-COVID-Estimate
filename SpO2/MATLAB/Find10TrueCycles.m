%find 10 true PPG cyles
function [cycle_head_value, cycle_head_index, cycle_foot_value, cycle_foot_index ] = Find10TrueCycles(peak, index, bpm_threshold_h, bpm_threshold_l,f)
% peak, index are outputs of FindPeaks.
% f is the Sampling frequency of PPG.
     size_in = size(peak);
     cycle_head_value = zeros(1, max(size_in));
     cycle_head_index = zeros(1, max(size_in));
     cycle_foot_value = zeros(1, max(size_in));
     cycle_foot_index = zeros(1, max(size_in));
     %45 < PR <200, so index_threshold_h = 133, index_threshold_l = 30
     index_threshold_l = (f*60)/bpm_threshold_h;
     index_threshold_h = (f*60)/bpm_threshold_l;
     
     a = zeros(1, max(size_in)); %Determine if there are 10 consecutive cycles that satisfy the condition
     p_data = 1;
     
     for i = 5:11:max(size_in)-11
         for j = 1:10
             index_difference = index(i+j)-index(i+j-1);
             b = (index_difference < index_threshold_h)&(index_difference > index_threshold_l);
             a(i) = b + a(i);
         end
          if a(i) == 10
             cycle_head_index(p_data) = index(i);
             cycle_head_value(p_data) = peak(i);
             cycle_foot_index(p_data) = index(i+10);
             cycle_foot_value(p_data) = peak(i+10);
             p_data = p_data + 1;
         end
     end

     cycle_head_index = cycle_head_index(cycle_head_index > 0);
     cycle_head_value = cycle_head_value(cycle_head_value > 0);
     cycle_foot_index = cycle_foot_index(cycle_foot_index > 0);
     cycle_foot_value = cycle_foot_value(cycle_foot_value > 0);
     
end