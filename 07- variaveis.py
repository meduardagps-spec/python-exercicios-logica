lado_1 = float(input("Medida do lado 1 do triângulo:"))
lad0_2 = float(input("Medida do lado 2:"))
lado_3 = float(input("Medida do lado 3:"))

a = lado_1 + lado_2
b = lado_1 + lado_3
c = lado_2 + lado_3

if l1<c and l2<a and l3<b:
    print("Esses comprimentos formam um triângulo!")
else:
    print("Essas medidas não formam um triângulo!")

