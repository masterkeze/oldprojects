function disp_y = control_y(target_rad,current_rad,max_speed)
err = 0.1;
current_rad = mod(current_rad,2*pi);
difference = abs(target_rad-current_rad);
if difference > err
    if difference <= pi
        disp_y = sign(target_rad-current_rad)*abs(max_speed);
    else
        disp_y = -1*sign(target_rad-current_rad)*abs(max_speed);
    end
else
    disp_y = 0;
end

end