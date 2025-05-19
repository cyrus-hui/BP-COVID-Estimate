%moving average
function [output] = MovingAverageFilter(inputPPG,windowSize)

window = zeros(1,windowSize);
size_in = size(inputPPG);
p_data = 1;
output = zeros(size_in);
 
for i = 1:max(size_in)
    window(p_data) = inputPPG(i);
    output(i) = sum(window)/windowSize;
    p_data = p_data+1;
    if p_data > windowSize
        p_data = 1;
    end
end

output(1:windowSize) = inputPPG(1:windowSize);%Keep the output constant when the number of input data is less than windowSize
 
end
