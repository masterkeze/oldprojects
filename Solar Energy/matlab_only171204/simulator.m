% This program is to establish the simulation
% environment for solar energy project

duration = 20;
fps = 10;
max_speed = pi;% rad/s
interval = 1/fps;

latitude = 22;
longitude = 114;
time_zone = 8;
y=2017;
mo=4;
d=16;
h=7;
mi=0;
s=0;

position_z = 0;
position_y = 0;

record = zeros(fps*duration,12);
begin = get_second(clock);
current = get_second(clock);
turn = 0;
while ( turn < fps*duration)
    frame_begin = get_second(clock);
    Rb_z = -1 * turn * (pi/36)/fps;
    Rb_x = Rx_controller(turn * (pi/12)/fps);
    
    R_boat = rotate_z(Rb_z)*rotate_x(Rb_x);
    R_boat = eye(3);
    h = 0.5*turn/fps + 6;
    
    [elevation_rad,azimuth_rad] = Solar_Angle_Calculation...
    (latitude,longitude,time_zone,y,mo,d,h,mi,s);
    R_target = get_target(elevation_rad,azimuth_rad);
    [Rz_rad_raw,Ry_rad_raw] = set_angle(R_target,R_boat);
    [Rz_rad,Ry_rad] = modify(Rz_rad_raw,Ry_rad_raw);
    %control part
    [disp_z,disp_y] = control(position_z,Rz_rad,...
        position_y,Ry_rad,max_speed*interval);
    position_z = position_z + disp_z;
    position_y = position_y + disp_y;
    R_final = rotate_z(position_z)*rotate_y(position_y);
    
    sun_light = get_sun_light(R_target);
    boat = get_boat(R_boat);
    plane = get_plane(R_boat,R_final);
    figure(1);
    draw(sun_light,boat,plane);
    position_z = mod(position_z,2*pi);
    position_y = mod(position_y,2*pi);
    
    record(turn+1,1) = rad2deg(position_z);
    record(turn+1,2) = rad2deg(position_y);
    record(turn+1,3) = rad2deg(Rz_rad);
    record(turn+1,4) = rad2deg(Ry_rad);
    record(turn+1,5) = rad2deg(Rz_rad_raw);
    record(turn+1,6) = rad2deg(Ry_rad_raw);
    record(turn+1,7) = efficient_analysis(sun_light,plane);
    record(turn+1,8) = efficient_analysis(sun_light,get_plane(eye(3),eye(3)));
    if turn >= 2
        velocity_z = (record(turn+1,3) - record(turn,3))/interval;
        velocity_y = (record(turn+1,4) - record(turn,4))/interval;
        if abs(velocity_z) >100
            velocity_z = record(turn,9);
        end
        if abs(velocity_y) >100
            velocity_y = record(turn,10);
        end
        record(turn+1,9) = velocity_z;
        record(turn+1,10) = velocity_y;
    end
    if turn >= 2
        record(turn+1,11) = (record(turn+1,9) - record(turn-1,9))/interval/2;
        record(turn+1,12) = (record(turn+1,10) - record(turn-1,10))/interval/2;
    end
    figure(2);
    h(1) = subplot(3,2,1);
    ylim([0 360]);
    plot(record(:,1:4));
    xlabel('target and practical position')
    
    h(2) = subplot(3,2,2);
    plot(record(:,3),'b');hold on
    plot(record(:,5),'r');hold off
    ylim([0 360]);
    xlabel('theoretical(r) and modified(b) Rz');
    
    h(3) = subplot(3,2,3);
    plot(record(:,4),'b');hold on
    plot(record(:,6),'r');hold off
    ylim([0 360]);
    xlabel('theoretical(r) and modified(b) Ry');
    
    h(4) = subplot(3,2,4);
    %plot(record(:,4));
    %ylim([0 360]);
    plot(record(:,7),'b');hold on
    plot(record(:,8),'r');hold off
    ylim([-1.2 1.2]);
    xlabel('efficiency with and without control');
    
    h(5) = subplot(3,2,5);
    plot(record(:,9),'b');
    %plot(record(:,10),'r');hold off
    
    h(6) = subplot(3,2,6);
    plot(record(:,10),'b');
    %plot(record(:,12),'r');hold off
    
    frame_end = get_second(clock);
    if (frame_end - frame_begin < interval)
        pause(frame_end - frame_begin);
    end
    
    turn = turn + 1;
    current = get_second(clock);
end

