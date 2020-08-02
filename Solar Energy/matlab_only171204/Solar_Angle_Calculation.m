function [elevation_rad, azimuth_rad] = Solar_Angle_Calculation...
    (latitude_toN,longtiude_toE,time_zone,y,mo,d,h,mi,s)
%   This function caculate the elevation angle
%   Detailed explanation goes here
julian_day = julian_date(y,mo,d,h,mi,s);
julian_century = (julian_day-2451545)/36525;
geom_mean_long_sun = mod(280.46646+julian_century*...
    (36000.76983+julian_century*0.0003032),360);
geom_mean_anom_sun = 357.52911+julian_century*...
    (35999.05029-0.0001537*julian_century);
eccent_earth_orbit = 0.016708634-julian_century*...
    (0.000042037+0.0000001267*julian_century);
sun_eq_of_ctr = sin(deg2rad(geom_mean_anom_sun))*...
    (1.914602-julian_century*(0.004817+0.000014*julian_century))+...
    sin(deg2rad(2*geom_mean_anom_sun))*...
    (0.019993-0.000101*julian_century)+...
    sin(deg2rad(3*geom_mean_anom_sun))*0.000289;
sun_true_long = geom_mean_long_sun + sun_eq_of_ctr;
sun_true_anom = geom_mean_anom_sun + sun_eq_of_ctr;
%disp(sun_true_long);
%disp(sun_true_anom);
mean_obliq_ecliptic = 23+(26+((21.448-julian_century*...
    (46.815+julian_century*(0.00059-julian_century*0.001813))))/60)/60;
obliq_corr = mean_obliq_ecliptic+0.00256*...
    cos(deg2rad(125.04-1934.136*julian_century));
sun_app_long = sun_true_long-0.00569-0.00478*...
    sin(deg2rad(125.04-1934.136*julian_century));
var_y = tan(deg2rad(obliq_corr/2))*tan(deg2rad(obliq_corr/2));
sun_declin = rad2deg(asin(sin(deg2rad(obliq_corr))*...
    sin(deg2rad(sun_app_long))));
eq_of_time = 4*rad2deg(var_y*sin(2*deg2rad(geom_mean_long_sun))...
    -2*eccent_earth_orbit*sin(deg2rad(geom_mean_anom_sun))...
    +4*eccent_earth_orbit*var_y*sin(deg2rad(geom_mean_anom_sun))...
    *cos(2*deg2rad(geom_mean_long_sun))...
    -0.5*var_y*var_y*sin(4*deg2rad(geom_mean_long_sun))...
    -1.25*eccent_earth_orbit*eccent_earth_orbit*sin(2*deg2rad(geom_mean_anom_sun)));
%disp(eq_of_time);
time_past_midnight = h/24 + mi/1440 + s/86400;
true_solar_time = mod(time_past_midnight*1440+eq_of_time+4*longtiude_toE-60*time_zone,1440);
if true_solar_time/4 <0
    hour_angle = true_solar_time/4+180;
else
    hour_angle = true_solar_time/4-180;
end
solar_zenith_angle = rad2deg(acos(sin(deg2rad(latitude_toN))*sin(deg2rad(sun_declin))+...
    cos(deg2rad(latitude_toN))*cos(deg2rad(sun_declin))*cos(deg2rad(hour_angle))));
elevation_deg = 90 - solar_zenith_angle;
if hour_angle > 0
    azimuth_deg = mod(rad2deg(acos(((sin(deg2rad(latitude_toN))*cos(deg2rad(solar_zenith_angle)))-...
        sin(deg2rad(sun_declin)))/(cos(deg2rad(latitude_toN))*sin(deg2rad(solar_zenith_angle)))))+180,360);
else
    azimuth_deg = mod(540-rad2deg(acos(((sin(deg2rad(latitude_toN))*cos(deg2rad(solar_zenith_angle)))-...
        sin(deg2rad(sun_declin)))/(cos(deg2rad(latitude_toN))*sin(deg2rad(solar_zenith_angle))))),360);
end
elevation_rad = deg2rad(elevation_deg);
azimuth_rad = deg2rad(azimuth_deg);
%disp(elevation_rad);
%disp(azimuth_rad);
end
function rad=deg2rad(deg)
rad = double(deg)/180*pi;
end
function deg=rad2deg(rad)
deg = double(rad)/pi*180;
end
function julian_day = julian_date(y,mo,d,h,mi,s)
julian_day_number = (1461*(y + 4800 + (mo - 14)/12))/4 +(367*(mo - 2 - 12 * ((mo - 14)/12)))/12 -...
    (3 * ((y + 4900 + (mo - 14)/12)/100))/4 + d - 32075;
julian_day = julian_day_number + (h-12)/24 + mi/1440 + s/86400;
end
