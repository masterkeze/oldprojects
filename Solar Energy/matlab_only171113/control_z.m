function disp_z = control_z(target_rad,current_rad,max_speed)
err = 0.001;
current_rad = mod(current_rad,2*pi);
difference = abs(target_rad-current_rad);
if or(difference < err, 2*pi-difference < err)
    disp_z = 0;
else
    if difference <= pi
        disp_z = sign(target_rad-current_rad)*abs(max_speed);
    else
        disp_z = -1*sign(target_rad-current_rad)*abs(max_speed);
%         if current_rad < pi
%             disp_z = abs(max_speed);
%         else
%             disp_z = -1*abs(max_speed);
%         end
    end
end

end