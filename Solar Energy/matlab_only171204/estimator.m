% This program is to estimate the harvest of solar energy and consumption
% of solar energy

% setting of parameters

width = 175 * 10 .^(-3);
height = 185 * 10.^(-3);
conversion_rate = 0.12;
standard_capacity = 1000; %watt per m^2

max_capacity = 3;
start = 7; % 7am
duration = 10; % 10 hours

latitude = 22;
longitude = 114;
time_zone = 8;
y=2017;
mo=4;
d=16;
mi=0;
s=0;

mass_of_plane = 0.3; %kg
mass_of_rod = 0.2; %kg

sample_size = duration*60;
record = zeros(sample_size,8);

turn = 0;
while turn < sample_size
    [elevation_rad,azimuth_rad] = Solar_Angle_Calculation...
    (latitude,longitude,time_zone,y,mo,d,start+turn/60,mi,s);
    R_target = get_target(elevation_rad,azimuth_rad);
    [Rz_rad_raw,Ry_rad_raw] = set_angle(R_target,R_boat);
    [Rz_rad,Ry_rad] = modify(Rz_rad_raw,Ry_rad_raw);
    
    R_control = rotate_z(Rz_rad)*rotate_y(Ry_rad);
    
    sun_light = get_sun_light(R_target);
    plane_raw = get_plane(eye(3),eye(3));
    plane_control = get_plane(eye(3),R_control);
    
    efficient_raw = efficient_analysis(sun_light,plane_raw);
    efficient_control = efficient_analysis(sun_light,plane_control);
    
    record(turn+1,1) = efficient_raw*max_capacity*60;
    record(turn+1,3) = max(0,efficient_control*max_capacity*60);
    
    if rem(turn,60) == 0
        record(turn+1,5) = max(0,efficient_control*max_capacity*60);
    else
         record(turn+1,5) = record(turn);
    end
    
    if rem(turn,1) == 0
        record(turn+1,7) = max(0,efficient_control*max_capacity*60);
    else
         record(turn+1,7) = record(turn);
    end
    
    if turn ==0
        record(1,2) = record(1,1);
        record(1,4) = record(1,3);
        record(1,6) = record(1,5);
    else
        record(turn+1,2) = record(turn,2)+record(turn+1,1);
        record(turn+1,4) = record(turn,4)+record(turn+1,3);
        record(turn+1,6) = record(turn,6)+record(turn+1,5);
        record(turn+1,8) = record(turn,8)+record(turn+1,7);
    end
    

    turn = turn + 1;
end

h(1) = subplot(2,2,1);
plot(record(:,2));
xlabel(' without control');
ylabel('J ½¹¶ú');
fprintf(num2str(record(sample_size,2)));
fprintf('\n');
h(2) = subplot(2,2,2);
plot(record(:,4));
xlabel(' ideal situation');
ylabel('J ½¹¶ú');
fprintf(num2str(record(sample_size,4)));
fprintf('\n');
h(3) = subplot(2,2,3);
plot(record(:,6));
xlabel(' control each hour');
ylabel('J ½¹¶ú');
fprintf(num2str(record(sample_size,6)));
fprintf('\n');
h(4) = subplot(2,2,4);
plot(record(:,8));
xlabel(' control each half hour');
ylabel('J ½¹¶ú');
fprintf(num2str(record(sample_size,8)));
fprintf('\n');
% h(1) = subplot(2,2,1);
% plot(record(:,1));
% xlabel('Instantaneous energy harvest without control');

% h(3) = subplot(2,2,3);
% plot(record(:,3));
% xlabel('Instantaneous energy harvest ideally');













