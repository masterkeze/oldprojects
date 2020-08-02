function sun_light = get_sun_light(R_target)
%#codegen
vector = [0 0;0 0;1 8];
sun_light = R_target*vector;
end