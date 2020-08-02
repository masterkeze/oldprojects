function speed = set_speed(max,target,current)
%#codegen
target = mod(target,2*pi);
current = mod(current,2*pi);
if abs(target-current) >0.01
    if and (current >= 0, current < pi)
        if and(target > current,target <= current + pi)
            speed = abs(max);
        else
            speed = -abs(max);
        end
    else
        if or(target>current, target<= mod(current+pi,2*pi))
            speed = abs(max);
        else
            speed = -abs(max);
        end
    end
else
    speed = 0;
end
end