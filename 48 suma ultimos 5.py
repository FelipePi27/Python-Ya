

#Problema:
##Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.


suma=0  #Operacion que pide el problema

print("Bienvenidos")
for f in range(10):
    n=int(input("Ingrese un número: "))
    if f >=5: # se le pide a la variable f que despues del quinto número ingresado comince a sumar los números
        suma=suma+n

print("La suma de los ultimos 5 números ingresados es: ",(suma))

