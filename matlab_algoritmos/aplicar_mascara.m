function  S1 = aplicar_mascara(A, m)


x=size(A);
n=size(m);
div=n(1)*n(2);
sumar=0;
for i=1:1:x(1)-3
    for j=1:1:x(2)-3
    sumar=0;
        for i1=1:1:n(1)
            for j1=1:1:n(2)
                X1=A(i+i1,j+j1)*m(i1,j1);
                sumar=X1+sumar;
            end
        end
        S1(i,j)=sumar;
    end
end