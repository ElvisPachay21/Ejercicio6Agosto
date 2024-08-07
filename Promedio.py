N1 = int(input("Ingrese el primer promedio: "))
N2 = int(input("Ingrese el segundo promedio: "))
N3 = int(input("Ingrese el tercer promedio: "))
N4 = int(input("Ingrese el cuarto promedio: "))

P = ( N1 + N2 + N3 + N4 ) / 4
print(P)

if P > 89 and P < 101  :
    print("A")
    
elif P > 79 and P < 90 :
    print("B")
elif P > 69 and P < 80 :
    print("C")
elif P > 59 and P < 70 :
    print("D")
elif P >= 0 and P < 60   :
    print("E")

 