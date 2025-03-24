function S2 = binarizacion(S1, u)

x=size(S1);
for i=1:1:x(1)-3
    for j=1:1:x(2)-3
        if (S1(i,j) <= u )
            S2(i,j) = 255;
        else 
             S2(i,j) = 0;
        end
    end
end