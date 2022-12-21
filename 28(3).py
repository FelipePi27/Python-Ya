
#While

##Problema:
#Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor ingresado de uno en uno.
#Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30.

#Es de FUNDAMENTAL importancia analizar los diagramas de flujo y la posterior codificación en Python de los siguientes problemas, 
#en varios problemas se presentan otras situaciones no vistas en el ejercicio anterior.

""" n=int(input("ingrese el valor final: "))
x=1
while x <=n:
    print(x)
    x=x+1 """



##Problema:Desarrollar un programa que permita la carga de 10 valores por teclado 
# y nos muestre posteriormente la suma de los valores ingresados y su promedio.

x=1
suma=0
while x<=10:
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    x=x+1
promedio=suma/10
print("La suma de los 10 valores es")
print(suma)
print("El promedio es")
print(promedio)













