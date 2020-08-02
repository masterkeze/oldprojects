function [Rz_rad,Ry_rad] = modify(Rz_rad,Ry_rad)
if Ry_rad < pi
    Ry_rad = 2*pi - Ry_rad;
    Rz_rad = Rz_rad + pi;
end
if Ry_rad < 3/2*pi
    Ry_rad = 3*pi - Ry_rad;
    Rz_rad = Rz_rad + pi;
end
Rz_rad = mod(Rz_rad,2*pi);
end