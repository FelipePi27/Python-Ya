##Recordar While-While
###
### #Problema:
##Realizar un programa que permita cargar dos listas de 15 valores cada una. 
# Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

List_1=0
List_2=0
print("Ingrese números de Lista 1")
x=1
while x <= 15:
    valor=int(input("Ingrese un número: "))
    List_1=List_1+valor
    x=x+1
print("Ingrese números de Lista 2")
x=1
while x <= 15:
    valor=int(input("Ingrese un número: "))
    List_2=List_2+valor
    x=x+1

if List_1>List_2:
    print("Lista 1 es mayor")
else:
    if List_2>List_1:
        print("Lista 2 es mayor")
    else:
        print("la suma de los valores ingresados en las listas sumados independientemente una de la otra, es igual")
