##problema:
##Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo 
# y a este resultado se lo multiplica por el tercero.

print("Bienvenidos,Ingrese tres números")

n1=int(input("ingrese el primer valor: "))
n2=int(input("ingrese el segundo valor: "))
n3=int(input("ingrese el tercer valor: "))

suma=n1+n2
producto=suma*n3
 
if n1==n2 and n1==n3:
    print("La suma corresponde a:",(suma))
    print("El producto corresponde a:",(producto))

     

