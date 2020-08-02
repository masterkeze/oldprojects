function plane = get_plane(Rb,Rfinal)
%#codegen
R0 = Rb*Rfinal;
w = 5;
plane = [w w -w -w;w -w -w w;0 0 0 0];
plane = R0*plane;
end