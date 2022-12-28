
#Problema:
#Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente 
# la suma de los valores ingresados y su promedio. Este problema ya lo desarrollamos, 
# lo resolveremos empleando la estructura for para repetir la carga de los diez valores por teclado.

suma=0  
for x in range(10):
    valor=int(input("Ingrese un número: "))
    suma=suma+valor
print("La suma del total de números ingresados corresponde a: ",(suma))
promedio=suma/10
print("El promedio correponde a: ",(promedio))
