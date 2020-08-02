function boat = get_boat(Rb)
w=5;
boat = [-w -w 1.5*w;-w w 0;0 0 0];
boat = Rb*boat;
boat = boat - [0 0 0;0 0 0;8 8 8];
end