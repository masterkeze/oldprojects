function [disp_z,disp_y] = control...
    (current_z,target_z,current_y,target_y,max_speed)
disp_z = control_z(target_z,current_z,max_speed);
disp_y = control_y(target_y,current_y,max_speed);
end