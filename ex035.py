l1=float(input("Medida do lado 1 do triângulo:"))
l2=float(input("Medida do lado 2:"))
l3=float(input("Medida do lado 3:"))
a=l1+l2
b=l1+l3
c=l2+l3
if l1<c and l2<a and l3<b:
    print("Esses comprimentos formam um triângulo!")
else:
    print("Essas medidas não formam um triângulo!")
