function b = Rx_controller(in)
%#codegen
rotate_limit = pi/4;
temp = mod(in,4*rotate_limit);
b = temp;
if and (temp >=0, temp<rotate_limit)
    b = temp;
end
if and (temp >=rotate_limit, temp<3*rotate_limit)
    b = 2*rotate_limit - temp;
end
if temp >=3*rotate_limit
    b = temp - 4*rotate_limit;
end

end
