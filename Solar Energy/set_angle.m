function [Rz_rad,Ry_rad] = set_angle(R_target,R_boat)
%#codegen
R_modify = R_boat\R_target;
Rz_rad = atan2(R_modify(2,3),R_modify(1,3));
Ry_rad = atan2(R_modify(2,3),R_modify(3,3)*sin(Rz_rad));
% Rz_boat = atan2(R_boat(2,1),R_boat(1,1));
% Rx_boat = atan2(R_boat(3,2),R_boat(3,3));
% Ry_rad = atan2(-R_target(3,1),R_target(3,3));
% Rz_rad = atan2(-R_target(1,2),R_target(2,2));

Ry_rad = mod(Ry_rad,2*pi);
if Ry_rad > pi
    Ry_rad = 2*pi - Ry_rad;
    Rz_rad = Rz_rad + pi;
end
Rz_rad = mod(Rz_rad,2*pi);
end