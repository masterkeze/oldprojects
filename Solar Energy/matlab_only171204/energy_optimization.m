%control optimization
%suppose the consumption is unknown
%this script will try to find out the optimal theshold of efficiency,
%which is used to adjust the position of two axes.

function total_energy = energy_optimization(efficiency_threshold,consumption)
    
    max_capacity = 3; % watt
    start = 7;%Am
    duration = 10; % 10 hours
    sample_size = duration*60;

    cold_start = 100; % the minimun cost to activate the machine
    
    latitude = 22;
    longitude = 114;
    time_zone = 8;
    y=2017;
    mo=4;
    d=16;
    mi=0;
    s=0;
    
    total_energy = 0;
    last_z = 0;
    last_y = 0;
    turn = 0;
    while turn < sample_size
        [elevation_rad,azimuth_rad] = Solar_Angle_Calculation...
        (latitude,longitude,time_zone,y,mo,d,start+turn/60,mi,s);
        R_target = get_target(elevation_rad,azimuth_rad);
        [Rz_rad_raw,Ry_rad_raw] = set_angle(R_target,eye(3));
        [Rz_rad,Ry_rad] = modify(Rz_rad_raw,Ry_rad_raw);
        
        sun_light = get_sun_light(R_target);
        current_plane = get_plane(eye(3),rotate_z(last_z)*rotate_y(last_y));
        current_efficiency = efficient_analysis(sun_light,current_plane);
        total_energy = total_energy + max(0,current_efficiency*max_capacity*60);
        if current_efficiency < efficiency_threshold
            total_energy = total_energy - (abs(Rz_rad-last_z)+abs(Ry_rad-last_y))*consumption - 2*cold_start;
            last_z = Rz_rad;
            last_y = Ry_rad;
        end
        %fprintf(num2str(current_efficiency));
        %fprintf('\n');
        turn = turn + 1;
    end
end


















