function result = draw_peak(e_start,e_step,c_start,c_step,n)
i = 1;
j = 1;
result = zeros(n);
while i < n + 1
    while j < n + 1
        result(i,j) = energy_optimization(e_start + e_step * (j-1),c_start + c_step*(i-1));
        j = j + 1;
    end
    j = 1;
    i = i + 1;
end
surf(result);
end