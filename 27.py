####Condisiones con Operadores logicos####
##Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación 
# (debe mostrar el mayor y el menor de ellos)

print("Bienvenidos,Ingrese tres números")

n1=int(input("ingrese el primer valor: "))
n2=int(input("ingrese el segundo valor: "))
n3=int(input("ingrese el tercer valor: "))

promedio=(n1+n2+n3//3)

if n1<n2 and n1<n3:
    print("El primer número ingresado es el menor:",(n1))
else:
    if n2<n3:
        print("El segundo número ingresado es el menor:",(n2))
    else:
        print("El tercee número ingresado es el menor:",(n3))

    
if n1>n2 and n1>n3:
    print("El primer número ingresado es el mayor:",(n1))
else:
    if n2>n3:
        print("El segundo número ingresado es el mayor:",(n2))
    else:
        print("El tercer número ingresado es el mayor:",(n3))



