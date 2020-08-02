function draw(sun_light,boat,plane)
%#codegen

x_p = plane(1,:);
y_p = plane(2,:);
z_p = plane(3,:);
fill3(x_p,y_p,z_p,z_p/10+0.5);
hold on
x_b = boat(1,:);
y_b = boat(2,:);
z_b = boat(3,:);
fill3(x_b,y_b,z_b,'g');
hold off
hold on
x_s = sun_light(1,:);
y_s = sun_light(2,:);
z_s = sun_light(3,:);
fill3(x_s,y_s,z_s,'b');
hold off
xlim([-12 12]);
ylim([-12 12]);
zlim([-12 12]);
xlabel('X, North');
ylabel('Y, West');
zlabel('Z');
daspect([1 1 1]);
hold on
efficiency = efficient_analysis(sun_light,plane);
prefix = 'Efficiency = ';
efficiency = num2str(efficiency);
out = strcat(prefix,efficiency);
text(0,0,15,char(out));
hold off
end