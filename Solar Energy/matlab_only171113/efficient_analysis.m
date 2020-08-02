function efficiency = efficient_analysis(sun_light,plane)
%#codegen
v1 = plane(:,1)-plane(:,2);
v2 = plane(:,2)-plane(:,3);
z = 1;
temp = v1(2)*v2(1)-v2(2)*v1(1);
x = (-v1(2)*v2(3)+v2(2)*v1(3))/temp;
efficiency = (-v1(3)*v2(1)+v2(3)*v1(1))/temp;
n = [x efficiency z];
sun_direction = sun_light(:,2) - sun_light(:,1);
efficiency = n*sun_direction/(norm(n)*norm(sun_direction));