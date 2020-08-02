function R_target = get_target(elevation,azimuth)

a = 2*pi - azimuth;
b = pi/2 - elevation;
Rz = [cos(a) -sin(a) 0;sin(a) cos(a) 0;0 0 1];
Ry = [cos(b) 0 sin(b);0 1 0;-sin(b) 0 cos(b)];
R_target = Rz*Ry;
end